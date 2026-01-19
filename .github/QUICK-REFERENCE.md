# 🎯 conda-lab AI Quick Reference

Quick commands and patterns for AI-assisted development in conda-lab.

## 🚀 Quick Commands

### Planning
```
@Plan Create a conda recipe for numpy 2.0 targeting macOS arm64
@Plan Add variants to hello-python for Python 3.9-3.12
@Plan Create a GitHub Actions workflow to build all recipes
```

### Implementation
```
@workspace Implement the plan from @Plan
@workspace Create a build.sh script for this C library
@workspace Add test section to this meta.yaml
```

### Review & Debug
```
Select files → @workspace /reviewSelection
@workspace Why is this conda-build failing? [paste error]
@workspace Compare this recipe to conda-forge conventions
```

### MCP Tools
```
@workspace List open issues in this repo using GitHub MCP
@workspace Search GitHub for similar conda recipes
@workspace What time is it in UTC?
```

## 📋 Automatic Instructions

Instructions auto-apply based on file type:

| Editing | Instructions Apply |
|---------|-------------------|
| `recipes/*/meta.yaml` | conda-build best practices |
| `recipes/*/build.sh` | macOS arm64 build patterns |
| `plugins/**/*.py` | Plugin architecture & hooks |
| `.github/**/*.yml` | CI/CD for conda packages |

No need to mention them—they're always active!

## 🎯 Agent Handoffs

After `@Plan` creates a plan:

1. **Review** the plan in chat
2. **Iterate** with feedback
3. **Click "Start Implementation"** button to hand off
4. **Or click "Open in Editor"** to refine plan first

## 💡 Pro Tips

### Get More Context
```
@workspace #file:recipes/hello-c/meta.yaml
@workspace Scan all recipes/ for variant examples
```

### Enable Thinking
Settings → `chat.agent.showThinking: true`

### Chain Operations
```
1. @Plan the feature
2. Review plan
3. @workspace implement step 1
4. Test
5. @workspace implement step 2
```

### Reference Documentation
```
@workspace According to conda-build docs, how should I...
@workspace Compare this to conda-forge guidelines
```

## 🔧 Copilot Features

### In Editor
- **Inline suggestions** - Just start typing
- **`Ctrl+I`** - Inline chat for quick edits
- **Right-click → Copilot** - Context menu actions

### In Chat
- **`@workspace`** - Full repo context
- **`#file:path`** - Reference specific file
- **`#selection`** - Reference selected code
- **`#codebase`** - Search entire codebase

### CodeLens
- **Generate Tests** - Click above functions
- **Explain** - Click above complex code
- **Fix** - Click on errors/warnings

## 📦 Recipe Development

### Start New Recipe
```
@Plan Create a conda recipe for:
- Package: scikit-learn 1.4
- Platform: macOS arm64
- Python: 3.9-3.11
- Include: comprehensive tests
```

### Debug Build
```
@workspace I'm getting this conda-build error:
[paste full error]

Current files:
#file:recipes/mypackage/meta.yaml
#file:recipes/mypackage/build.sh
```

### Add Variants
```
@workspace Add conda-build variants to this recipe for:
- Python 3.9, 3.10, 3.11, 3.12
- Show me the conda_build_config.yaml too
```

## 🔌 Plugin Development

### Create Plugin
```
@Plan Create a conda plugin that:
- Adds a subcommand: conda mycommand
- Lists installed packages with metadata
- Uses modern pyproject.toml structure
```

### Debug Loading
```
@workspace My plugin isn't loading. Here's the setup:
#file:plugins/myplugin/pyproject.toml

When I run: conda info --plugins
It doesn't appear. What's wrong?
```

### Test Entry Points
```
@workspace Create a test that verifies:
- Plugin entry points are registered
- Hook returns correct type
- Subcommand executes without errors
```

## 📚 Documentation

### Explain Concept
```
@workspace Explain conda-build variants with examples
from this repo. Keep it beginner-friendly.
```

