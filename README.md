# conda-lab

A lightweight conda experimentation lab for understanding conda-build recipes, variants, and plugins. Focused on reproducible environments, macOS/arm64 behavior, plugin boundaries, and documentation-driven learning—without forking core conda or conda-build repositories.

## 🎯 Purpose

This repository is a **learning sandbox** for:

- 📦 **Experimenting with conda-build recipes** (C, Python, variants)
- 🔌 **Developing and testing conda plugins** (solvers, subcommands, hooks)
- 📚 **Understanding conda internals** through documentation and examples
- 🔬 **Testing reproducibility strategies** (lock files, explicit specs)
- 🍎 **macOS arm64 specifics** (Miniforge, Apple Silicon, native builds)

## 📁 Repository Structure

```
conda-lab/
├── README.md                    # You are here
├── workspace/
│   └── conda-lab.code-workspace # VS Code multi-root workspace
├── envs/
│   ├── dev.yml                  # Development environment
│   └── build.yml                # Build environment with compilers
├── recipes/
│   ├── hello-c/                 # Simple C program with compilers
│   ├── hello-python/            # Python package (noarch)
│   └── variants-demo/           # Demonstrates build variants
├── plugins/
│   ├── rebuilt-conda-graph/     # Example plugin (modern structure)
│   └── scratch/                 # Experimental plugin code
├── docs/
│   ├── conda-build/
│   │   ├── macos-env-vars.md
│   │   ├── render-vs-build-vs-test.md
│   │   └── variants.md
│   ├── plugins/
│   │   ├── plugin-architecture.md
│   │   └── entry-points.md
│   └── reproducibility.md
├── prompts/
│   ├── copilot-lab.md           # GitHub Copilot prompts
│   └── mcp-lab.md               # MCP tool prompts
└── notes/
    ├── questions.md             # Open questions and research topics
    └── experiments.md           # Experiment log and learnings
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/sophieblock/conda-lab.git
cd conda-lab
```

### 2. Set Up Environment

Install Miniforge (if not already installed):
```bash
# On macOS with Homebrew
brew install miniforge
```

Create the development environment:
```bash
conda env create -f envs/dev.yml
conda activate conda-lab-dev
```

### 3. Open in VS Code

```bash
code workspace/conda-lab.code-workspace
```

### 4. Explore Examples

**Build a simple recipe:**
```bash
conda build recipes/hello-python/
```

**Render with variants:**
```bash
conda render recipes/variants-demo/
```

**Install a plugin:**
```bash
cd plugins/rebuilt-conda-graph/
pip install -e .
conda info --plugins
conda graph numpy --show-deps
```

## 📦 Example Recipes

### hello-c
Simple C program demonstrating:
- Compiler usage (`{{ compiler('c') }}`)
- Platform-specific builds (macOS arm64)
- Native executable packaging

**Build:**
```bash
conda build recipes/hello-c/
```

### hello-python
Pure Python package showing:
- `noarch: python` builds
- Entry points / console scripts
- Minimal dependencies

**Build:**
```bash
conda build recipes/hello-python/
```

### variants-demo
Demonstrates conda-build variants:
- Multiple Python versions (3.10, 3.11)
- Multiple numpy versions
- Custom variant dimensions
- Build string customization

**Render all variants:**
```bash
conda render recipes/variants-demo/
```

## 🔌 Example Plugin

### rebuilt-conda-graph

A minimal conda plugin demonstrating:
- Modern Python packaging (pyproject.toml, src/ layout)
- Entry point registration
- Custom solver implementation (placeholder)
- Custom subcommand (`conda graph`)

**Install:**
```bash
cd plugins/rebuilt-conda-graph/
pip install -e .
```

**Use:**
```bash
conda graph numpy pandas --show-deps
conda install --solver=rebuilt-graph numpy
```

**Structure:**
```
rebuilt-conda-graph/
├── pyproject.toml              # Modern packaging config
├── src/
│   └── conda_graph_rebuilt/
│       ├── __init__.py
│       └── plugin.py           # Hook implementations
└── README.md
```

## 📚 Documentation

### Conda Build
- [macOS Environment Variables](docs/conda-build/macos-env-vars.md) - Understanding build environment on macOS arm64
- [Render vs Build vs Test](docs/conda-build/render-vs-build-vs-test.md) - Three phases of conda-build
- [Build Variants](docs/conda-build/variants.md) - Creating build matrices

### Plugins
- [Plugin Architecture](docs/plugins/plugin-architecture.md) - How conda's plugin system works
- [Entry Points](docs/plugins/entry-points.md) - Deep dive on Python entry points

### General
- [Reproducibility](docs/reproducibility.md) - Strategies for reproducible environments

## 🎓 Learning Paths

### Path 1: Recipe Development
1. Read `docs/conda-build/render-vs-build-vs-test.md`
2. Build `recipes/hello-python/`
3. Modify and rebuild with changes
4. Read `docs/conda-build/variants.md`
5. Experiment with `recipes/variants-demo/`

### Path 2: Plugin Development
1. Read `docs/plugins/plugin-architecture.md`
2. Read `docs/plugins/entry-points.md`
3. Install `plugins/rebuilt-conda-graph/`
4. Modify the plugin and reload
5. Create your own plugin in `plugins/scratch/`

