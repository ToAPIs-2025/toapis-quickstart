import assert from 'node:assert/strict'
import { test } from 'node:test'
import { generateToAPIs, isToAPIsBase } from './dist/lib/providers/toapis.js'
const png = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aN7sAAAAASUVORK5CYII=', 'base64')
const json = body => new Response(JSON.stringify(body), { headers:{'content-type':'application/json'} })
test('async task result becomes an image; credentials go only to the API, POST occurs once', async () => {
  const original = globalThis.fetch; const calls = []
  globalThis.fetch = async (url, init) => {
    calls.push({url,init})
    if (init.method === 'POST') return json({id:'fixture_1'})
    if (String(url).includes('/fixture_1')) return json({status:'completed',result:{data:[{url:'https://assets.example/image.png'}]}})
    assert.equal(init.headers, undefined); return new Response(png,{headers:{'content-type':'image/png'}})
  }
  try {
    const result = await generateToAPIs('fixture-key','https://toapis.cn/v1','gpt-image-2',{prompt:'fixture',aspectRatio:'16:9',resolution:'1K'})
    assert.equal(result.imageBase64,png.toString('base64'))
    assert.deepEqual(JSON.parse(calls[0].init.body),{model:'gpt-image-2',prompt:'fixture',size:'16:9',resolution:'1k',n:1,response_format:'url'})
    assert.equal(calls.filter(call=>call.init.method==='POST').length,1)
    assert.equal(calls[1].url,'https://toapis.cn/v1/images/generations/fixture_1')
  } finally { globalThis.fetch=original }
})
test('failed task retains ID and never resubmits', async () => {
  const original=globalThis.fetch; let posts=0
  globalThis.fetch=async (_url,init)=>init.method==='POST'?(posts++,json({id:'failed_task'})):json({status:'failed'})
  try { await assert.rejects(generateToAPIs('fixture','https://toapis.com','gpt-image-2',{prompt:'fixture'}),/failed_task/); assert.equal(posts,1) } finally {globalThis.fetch=original}
})
test('unsupported models, references and incorrect base URLs fail before network', async () => {
  assert.equal(isToAPIsBase('https://toapis.com.evil.example'),false)
  await assert.rejects(generateToAPIs('fixture','https://toapis.cn','gpt-image-2-vip',{prompt:'fixture'}),/gpt-image-2 only/)
  await assert.rejects(generateToAPIs('fixture','https://toapis.cn','gpt-image-2',{prompt:'fixture',referenceImages:['https://example.com/ref.png']}),/Reference images/)
  await assert.rejects(generateToAPIs('fixture','https://toapis.cn/v1/v1','gpt-image-2',{prompt:'fixture'}),/Base URL/)
})
test('429 observation can be cancelled without duplicate generation', async () => {
  const original=globalThis.fetch; let posts=0; const controller=new AbortController()
  globalThis.fetch=async (_url,init)=>{if(init.method==='POST'){posts++;return json({id:'limited_task'})}setTimeout(()=>controller.abort(new Error('fixture cancellation')),10);return new Response('{}',{status:429,headers:{'retry-after':'8'}})}
  try {await assert.rejects(generateToAPIs('fixture','https://toapis.cn','gpt-image-2',{prompt:'fixture',signal:controller.signal}),/limited_task/);assert.equal(posts,1)}finally{globalThis.fetch=original}
})