### Create Guide
```
@workspace Create a troubleshooting guide for:
"ResolvePackageNotFound" errors on macOS arm64
Include common causes and solutions from our recipes.
```

### Compare Approaches
```
@workspace Compare:
1. noarch: python
2. Platform-specific builds
For our hello-python recipe. Pros/cons?
```

## 🔍 Code Search

### Find Examples
```
@workspace Search codebase for examples of:
- pin_subpackage usage
- compiler() jinja2 function
- test: requires section
```

### Find Patterns
```
@workspace Find all recipes that:
- Use skip: true
- Have variants defined
- Include compiled extensions
```

## 🚀 CI/CD

### Create Workflow
```
@Plan Create GitHub Actions workflow to:
- Build all recipes on PR
- Test on macOS 14 (arm64)
- Upload artifacts
- Cache conda packages
Follow github-actions.instructions.md
```

### Debug Workflow
```
@workspace This GitHub Actions run failed:
[paste error or link]

Check: #file:.github/workflows/build-recipes.yml
```

## 🎨 Customization

### Add Instructions
1. Create `prompts/my-topic.instructions.md`
2. Add YAML frontmatter:
```yaml
---
applyTo: 'path/pattern/**/*.ext'
description: Brief description
---
```
3. Write instructions in Markdown

### Create Agent
1. Create `prompts/MyAgent.agent.md`
2. Add frontmatter with `name`, `description`, `tools`
3. Write agent instructions
4. Use: `@MyAgent do something`

### MCP Servers
Edit `.vscode/mcp.json`:
```json
{
  "servers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "my-mcp-package"],
      "type": "stdio"
    }
  }
}
```

## ⚡ Keyboard Shortcuts

- **`Cmd+I`** - Open Copilot Chat
- **`Ctrl+I`** - Inline chat
- **`Cmd+Shift+I`** - Focus chat input
- **`Esc`** - Dismiss suggestions
- **`Tab`** - Accept suggestion
- **`Opt+]`** - Next suggestion

## 🐛 Troubleshooting

### Copilot Not Working?
```
1. Check: GitHub Copilot extension installed
2. Verify: Signed in to GitHub
3. Reload: Cmd+Shift+P → "Reload Window"
4. Check: .vscode/settings.json loaded
```

### MCP Servers Not Loading?
```
1. Check: .vscode/mcp.json exists
2. Verify: chat.mcp.autostart: "newAndOutdated"
3. Check: Output panel → MCP Servers
4. Try: Cmd+Shift+P → "MCP: Restart Servers"
```

### Instructions Not Applying?
```
1. Verify: File matches applyTo pattern
2. Check: YAML frontmatter valid
3. Test: Ask Copilot about the instructions
4. Example: "What instructions apply to this file?"
```

## 📖 Learn More

- **[AI Setup Guide](.github/AI-SETUP.md)** - Complete documentation
- **[Enhancement Summary](.github/ENHANCEMENT-SUMMARY.md)** - What's included
- **[Workspace Settings](.github/WORKSPACE-SETTINGS.md)** - Settings architecture

## 💬 Example Conversations

### Recipe Review
```
User: @workspace /reviewSelection
[Copilot reviews meta.yaml against conda-build.instructions]

User: Add the missing test section
[Copilot adds imports test]

User: Should this be noarch?
[Copilot explains based on compiled code check]
```

### Debug Session
```
User: @workspace Build failing with undefined symbol
#file:recipes/hello-c/build.sh

[Copilot analyzes, suggests LDFLAGS fix]

User: Implement the fix
[Copilot updates build.sh with proper flags]

User: Test it
[Copilot suggests: conda build recipes/hello-c/]
```

### Planning Workflow
```
User: @Plan Add pytest recipe with variants

[Plan agent researches, drafts plan]

User: Also include pytest-cov plugin
[Plan agent updates plan]

User: [Click "Start Implementation"]
[Main agent implements the plan]
```

---

**Remember:** The AI knows conda, conda-build, macOS arm64, and your repo structure. Just ask!
