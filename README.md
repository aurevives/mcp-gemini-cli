# MCP Gemini CLI

MCP server that wraps Google Gemini CLI to get a second AI opinion with Gemini 2.5 Pro in Claude Code.

## Features

- Get second opinion from Gemini 2.5 Pro
- Full codebase analysis with 1M token context
- Free tier: 60 requests/minute, 1000/day
- Claude Code integration via MCP

## Installation

### Prerequisites

1. **Node.js 18+** for Gemini CLI
2. **Python 3.8+** for MCP server
3. **Gemini CLI** installed and configured

### Install Gemini CLI

```bash
npm install -g @google/gemini-cli
gemini  # Follow auth setup
```

### Install MCP

```bash
git clone https://github.com/aurevives/mcp-gemini-cli.git
cd mcp-gemini-cli
pip install -r requirements.txt
```

### Configure Claude Code

**Option 1: Direct from GitHub with uvx (Recommended)**
```bash
claude mcp add gemini-cli -- uvx --from git+https://github.com/aurevives/mcp-gemini-cli.git mcp-gemini-cli
```

**Option 2: Local installation**
```bash
claude mcp add-json gemini-cli '{
  "command": "python3",
  "args": ["/path/to/mcp-gemini-cli/server.py"],
  "env": {}
}'
```

Restart Claude Code.

## Tools

### `gemini_prompt`

Send prompt to Gemini 2.5 Pro for second opinion.

**Parameters:**
- `prompt` (string): Question or problem
- `model` (string, optional): Gemini model (default: `gemini-2.5-pro`)

### `gemini_analyze_codebase`

Analyze codebase with 1M token context.

**Parameters:**
- `question` (string): Question about the codebase
- `path` (string, optional): Directory to analyze (default: current)
- `model` (string, optional): Gemini model (default: `gemini-2.5-pro`)

### `gemini_status`

Check Gemini CLI configuration status.

## Usage Examples

### Get second opinion on technical problem
```
Use gemini_prompt: "API timeouts randomly in production but not dev. What are possible causes?"
```

### Analyze project architecture
```
Use gemini_analyze_codebase with question: "Review this codebase architecture and suggest improvements"
```

## License

MIT