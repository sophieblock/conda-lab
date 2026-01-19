# Experiments and Learnings

Document experiments, findings, and lessons learned in conda-lab.

## Format

Each experiment should include:
- **Date**: When the experiment was run
- **Goal**: What you were trying to learn
- **Setup**: How the experiment was configured
- **Results**: What you found
- **Conclusion**: Key takeaways
- **References**: Related code/docs

---

## Example Experiment Template

### [Date] - [Experiment Title]

**Goal**: What question were you trying to answer?

**Setup**:
```bash
# Commands run
# Files created
# Configuration used
```

**Results**:
- Finding 1
- Finding 2
- Unexpected behavior

**Conclusion**:
Key takeaway or lesson learned.

**References**:
- Code: `path/to/file`
- Docs: `docs/topic.md`
- External: [Link](url)

---

## Completed Experiments

### 2026-01-19 - Initial Repository Setup

**Goal**: Create a minimal conda-lab repository structure following modern Python packaging practices.

**Setup**:
- Created folder structure: recipes/, plugins/, docs/, prompts/, envs/, notes/
- Added three example recipes: hello-c, hello-python, variants-demo
- Created rebuilt-conda-graph plugin with src/ layout
- Added comprehensive documentation
- Configured VS Code multi-root workspace

**Results**:
- Successfully created modular repository structure
- Recipes demonstrate C builds, Python builds, and variants
- Plugin uses modern pyproject.toml with proper entry points
- Documentation covers conda-build and plugin topics
- Workspace configuration supports multi-folder development

**Conclusion**:
A well-organized repository structure helps with:
1. Separation of concerns (recipes vs plugins vs docs)
2. Discoverability (clear folder purposes)
3. Learning (examples demonstrate patterns)
4. Collaboration (VS Code workspace configuration)

**References**:
- Repository structure: Root directory
- Example plugin: `plugins/rebuilt-conda-graph/`
- Documentation: `docs/`

---

## Experiment Ideas

### Recipes

- [ ] Build hello-c recipe on macOS arm64
  - Verify compiler selection
  - Check binary architecture
  - Test package installation

- [ ] Test variants-demo with all combinations
  - Count total builds generated
  - Measure build time per variant
  - Compare build strings

- [ ] Cross-compile a package
  - Target different architecture
  - Handle compiler selection
  - Verify binary format

- [ ] Multi-output recipe
  - Split package into subpackages
  - Test dependency handling
  - Verify file organization

### Plugins

- [ ] Install and test rebuilt-conda-graph plugin
  - Verify entry point registration
  - Test `conda graph` command
  - Check solver registration
  - Measure load time

- [ ] Create minimal plugin from scratch
  - Simplest possible plugin
  - Measure development time
  - Document pain points

- [ ] Plugin interaction test
  - Install multiple plugins
  - Check for conflicts
  - Test load order

- [ ] Plugin error handling
  - Trigger various errors
  - Check conda's response
  - Test recovery behavior

### Build Performance

- [ ] Benchmark variant build times
  - Single variant vs all variants
  - Serial vs parallel builds
  - Cache hit vs miss

- [ ] Compare conda-build vs mamba
  - Same recipe with both
  - Measure speed difference
  - Note feature differences

- [ ] Solver performance testing
  - Large dependency tree
  - Conflicting requirements
  - Multiple solutions

### Environment Reproducibility

- [ ] Test lock file reproducibility
  - Create env from environment.yml
  - Generate lock file
  - Recreate from lock
  - Compare results

- [ ] Cross-platform lock files
  - Generate for macOS arm64
  - Test on macOS x86_64
  - Document differences

- [ ] Environment drift over time
  - Save environment.yml
  - Wait for package updates
  - Try to recreate
  - Document failures

### Documentation

- [ ] Test all code examples
  - Run each command in docs
  - Verify outputs match
  - Fix incorrect examples

- [ ] Documentation coverage
  - List all features
  - Check if documented
  - Identify gaps