### Path 3: macOS arm64 Deep Dive
1. Read `docs/conda-build/macos-env-vars.md`
2. Build `recipes/hello-c/`
3. Examine the compiled binary with `file` command
4. Experiment with compiler flags
5. Test on different platforms

## 🛠️ Development Workflow

### Building Recipes

```bash
# Render (check template processing)
conda render recipes/hello-python/

# Build (create package)
conda build recipes/hello-python/

# Build without testing
conda build --no-test recipes/hello-python/

# Build specific variant
conda build recipes/variants-demo/ --variants '{"python": "3.11"}'
```

### Testing Plugins

```bash
# Install in development mode
cd plugins/rebuilt-conda-graph/
pip install -e .

# Verify registration
conda info --plugins

# Test functionality
conda graph numpy

# Make changes and reload
pip install -e . --force-reinstall
```

### Managing Environments

```bash
# Create development environment
conda env create -f envs/dev.yml

# Create build environment (with compilers)
conda env create -f envs/build.yml

# Update environment
conda env update -f envs/dev.yml --prune

# Export exact environment
conda env export > environment.lock.yml
```

## 💡 Tips and Tricks

### Debugging Recipes

```bash
# Verbose output
conda build -v recipes/hello-python/

# Keep build directory
conda build --dirty recipes/hello-python/

# Debug mode (drops into build environment)
conda build --debug recipes/hello-python/
```

### Inspecting Packages

```bash
# List package contents
conda build recipes/hello-python/
tar -tzf ~/miniforge3/conda-bld/osx-arm64/hello-python-*.tar.bz2

# Extract package
mkdir temp && cd temp
tar -xf ~/miniforge3/conda-bld/osx-arm64/hello-python-*.tar.bz2
```

### Working with Variants

```bash
# List all variants
conda render recipes/variants-demo/ --variants

# Render specific variant to file
conda render recipes/variants-demo/ \
  --variants '{"python": "3.11", "numpy": "1.26"}' \
  --file rendered.yaml
```

## 🎯 Common Tasks

### Add a New Recipe

1. Create directory: `mkdir recipes/my-recipe`
2. Add `meta.yaml` and `build.sh`
3. Test render: `conda render recipes/my-recipe/`
4. Build: `conda build recipes/my-recipe/`

### Create a Plugin

1. Create directory: `mkdir -p plugins/my-plugin/src/my_plugin`
2. Add `pyproject.toml` with entry points
3. Add `src/my_plugin/plugin.py` with hooks
4. Install: `pip install -e plugins/my-plugin/`
5. Verify: `conda info --plugins`

### Update Documentation

1. Edit relevant `.md` file in `docs/`
2. Test code examples manually
3. Update cross-references if needed
4. Commit changes

## 🔍 Useful Commands

```bash
# Check conda configuration
conda info

# List installed plugins
conda info --plugins

# Check package cache
conda clean --dry-run --all

# Verify recipe
conda build --check recipes/hello-python/

# Search for packages
conda search numpy

# Show package info
conda info numpy
```

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome!

1. Open an issue for discussion
2. Fork and create a feature branch
3. Test your changes
4. Submit a pull request

## 📝 Notes and Questions

- **questions.md**: Open questions and research topics
- **experiments.md**: Experiment log and findings
- **prompts/**: Useful prompts for AI assistants

## 🤖 AI-Powered Development

This repository includes advanced AI assistance for conda development:

### Features
- 🧠 **Custom Copilot Agents** - Specialized planning for conda tasks
- 📋 **Auto-Applied Instructions** - Best practices for recipes, plugins, CI/CD
- 🔌 **MCP Server Integration** - GitHub tools, time operations, sequential thinking
- ⚙️ **Optimized Settings** - 100+ Copilot enhancements for conda workflows

### Quick Start
```
@Plan Create a conda recipe for my-package
@workspace Review this recipe against conda-forge best practices
```

### Documentation
- **[AI Setup Guide](.github/AI-SETUP.md)** - Complete usage documentation
- **[Enhancement Summary](.github/ENHANCEMENT-SUMMARY.md)** - What's included
- **[Workspace Settings](.github/WORKSPACE-SETTINGS.md)** - Settings architecture
- **[Comparison](.github/COMPARISON.md)** - Based on austenstone/.vscode

**New to AI-assisted conda development?** Start with [AI-SETUP.md](.github/AI-SETUP.md)!

## 🔗 References

### Official Documentation
- [Conda Documentation](https://docs.conda.io/)
- [Conda-Build Documentation](https://docs.conda.io/projects/conda-build/)
- [Conda Plugin Documentation](https://docs.conda.io/projects/conda/en/latest/dev-guide/plugins/)

### Tools
- [Miniforge](https://github.com/conda-forge/miniforge) - Minimal conda installer
- [conda-lock](https://github.com/conda/conda-lock) - Lock file generator
- [Mamba](https://github.com/mamba-org/mamba) - Fast conda alternative

### Community
- [Conda-Forge](https://conda-forge.org/) - Community-led conda packages
- [Conda GitHub](https://github.com/conda/conda) - Conda source code

## 📜 License

MIT License - See LICENSE file for details.

## 🙏 Acknowledgments

Built for learning and experimentation with conda, conda-build, and the conda plugin system.
Target platform: macOS arm64 (Apple Silicon) with Miniforge and zsh.
