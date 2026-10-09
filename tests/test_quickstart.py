import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
import quickstart


class QuickstartTests(unittest.TestCase):
    def test_request_routes_and_models_match_documentation(self):
        expected = {
            "chat": ("/chat/completions", "gpt-6.1-sol"),
            "image": ("/images/generations", "gpt-image-2-vip"),
            "video": ("/videos/generations", "seedance-2"),
        }
        for kind, (path, model) in expected.items():
            with self.subTest(kind=kind):
                actual_path, body = quickstart.build_request(kind, "test")
                self.assertEqual((actual_path, body["model"]), (path, model))

    def test_image_quality_applies_only_to_vip(self):
        _, vip = quickstart.build_request("image", "test")
        self.assertEqual((vip["resolution"], vip["quality"]), ("1k", "low"))
        _, standard = quickstart.build_request("image", "test", "gpt-image-2")
        self.assertNotIn("quality", standard)
    def test_video_first_call_is_four_seconds_720p_without_audio(self):
        _, body = quickstart.build_request("video", "test")
        self.assertEqual(body["duration"], 4)
        self.assertEqual(body["resolution"], "720p")
        self.assertEqual(body["size"], "16:9")
        self.assertIs(body["generate_audio"], False)
    def test_completed_task_uses_documented_result_shape(self):
        task = {"status": "completed", "result": {"data": [{"url": "https://example.com/result.png"}]}}
        self.assertEqual(quickstart.result_url(task), "https://example.com/result.png")

    def test_china_base_url_and_existing_v1_are_not_duplicated(self):
        self.assertEqual(quickstart.api_base("https://toapis.cn"), "https://toapis.cn/v1")
        self.assertEqual(quickstart.api_base("https://toapis.com/v1/"), "https://toapis.com/v1")


if __name__ == "__main__":
    unittest.main()
