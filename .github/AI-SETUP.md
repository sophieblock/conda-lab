# AI Setup for conda-lab

This document explains the enhanced AI configuration in this repository.

## 🤖 Overview

The conda-lab repository is configured with custom GitHub Copilot instructions, MCP servers, and AI agents to optimize development workflows for conda packaging, plugin development, and documentation.

## 📁 Directory Structure

```
.vscode/
├── settings.json          # VS Code & Copilot settings
├── mcp.json              # MCP server configurations
└── tasks.json            # Build tasks

prompts/
├── Plan.agent.md         # Planning agent for conda tasks
├── conda-build.instructions.md    # Recipe best practices
├── conda-plugin.instructions.md   # Plugin development guide
├── github-actions.instructions.md # CI/CD patterns
├── copilot-lab.md        # Prompt templates
└── mcp-lab.md            # MCP usage examples

.github/workflows/
└── build-recipes.yml     # Conda package CI
```

## ⚙️ VS Code Settings

### Key Copilot Features Enabled

The `.vscode/settings.json` includes:

- **Thinking Tool**: `github.copilot.chat.agent.thinkingTool: true`
- **Code Search**: `github.copilot.chat.codesearch.enabled: true`
- **Temporal Context**: Tracks recent edits for better suggestions
- **Test Generation**: CodeLens for generating tests
- **Review Selection**: AI code reviews on selected code
- **Rename Suggestions**: Smart variable/function renaming

### Chat & Tool Settings

- **Auto-approve tools**: `chat.tools.autoApprove: true`
- **Todo tracking**: `chat.todoListTool.enabled: true`
- **MCP auto-start**: `chat.mcp.autostart: "newAndOutdated"`
- **Custom agents**: `chat.customAgentInSubagent.enabled: true`

### Language-Specific Settings

- **Python**: Black formatter, organize imports on save
- **YAML**: 2-space indent for conda recipe files
- **Markdown**: Prettier formatter, word wrap enabled

## 🔌 MCP Server Configuration

The `.vscode/mcp.json` configures Model Context Protocol servers:

### GitHub Integration

- **github-mcp-server**: Default GitHub operations + org management
- **github-actions**: CI/CD workflow interactions
- **github-context**: Repository context awareness

### Utilities

- **time**: Timezone-aware time operations
- **sequential-thinking**: Step-by-step reasoning for complex tasks

### Adding Custom MCP Servers

Edit `.vscode/mcp.json` to add servers:

```json
{
  "servers": {
    "your-server": {
      "command": "npx",
      "args": ["-y", "your-mcp-package"],
      "type": "stdio"
    }
  }
}
```

## 🎯 Custom Agents

### Plan Agent (`prompts/Plan.agent.md`)

Specialized planning agent for conda tasks.

**Usage:**
```
@Plan Create a recipe for numpy 2.0 targeting macOS arm64
```

**Capabilities:**
- Researches existing recipes and patterns
- Generates step-by-step implementation plans
- Considers conda-specific requirements
- References project documentation

**Handoffs:**
- **Start Implementation**: Hands off to default agent with plan
- **Open in Editor**: Creates untitled file with plan for editing

### How to Invoke

In GitHub Copilot Chat:
- `@Plan [describe your task]` - Creates a plan
- Click handoff buttons to proceed with implementation

## 📚 Instruction Files

Instruction files apply automatically based on file type:

### conda-build.instructions.md

Applies to: `recipes/**/meta.yaml`, `build.sh`, `conda_build_config.yaml`

**Best practices for:**
- Recipe structure and metadata
- Dependency specification
- macOS arm64 builds
- Variants and testing

### conda-plugin.instructions.md

Applies to: `plugins/**/pyproject.toml`, `plugins/**/*.py`

**Covers:**
- Plugin architecture
- Entry point configuration
- Hook implementations
- Testing strategies

### github-actions.instructions.md

Applies to: `.github/**/*.yml`, `.github/**/*.yaml`

**Guidelines for:**
- Conda-specific CI workflows
- Platform matrices
- Caching strategies
- Security best practices

## 🚀 Usage Examples

### Generate a Recipe

```
@workspace Create a conda recipe for scikit-learn 1.4 that:
- Targets macOS arm64
- Supports Python 3.9-3.11
- Includes comprehensive tests
Use the Plan agent first.
```

### Debug Build Issues

```
@workspace I'm getting this error building hello-c:
[paste error]
Check the build.sh and meta.yaml in recipes/hello-c/
```

### Review Recipe

```
Select recipe files, then:
@workspace /reviewSelection Check this recipe against conda-forge best practices
```

### Create GitHub Workflow

```
@workspace Create a GitHub Actions workflow to:
- Build all recipes on PR
- Test on macOS arm64
- Upload artifacts
Follow our github-actions instructions.
```

## 🔍 MCP Tools Usage

### GitHub Operations

```
@workspace List all open issues in this repo using MCP tools
@workspace Create a draft PR for this feature branch
```

### Time-based Operations

```
@workspace What time is it in NYC? (uses time MCP server)
```

### Sequential Thinking

```
@workspace Use sequential-thinking to analyze:
Why does variants-demo build 3 outputs?
```

## 🎨 Customization

### Adding Custom Instructions

1. Create a new `.instructions.md` file in `prompts/`
2. Add YAML frontmatter with `applyTo` patterns:
   ```yaml
   ---
   applyTo: 'docs/**/*.md'
   description: Documentation writing guidelines
   ---
   ```
3. Write your instructions in Markdown

### Creating Custom Agents

1. Create a `.agent.md` file in `prompts/`
2. Add YAML frontmatter with required fields:
   ```yaml
   ---
   name: YourAgent
   description: Brief description
   argument-hint: Usage hint
   tools: ['tool1', 'tool2']
   ---
   ```
3. Write agent instructions following the pattern in Plan.agent.md

### Configuring Toolsets

Create `.toolsets.jsonc` files to constrain tool access for specific agents:

```jsonc
{
  "allowed": ["mcp_server_name/*"],
  "denied": []
}
```

## 📖 Additional Resources

### Copilot Documentation
- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [Custom Instructions](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)

### MCP Resources
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Servers List](https://github.com/punkpeye/awesome-mcp-servers)

### Conda Packaging
- [conda-build docs](https://docs.conda.io/projects/conda-build/)
- [conda-forge guidelines](https://conda-forge.org/docs/maintainer/guidelines.html)

## 🤝 Contributing

When adding AI configurations:

1. Test instructions with actual Copilot interactions
2. Document usage examples
3. Keep instructions concise and actionable
4. Consider conda-specific edge cases
5. Update this README with new features

## 💡 Tips

- Use `@workspace` to give Copilot full repo context
- Use `#file:path` to reference specific files
- Combine agents: `@Plan` then `@workspace implement this`
- Enable "Show Thinking" in settings to see reasoning
- Review and iterate on generated plans before implementation
- Use MCP tools explicitly: `use #mcp tool to...`
