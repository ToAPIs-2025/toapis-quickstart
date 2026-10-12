// Start the patched upstream MCP server with the user's own private ToAPIs key.
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { spawn } from 'node:child_process'
const root = path.dirname(fileURLToPath(import.meta.url))
const file = process.env.TOAPIS_ENV_FILE
if (!file) throw new Error('Set TOAPIS_ENV_FILE to your private .env file path. Never put the key in this repository.')
const values = {}
for (const line of fs.readFileSync(file,'utf8').split(/\r?\n/)) {
  const match = line.trim().match(/^(?:export\s+)?([A-Z_][A-Z0-9_]*)\s*=\s*(.*)$/)
  if (match) values[match[1]] = match[2].replace(/^(['"])(.*)\1$/,'$2').trim()
}
if (!values.TOAPIS_API_KEY) throw new Error('TOAPIS_API_KEY missing in private environment file')
const env = { ...process.env, OPENAI_API_KEY:values.TOAPIS_API_KEY, OPENAI_BASE_URL:values.TOAPIS_BASE_URL || 'https://toapis.cn', OPENAI_MODEL:'gpt-image-2', MEIGEN_OUTPUT_DIR:process.env.MEIGEN_OUTPUT_DIR || path.join(root,'generated') }
const child = spawn(process.execPath,[path.join(root,'dist/index.js')],{cwd:root,env,stdio:'inherit'})
child.on('error',()=>{ console.error('MCP process failed to start.'); process.exitCode=1 })
child.on('exit',code=>{process.exitCode=code ?? 1})
for (const signal of ['SIGINT','SIGTERM']) process.on(signal,()=>child.kill(signal))
