import unittest
from unittest.mock import patch
import generate as g


class ContractTests(unittest.TestCase):
    def test_no_duplicate_v1_or_foreign_token_destination(self):
        self.assertEqual(g.normalize_base('https://toapis.cn/v1/'), 'https://toapis.cn/v1')
        for value in ('https://evil.example', 'http://toapis.cn', 'https://toapis.cn/v1/v1'):
            with self.assertRaises(ValueError):
                g.normalize_base(value)

    def test_reference_contract_and_fixed_single_image(self):
        p = g.build_payload('Keep subject', 'https://files.toapis.com/ref.png')
        self.assertEqual(p['reference_images'], ['https://files.toapis.com/ref.png'])
        self.assertEqual(p['n'], 1)
        self.assertEqual(p['resolution'], '1k')
        self.assertNotIn('image', p)

    def test_async_lifecycle(self):
        responses = [{'status': 'queued'}, {'status': 'in_progress'},
                     {'status': 'completed', 'result': {'data': [{'url': 'https://files.toapis.com/out.png'}]}}]
        with patch.object(g, 'api_json', side_effect=responses), patch.object(g.time, 'sleep'):
            task, history = g.poll('https://toapis.cn/v1', 'test-key', 'test-task')
        self.assertEqual(len(history), 3)
        self.assertEqual(g.result_url(task), 'https://files.toapis.com/out.png')

    def test_failed_http200_is_failure(self):
        with patch.object(g, 'api_json', return_value={'status': 'failed'}), patch.object(g.time, 'sleep'):
            with self.assertRaises(RuntimeError):
                g.poll('https://toapis.cn/v1', 'test-key', 'test-task')

    def test_rate_limit_query_retries_without_post(self):
        done = {'status': 'completed', 'url': 'https://files.toapis.com/out.png'}
        with patch.object(g, 'api_json', side_effect=[g.APIError(429, 12), done]) as call, patch.object(g.time, 'sleep') as sleep:
            g.poll('https://toapis.cn/v1', 'test-key', 'test-task')
        self.assertTrue(all(x.args[0] == 'GET' for x in call.call_args_list))
        self.assertGreaterEqual(sleep.call_args_list[1].args[0], 12)


if __name__ == '__main__':
    unittest.main()
