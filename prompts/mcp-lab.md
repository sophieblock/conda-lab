# MCP (Model Context Protocol) Lab Prompts

Prompts and patterns for working with MCP tools and context in conda-lab.

## Overview

MCP enables AI assistants to interact with tools and data sources in a standardized way.
These prompts leverage MCP for conda development tasks.

## File System Operations

### Explore Recipe Structure

```
Use the filesystem MCP to:
1. List all recipe directories in recipes/
2. Read meta.yaml from each recipe
3. Summarize the differences between them
```

### Search for Patterns

```
Search the codebase using MCP for:
- All uses of "# [osx]" selectors
- All entry_points configurations
- All references to CONDA_PREFIX
```

### Read and Compare

```
Read these files via MCP and compare:
- recipes/hello-c/build.sh
- recipes/hello-python/build.sh
Highlight the key differences between C and Python builds.
```

## Command Execution

### Build and Test

```
Using the command execution MCP:
1. conda render recipes/hello-python/
2. Capture the output
3. Explain what the rendered recipe shows
```

### Environment Validation

```
Execute via MCP:
1. conda env create -f envs/dev.yml --dry-run
2. Parse the output to list all packages
3. Check for any conflicts or warnings
```

### Plugin Discovery

```
Run via MCP:
1. pip install -e plugins/rebuilt-conda-graph/
2. conda info --plugins
3. Verify the plugin is registered correctly
```

## Documentation Tasks

### Generate TOC

```
Read all markdown files in docs/ via MCP and generate:
1. A table of contents with links
2. A brief summary of each document
3. Suggested reading order for newcomers
```

### Check Links

```
Parse all .md files via MCP and:
1. Extract all markdown links
2. Verify internal links point to existing files
3. Report broken links
```

### Update Index

```
Generate a docs/README.md that:
1. Lists all documentation files
2. Includes one-line summaries
3. Organizes by topic (conda-build, plugins, etc.)
```

## Code Analysis

### Analyze Plugin Structure

```
Use MCP to read all Python files in plugins/rebuilt-conda-graph/ and:
1. Map out the class hierarchy
2. List all hook implementations
3. Identify entry points
```

### Extract Metadata

```
Parse all meta.yaml files via MCP and extract:
- Package names and versions
- All build requirements
- All test commands
Create a summary table.
```

### Find Dependencies

```
Scan all setup.py and pyproject.toml files and:
1. List all conda dependencies
2. List all pip dependencies
3. Check for version conflicts
```

## Testing and Validation

### Validate Recipes

```
For each recipe in recipes/, use MCP to:
1. Check if meta.yaml is valid YAML
2. Verify build.sh exists and is executable
3. Check for required fields (name, version, about)
```

### Check Consistency

```
Verify consistency across the repo via MCP:
1. All Python code uses consistent formatting
2. All recipes follow the same structure
3. All docs use the same markdown style
```

### Lint Configuration

```
Read and validate configuration files:
1. Check pyproject.toml syntax
2. Verify entry points are properly formatted
3. Ensure conda environment files are valid YAML
```

## Workspace Operations

### Update Workspace Config

```
Modify workspace/conda-lab.code-workspace via MCP to:
1. Add a new folder for experiments
2. Update Python interpreter path
3. Add recommended extensions
```

### Generate Workspace Report

```
Analyze the workspace configuration and:
1. List all configured folders
2. Show all settings
3. List recommended extensions
4. Suggest improvements
```

## Git Integration

### Analyze Changes

```
Use git via MCP to:
1. Show files changed since last commit
2. Summarize changes in each recipe
3. Check if docs need updating
```

### Generate Changelog

```
From git history via MCP:
1. List all commits since last release
2. Group by component (recipes, plugins, docs)
3. Generate a changelog entry
```

## Advanced Workflows

### Recipe Development Pipeline

```
Orchestrate via MCP:
1. Create new recipe directory
2. Generate meta.yaml template
3. Create build.sh skeleton
4. Run conda render to validate
5. Report any issues
```

### Plugin Testing Pipeline

```
Automate plugin testing:
1. Install plugin in editable mode
2. Run conda info --plugins
3. Execute plugin command
4. Capture and validate output
5. Uninstall plugin
```

### Documentation Update

```
Update docs based on code changes:
1. Detect new Python files in plugins/
2. Extract docstrings
3. Generate API documentation
4. Add to docs/plugins/
```

## Context Management

### Load Context

```
Before answering questions, use MCP to load:
1. Current working environment (conda list)
2. Recent git changes
3. Relevant documentation files
4. Example recipe code
```

### Maintain State

```
Track state across interactions:
1. Store last built recipe
2. Remember environment settings
3. Track which docs were referenced
4. Note unresolved issues
```

## Error Handling

### Debug Build Failure

```
When a build fails, use MCP to:
1. Capture full error output
2. Read the meta.yaml
3. Check build.sh for issues
4. Inspect environment variables
5. Suggest specific fixes
```

### Troubleshoot Plugin

```
Debug plugin loading issues:
1. Read plugin code via MCP
2. Check entry point configuration
3. Verify imports are available
4. Test plugin registration
5. Provide diagnostic report
```

## Reporting

### Generate Summary

```
Create a repository summary via MCP:
1. Count recipes, plugins, docs
2. List all entry points
3. Show environment configurations
4. Highlight recent changes
5. Suggest next steps
```

### Health Check

```
Run a health check via MCP:
1. Validate all YAML files
2. Check Python syntax
3. Verify all docs exist
4. Test basic conda commands
5. Report status
```

## Best Practices

### Efficient Context Loading

```
Load minimal necessary context:
- Don't read entire files if summary suffices
- Use targeted searches instead of full scans
- Cache frequently accessed data
```

### Incremental Updates

```
Make changes incrementally:
1. Read current state
2. Make small modification
3. Validate change
4. Repeat
```

### Error Recovery

```
Handle failures gracefully:
1. Catch MCP tool errors
2. Provide helpful error messages
3. Suggest alternative approaches
4. Continue with available data
```

## Example MCP Session

```
# 1. Explore
"List all recipes using MCP"

# 2. Select
"Read the meta.yaml for hello-python"

# 3. Analyze
"Parse this meta.yaml and explain each section"

# 4. Modify
"Add a new dependency to requirements.run"

# 5. Validate
"Render the modified recipe to check for errors"

# 6. Document
"Update the recipe README based on changes"
```

## See Also

- `prompts/copilot-lab.md` - GitHub Copilot prompts
- `docs/` - Technical documentation
- [MCP Specification](https://spec.modelcontextprotocol.io/)
