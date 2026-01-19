# VS Code Settings Architecture in conda-lab

This document explains how settings work in the conda-lab multi-root workspace.

## Settings Hierarchy

VS Code applies settings in this order (higher numbers win):

1. **Default settings** (VS Code built-ins)
2. **User settings** (`~/Library/Application Support/Code/User/settings.json`)
3. **Workspace settings** (from `conda-lab.code-workspace`)
4. **Folder settings** (from `conda-lab/.vscode/settings.json`)

## Current Setup

### Multi-Root Workspace File

Location: `workspace/conda-lab.code-workspace`

```json
{
  "folders": [
    {
      "path": ".."
    }
  ],
  "settings": {
    // Workspace-level settings would go here
    // Currently empty
  }
}
```

### Folder Settings

Location: `.vscode/settings.json`

Contains all our Copilot, Python, YAML, and other configurations.

## How It Works

### When Opening the Workspace

1. You open `conda-lab.code-workspace`
2. VS Code loads the folder `.vscode/settings.json`
3. Settings from `.vscode/settings.json` apply to that folder
4. Settings in `conda-lab.code-workspace` would override folder settings (but we have none defined there)

### Settings Precedence

```
conda-lab.code-workspace (workspace settings)
         ↓ overrides
.vscode/settings.json (folder settings)
         ↓ overrides
User settings
         ↓ overrides
Default settings
```

## Your Original Question

> "When activating the multi-root workspace `conda-lab.code-workspace`, 
> will settings from the mono-workspace 'conda-lab' be inherited?"

**Answer:** 

The `.vscode/settings.json` file in the `conda-lab` folder **is not "inherited"** from a previous workspace—it's applied because that folder is part of the multi-root workspace.

- ✅ `.vscode/settings.json` **will apply** to files in the conda-lab folder
- ✅ Settings work the same whether you open the folder directly or via the workspace file
- ❌ Nothing is "inherited" from prior sessions; it's just folder settings

### What Changes Between Direct Folder vs Workspace File

**Opening folder directly:**
```
~/dev/conda-lab → Uses .vscode/settings.json
```

**Opening workspace file:**
```
conda-lab.code-workspace → Loads conda-lab folder → Uses .vscode/settings.json
```

Same settings apply in both cases! The workspace file just adds the ability to:
- Include multiple folders
- Define workspace-level settings that override folder settings
- Manage workspace-specific tasks, extensions, etc.

## Design Decision: Where to Put Settings

### Current: Folder Settings (`.vscode/settings.json`)

**Pros:**
- ✅ Works whether opened as folder or workspace
- ✅ Version controlled with the repo
- ✅ Shared with all contributors
- ✅ No duplication needed

**Cons:**
- ❌ Can't have different settings per workspace if you reuse the folder

### Alternative: Workspace Settings (`conda-lab.code-workspace`)

**Pros:**
- ✅ Can override folder settings for specific workspace
- ✅ Personal workspace configs don't need to be committed

**Cons:**
- ❌ Only apply when opening via workspace file
- ❌ Workspace file might not be committed (personal configs)
- ❌ Duplication if multiple workspaces use same folder

### Our Recommendation: Hybrid Approach

**In `.vscode/settings.json` (committed):**
- Copilot configurations (shared by all)
- Language-specific settings (Python, YAML)
- Shared development tools (formatters, linters)
- Project-specific settings (conda-related)

**In `conda-lab.code-workspace` (optional, personal):**
- Personal overrides
- Local environment paths
- Experimental settings
- Multi-root specific configurations

## Tasks and Launch Configurations

### Tasks (`.vscode/tasks.json`)

- Defined at folder level
- Accessible when folder is part of workspace
- Can also be defined in workspace file
- Workspace tasks override folder tasks with same label

### Launch Configurations (`.vscode/launch.json`)

- Work the same as tasks
- Folder-level configs available in workspace
- Can be supplemented in workspace file

## MCP Configuration

Location: `.vscode/mcp.json`

- MCP servers are folder-specific
- Loaded when folder is opened (directly or via workspace)
- Not affected by workspace file
- Same servers available regardless of how folder is opened

## Extensions

### Recommended Extensions

Could be defined in:
- `.vscode/extensions.json` (folder-level, committed)
- `conda-lab.code-workspace` (workspace-level, personal)

Currently: Not defined. Consider adding:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.black-formatter",
    "redhat.vscode-yaml",
    "github.copilot",
    "github.copilot-chat"
  ]
}
```

## Testing Settings Precedence

### Verify Folder Settings Apply

1. Open `conda-lab.code-workspace`
2. Open a Python file
3. Check: `Cmd+,` → Search "python.terminal.useEnvFile"
4. Should show "true" from `.vscode/settings.json`

### Add Workspace Override (optional)

Edit `conda-lab.code-workspace`:

```json
{
  "folders": [{"path": ".."}],
  "settings": {
    "editor.tabSize": 4  // Override folder setting of 2
  }
}
```

Result: Tab size becomes 4 (workspace wins over folder).

## Multi-Root Expansion Example

If you later add multiple folders:

```json
{
  "folders": [
    {"path": "..", "name": "conda-lab"},
    {"path": "../../other-project", "name": "other"}
  ],
  "settings": {
    // These apply to ALL folders
    "editor.tabSize": 2
  }
}
```

Each folder's `.vscode/settings.json` still applies to that folder, but workspace settings override both.

## Summary

**For conda-lab, the answer is:**

1. Your `.vscode/settings.json` applies whether you open the folder directly or via the workspace file
2. Nothing is "inherited"—the settings are always there because they're in the folder
3. The workspace file can **add** or **override** folder settings but doesn't by default
4. All our AI enhancements (Copilot settings, MCP servers, instructions) work the same way regardless

**Best practice:** Keep shared settings in `.vscode/settings.json` (committed), use workspace file for personal overrides or multi-root specific configs.