- [ ] User journey testing
  - Follow docs as new user
  - Note confusion points
  - Suggest improvements

## Learnings Log

### Conda Build

**Learning**: Selectors are evaluated before Jinja2 variables
- **Date**: TBD
- **Impact**: Affects recipe structure
- **Example**: Can't use variables in selectors
- **Reference**: `docs/conda-build/render-vs-build-vs-test.md`

**Learning**: noarch: python skips variant matrix
- **Date**: TBD
- **Impact**: Faster builds for pure Python
- **Example**: hello-python recipe
- **Reference**: `recipes/hello-python/meta.yaml`

### Plugins

**Learning**: Entry points are cached by Python
- **Date**: TBD
- **Impact**: Must reinstall after changes
- **Example**: `pip install -e .` updates entry points
- **Reference**: `docs/plugins/entry-points.md`

**Learning**: Plugins load lazily on first use
- **Date**: TBD
- **Impact**: Startup performance not affected
- **Example**: Plugin loading on `conda graph`
- **Reference**: Plugin architecture docs

### macOS arm64

**Learning**: $CC automatically set to arm64 clang
- **Date**: TBD
- **Impact**: No manual compiler flags needed
- **Example**: hello-c builds correctly
- **Reference**: `docs/conda-build/macos-env-vars.md`

**Learning**: Skip selector format for arm64
- **Date**: TBD
- **Impact**: Prevents builds on wrong platforms
- **Example**: `skip: True # [not osx or not arm64]`
- **Reference**: Recipe examples

## Failed Experiments

Document failures to avoid repeating them.

### Failed Experiment Template

**Date**: When attempted  
**Goal**: What you tried to do  
**Approach**: How you tried to do it  
**Failure**: What went wrong  
**Lesson**: What you learned  
**Alternative**: What to try instead

---

## Metrics and Benchmarks

### Build Times

| Recipe | Variants | Time | Date | Notes |
|--------|----------|------|------|-------|
| hello-c | 1 | TBD | - | Single platform |
| hello-python | 1 | TBD | - | noarch |
| variants-demo | 12 | TBD | - | 3 Python × 2 NumPy × 2 variants |

### Package Sizes

| Package | Size | Compressed | Date | Notes |
|---------|------|------------|------|-------|
| hello-c | TBD | TBD | - | Native binary |
| hello-python | TBD | TBD | - | Pure Python |

### Plugin Performance

| Plugin | Load Time | Memory | Date | Notes |
|--------|-----------|--------|------|-------|
| rebuilt-conda-graph | TBD | TBD | - | With subcommand |

## Research Findings

### Topic: Conda Solver Algorithms

**Research Date**: TBD  
**Question**: How does conda's solver work?  
**Findings**:
- Uses SAT solver (libsolv)
- Converts dependencies to constraints
- Finds satisfying assignment
- Optimizes for specific criteria

**References**:
- [Libsolv Documentation](https://github.com/openSUSE/libsolv)
- Conda source code

### Topic: Entry Point Discovery

**Research Date**: TBD  
**Question**: How are entry points discovered?  
**Findings**:
- importlib.metadata scans installed packages
- Reads metadata from .dist-info directories
- Entry points grouped by entry point group
- Lazy loading on first access

**References**:
- `docs/plugins/entry-points.md`
- Python importlib.metadata docs

## Next Steps

Based on experiments and learnings:

1. [ ] Run build performance benchmarks
2. [ ] Test plugin installation and discovery
3. [ ] Verify all documentation examples
4. [ ] Create video walkthrough of repository
5. [ ] Set up CI for automated testing

## How to Use This File

1. **Before Experiment**: Copy template, fill in goal/setup
2. **During Experiment**: Take notes on observations
3. **After Experiment**: Document results and conclusions
4. **Reference Later**: Link from documentation or questions.md

## Related Files

- `notes/questions.md` - Open questions to investigate
- `docs/` - Documented findings and guides
- `recipes/` - Example code for experiments
