import fs from 'node:fs'
import path from 'node:path'
import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js'

// Load credentials in memory only. This script never prints or copies the key.
const [credentialFile, outputDir, mode = 'list'] = process.argv.slice(2)
if (!['list','live'].includes(mode)) throw new Error('Mode must be list or live');
if (!credentialFile || !outputDir) throw new Error('Usage: node toapis-smoke.mjs <private-env-file> <output-directory> [list|live]')
const secrets = {}
for (const line of fs.readFileSync(credentialFile, 'utf8').split(/\r?\n/)) {
  const match = line.trim().match(/^(?:export\s+)?([A-Z_][A-Z0-9_]*)\s*=\s*(.*)$/)
  if (match) secrets[match[1]] = match[2].replace(/^(['"])(.*)\1$/, '$2').trim()
}
const key = secrets.TOAPIS_API_KEY
if (!key) throw new Error('TOAPIS_API_KEY missing in private credential file')
const base = secrets.TOAPIS_BASE_URL || 'https://toapis.cn'
fs.mkdirSync(outputDir, { recursive: true })
const env = Object.fromEntries(Object.entries(process.env).filter(([,value]) => value !== undefined))
Object.assign(env, { OPENAI_API_KEY: key, OPENAI_BASE_URL: base, OPENAI_MODEL: 'gpt-image-2', MEIGEN_OUTPUT_DIR: path.resolve(outputDir), TOAPIS_ENV_FILE:credentialFile })
const client = new Client({ name: 'toapis-integration-verification', version: '1.0.0' })
const transport = new StdioClientTransport({ command: process.execPath, args: [path.resolve(process.env.TOAPIS_TEST_WRAPPER ? 'start-toapis.mjs' : 'dist/index.js')], env, stderr: 'pipe' })
const trace = []
transport.stderr?.on('data', chunk => {
  for (const line of String(chunk).split(/\r?\n/)) {
    if (line.startsWith('TOAPIS_TASK ')) {
      try { const event = JSON.parse(line.slice(12)); trace.push(event); fs.writeFileSync(path.join(outputDir, 'task-trace.json'), JSON.stringify(trace, null, 2)); console.log(JSON.stringify({event:event.status, taskId:event.taskId})) } catch {}
    }
  }
})
const args = { provider:'openai', model:'gpt-image-2', prompt:'Create an elegant ecommerce product poster for an unbranded matte orange insulated tumbler. Centered hero product on a black stone podium, warm orange rim light, deep charcoal studio background, controlled condensation, premium commercial photography, generous negative space in the upper third for a headline added later. No text, no logos, no watermarks.', aspectRatio:'3:4', resolution:'1K', wait:true, download:true }
const started = new Date().toISOString()
try {
  await client.connect(transport)
  const tools = await client.listTools()
  if (!tools.tools.some(tool => tool.name === 'generate_image')) throw new Error('generate_image not exposed by MCP')
  console.log(JSON.stringify({ mcpConnected:true, tools:tools.tools.map(tool => tool.name), mode }))
  if (mode === 'list') process.exitCode = 0
  else {
    const result = await client.callTool({ name:'generate_image', arguments:args }, undefined, { timeout:720000 })
    const body = result.structuredContent || JSON.parse(result.content.find(item => item.type === 'text').text)
    const record = { upstream:'jau123/MeiGen-AI-Design-MCP', upstreamSha:'33ecb583c541652574c5875963d1225fa4ecf751', test:'real MCP generate_image -> patched upstream OpenAIProvider -> ToAPIs async -> local image', started, completed:new Date().toISOString(), request:args, result:body, elapsedSeconds:(Date.now()-Date.parse(started))/1000, actualCharge:null, chargeNote:'Task fields are not a verified account Usage Log. See task-trace.json; do not label listed price as actual charge.' }
    fs.writeFileSync(path.join(outputDir,'real-mcp-test.json'),JSON.stringify(record,null,2))
    console.log(JSON.stringify({ success:body.success, status:body.status, savedPath:body.savedPath, elapsedSeconds:record.elapsedSeconds }))
    if (!body.success || !body.savedPath) process.exitCode = 1
  }
} finally { await client.close() }
