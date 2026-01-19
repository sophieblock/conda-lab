# GitHub Copilot Lab Prompts

Useful prompts and patterns for working with GitHub Copilot in conda-lab.

## Recipe Development Prompts

### Generate Recipe Template

```
Create a conda recipe meta.yaml for a Python package named "mypackage" 
version 1.0.0 that depends on numpy and pandas. Include test section.
Target macOS arm64.
```

### Debug Build Script

```
I have a conda build.sh script that's failing with error: [paste error]
The build environment is macOS arm64 with clang. 
Here's my current script: [paste script]
What's wrong and how do I fix it?
```

### Add Variants

```
Add conda-build variants to this meta.yaml to build for 
Python 3.9, 3.10, and 3.11. Show the conda_build_config.yaml too.
```

## Plugin Development Prompts

### Create Plugin Skeleton

```
Create a conda plugin using pyproject.toml that adds a custom subcommand
called "analyze". Use modern src/ layout and proper entry points.
```

### Implement Hook

```
Implement a conda_solvers() hook that registers a custom solver.
The solver should [describe behavior]. Use the conda plugins API.
```

### Debug Plugin Loading

```
My conda plugin isn't being discovered. Here's my pyproject.toml:
[paste config]
What could be wrong with the entry point configuration?
```

## Documentation Prompts

### Explain Concept

```
Explain conda-build variants like I'm new to conda. 
Use examples from macOS arm64. Include code samples.
```

### Compare Approaches

```
Compare noarch: python vs platform-specific builds for conda packages.
When should I use each? Include pros/cons.
```

### Troubleshooting Guide

```
Create a troubleshooting guide for "ResolvePackageNotFound" errors
on macOS arm64. Include common causes and solutions.
```

## Environment Prompts

### Create Environment File

```
Create a conda environment.yml for developing Python packages on macOS arm64.
Include conda-build, pytest, black, and common dev tools.
```

### Debug Environment Issue

```
My conda environment has conflicting dependencies:
[paste error]
How do I resolve this? Suggest changes to environment.yml.
```

## Code Review Prompts

### Review Recipe

```
Review this conda recipe for best practices:
[paste meta.yaml]
Focus on: dependencies, tests, and macOS arm64 compatibility.
```

### Review Plugin

```
Review this conda plugin implementation:
[paste code]
Check for: proper hook usage, error handling, and API compliance.
```

## Learning Prompts

### Understand Error

```
I got this error building a conda package:
[paste error]
Explain what it means in simple terms and how to fix it.
```

### Learn Pattern

```
Show me examples of using selectors in conda meta.yaml
for platform-specific (macOS, Linux, Windows) dependencies.
```

## Quick Reference Prompts

### Generate Command

```
Give me the conda-build command to:
- Build only Python 3.11 variant
- Skip tests
- Output to custom directory
```

### Find Documentation

```
Where in the conda-build docs can I find information about:
- Build environment variables
- Test section options
- Variant configuration
```

## Tips for Better Results

1. **Be Specific**: Include error messages, file contents, platform details
2. **Provide Context**: Mention macOS arm64, Miniforge, specific tools
3. **Ask for Examples**: Request code samples, not just explanations
4. **Iterate**: Follow up with refinements and edge cases
5. **Request Testing**: Ask for test cases or validation steps

## Example Workflow

```
# 1. Start broad
"I need to create a conda recipe for a C library"

# 2. Get specific
"Add compiler dependencies for macOS arm64"

# 3. Debug issues
"The build fails with undefined symbols. Here's the error: [paste]"

# 4. Add tests
"Add a test section that verifies the compiled library loads"

# 5. Document
"Write a README explaining how to build this recipe"
```

## Common Patterns

### Recipe Metadata

```
Set up package metadata in meta.yaml:
- Name: {{ name }}
- Version from variable
- Source from git tag
- MIT license
```

### Build Configuration

```
Configure build section for:
- Skip on non-macOS platforms
- Custom build string
- Entry points for CLI tool
```

### Testing

```
Add comprehensive tests:
- Import test for Python modules
- Command existence tests
- Version output validation
```

## Copilot Workspace Tips

When using Copilot in the multi-root workspace:

1. **Switch Context**: Select the right folder (recipes/, plugins/, docs/)
2. **Use Relative Paths**: Copilot understands workspace structure
3. **Reference Files**: "Based on recipes/hello-python/meta.yaml..."
4. **Compare**: "Compare this approach to rebuilt-conda-graph plugin"

## See Also

- `prompts/mcp-lab.md` - MCP-specific prompts
- `docs/` - Reference documentation
- `recipes/` - Example recipes for context
