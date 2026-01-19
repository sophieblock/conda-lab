# Comparison: austenstone/.vscode vs conda-lab AI Setup

This document compares the AI configuration from austenstone/.vscode with conda-lab's implementation.

## Key Improvements Adopted

### 1. Advanced Copilot Settings

**From austenstone/.vscode:**
```json
"github.copilot.chat.agent.thinkingTool": true,
"github.copilot.chat.codesearch.enabled": true,
"github.copilot.chat.edits.temporalContext.enabled": true,
"github.copilot.chat.anthropic.thinking.enabled": true
```

**Benefit:** Enhanced reasoning, search capabilities, and context awareness.

### 2. MCP Server Integration

**From austenstone/.vscode:**
- GitHub MCP servers (actions, context, security, etc.)
- Sequential thinking server
- Time server for timezone operations

**Adapted for conda-lab:**
- Focused on GitHub and time servers
- Streamlined for conda-specific workflows
- Removed unused servers (firecrawl, chrome-devtools, etc.)

### 3. Custom Agents Pattern

**From austenstone/.vscode:**
- Plan.agent.md structure with YAML frontmatter
- Handoffs between agents
- Tool restrictions
- Stopping rules

**Implemented in conda-lab:**
- Plan agent customized for conda tasks
- Handoffs to implementation agent
- Conda-specific research patterns

### 4. Instruction Files

**From austenstone/.vscode:**
- `applyTo` YAML frontmatter for automatic application
- Multiple instruction files for different contexts
- GitHub Actions best practices

**Implemented in conda-lab:**
- conda-build.instructions.md for recipes
- conda-plugin.instructions.md for plugins
- github-actions.instructions.md adapted for conda CI

### 5. Chat Tool Settings

**From austenstone/.vscode:**
```json
"chat.tools.autoApprove": true,
"chat.todoListTool.enabled": true,
"chat.mcp.autostart": "newAndOutdated",
"chat.customAgentInSubagent.enabled": true
```

**Benefit:** Smoother workflows with less friction.

## Differences & Customizations

### What We Kept

✅ Core Copilot chat features  
✅ MCP discovery settings  
✅ Agent architecture with handoffs  
✅ GitHub Actions patterns  
✅ Tool auto-approval settings  

### What We Adapted

🔧 **MCP Servers**: Minimal set focused on GitHub + utilities  
🔧 **Plan Agent**: Conda-specific research and planning logic  
🔧 **Instructions**: Domain-specific for conda packaging  
🔧 **Language Settings**: Python, YAML, Markdown optimized for conda  

### What We Skipped

❌ Azure-specific settings (not applicable)  
❌ Chrome DevTools MCP (not needed)  
❌ Firecrawl MCP (not needed)  
❌ Playwright MCP (not needed)  
❌ Context7 MCP (not applicable)  
❌ Advanced inline edits config (experimental features)  

## Custom Additions for conda-lab

### 1. Conda-Specific cSpell Words

```json
"cSpell.userWords": [
  "conda", "condabuild", "condaforge",
  "mamba", "micromamba", "noarch",
  "pyproject", "setuptools"
]
```

### 2. Python Environment Settings

```json
"python.terminal.useEnvFile": true,
"[python]": {
  "editor.defaultFormatter": "ms-python.black-formatter"
}
```

### 3. YAML Formatting for Recipes

```json
"[yaml]": {
  "editor.defaultFormatter": "redhat.vscode-yaml",
  "editor.tabSize": 2
}
```

### 4. Plan Agent: Conda Context

- Searches `recipes/`, `plugins/`, `docs/` directories
- Considers macOS arm64 platform specifics
- References conda-build conventions
- Includes variant matrix considerations

### 5. Instruction Files: Conda Patterns

**conda-build.instructions.md:**
- Recipe structure for macOS arm64
- Dependency specification patterns
- Build script best practices
- Testing strategies

**conda-plugin.instructions.md:**
- Entry point configuration
- Hook implementations
- Plugin discovery debugging

## Usage Comparison

### austenstone/.vscode Style

```
@Plan Create a TypeScript server
→ Plans with general best practices
→ Hands off to implementation
```

### conda-lab Style

```
@Plan Create a recipe for numpy 2.0
→ Searches existing recipes
→ Considers macOS arm64 requirements
→ Includes variant matrix suggestions
→ References conda-build docs
→ Hands off with conda-specific context
```

## Architecture Patterns Learned

### 1. Agent Frontmatter Structure

```yaml
---
name: AgentName
description: Brief description
argument-hint: Usage hint
tools: ['tool1', 'tool2']
handoffs:
  - label: Button Text
    agent: target
    prompt: Context for target
---
```

### 2. Stopping Rules Pattern

```xml
<stopping_rules>
STOP IMMEDIATELY if [condition].
If you catch yourself [action], STOP.
NEVER [forbidden action].
</stopping_rules>
```

### 3. Workflow Pattern

```xml
<workflow>
## 1. Phase Name:
Instructions and tool calls

## 2. Next Phase:
Output requirements

## 3. Feedback Handling:
Iteration logic
</workflow>
```

### 4. Style Guide Pattern

```xml
<output_style_guide>
Template with {placeholders}
Word counts and constraints
IMPORTANT: Override rules
</output_style_guide>
```

### 5. Instruction File Pattern

```yaml
---
applyTo: 'glob/pattern/**/*.ext'
description: Context description
---
Instructions in Markdown
```

## Performance Optimizations

**From austenstone/.vscode:**
- Auto-accept delay: 5 seconds
- Max requests: 100
- MCP autostart: newAndOutdated
- Global tool auto-approve

**Impact:** Faster iterations, less manual confirmation.

## Security Considerations

**From austenstone/.vscode GitHub Actions instructions:**
- Principle of least privilege
- Pin actions to commit SHA
- OIDC for authentication
- No hardcoded credentials

**Applied in conda-lab:**
- `permissions: contents: read` in workflows
- Explicit permission grants per job
- Secure handling of conda channel tokens

## Next Steps for Enhancement

Based on austenstone's config, we could add:

1. **More MCP Servers**: 
   - Data store for recipe database
   - Sequential thinking for complex debugging

2. **Additional Agents**:
   - Research agent for conda-forge exploration
   - Review agent for recipe validation

3. **Toolset Constraints**:
   - Create `.toolsets.jsonc` for specific agents
   - Limit tool access for focused workflows

4. **Commit Message Instructions**:
   - `.copilot-commit-message-instructions.md`
   - Conventional commits for conda-lab

## Conclusion

The austenstone/.vscode repository provided excellent patterns for:
- Agent architecture with clear separation of concerns
- MCP integration for extended capabilities
- Instruction files that apply automatically
- Best practices for GitHub Actions

We successfully adapted these patterns for conda-lab's domain-specific needs while maintaining the core architectural principles.
