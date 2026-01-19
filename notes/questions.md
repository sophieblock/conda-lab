# Questions and Open Issues

Track questions, uncertainties, and areas for investigation in conda-lab.

## Conda Build Questions

### Variants

- [ ] How do zip_keys actually work in conda_build_config.yaml?
- [ ] Can you have nested variant dimensions?
- [ ] What's the performance impact of large variant matrices?
- [ ] How does conda-build parallelize variant builds?

### Selectors

- [ ] What's the complete list of available selectors?
- [ ] Can you create custom selectors?
- [ ] How do selectors interact with variants?
- [ ] Are there selector performance considerations?

### Environment Variables

- [ ] What environment variables are available in test phase?
- [ ] How do BUILD_PREFIX and PREFIX differ?
- [ ] Can you set custom environment variables in meta.yaml?
- [ ] How are environment variables passed to subprocesses?

### macOS arm64 Specifics

- [ ] When should you use `skip: True # [not osx or not arm64]`?
- [ ] How to handle packages that need Rosetta?
- [ ] What's the proper way to detect arm64 in build scripts?
- [ ] Are there arm64-specific compiler flags to be aware of?

## Plugin Questions

### Architecture

- [ ] Can plugins depend on other plugins?
- [ ] How do multiple plugins interact if they implement the same hook?
- [ ] Is there a plugin priority or loading order?
- [ ] Can plugins be dynamically loaded/unloaded?

### Solvers

- [ ] How does conda's default solver work under the hood?
- [ ] What algorithms are best for dependency resolution?
- [ ] How to handle cyclic dependencies in a custom solver?
- [ ] Performance optimization strategies for large repos?

### Testing

- [ ] Best practices for testing conda plugins?
- [ ] How to mock conda internals in tests?
- [ ] Integration testing vs unit testing for plugins?
- [ ] How to test plugin interactions with conda core?

### Distribution

- [ ] Should plugins be distributed via conda or pip?
- [ ] How to version plugins relative to conda versions?
- [ ] Handling breaking changes in conda plugin API?
- [ ] Best practices for plugin documentation?

## Reproducibility Questions

### Lock Files

- [ ] conda-lock vs conda list --explicit - when to use which?
- [ ] How to handle lock files across different architectures?
- [ ] Managing lock file drift over time?
- [ ] Lock files in monorepo setups?

### Channels

- [ ] Channel priority rules and implications?
- [ ] How to create and maintain a private channel?
- [ ] Channel mirroring for air-gapped environments?
- [ ] Mixing conda-forge and defaults - best practices?

### Environments

- [ ] When to use environment.yml vs requirements.txt vs setup.py?
- [ ] How to handle dev vs prod environment differences?
- [ ] Managing multiple related environments?
- [ ] Environment cleanup and maintenance strategies?

## Performance Questions

### Build Time

- [ ] What makes conda-build slow?
- [ ] Caching strategies for faster rebuilds?
- [ ] Parallel building of variants?
- [ ] Build time comparison: conda-build vs other tools?

### Solver Performance

- [ ] When does solving become slow?
- [ ] How to debug slow solver operations?
- [ ] Mamba vs conda solver - when to use which?
- [ ] Solver caching and optimization?

## Integration Questions

### VS Code

- [ ] Best extensions for conda development?
- [ ] Debugging conda recipes in VS Code?
- [ ] Multi-root workspace tips and tricks?
- [ ] Language server integration for meta.yaml?

### CI/CD

- [ ] GitHub Actions setup for conda packages?
- [ ] Caching conda environments in CI?
- [ ] Testing across multiple platforms?
- [ ] Automated recipe updates?

### Docker

- [ ] Best practices for conda in containers?
- [ ] Miniforge vs Miniconda vs Anaconda in Docker?
- [ ] Layer caching strategies?
- [ ] Multi-stage builds with conda?

## Ecosystem Questions

### Conda vs Pip

- [ ] When should you use conda vs pip?
- [ ] Can you safely mix conda and pip?
- [ ] How to handle packages only available in one ecosystem?
- [ ] Best practices for dual distribution?

### Conda-Forge

- [ ] How does conda-forge infrastructure work?
- [ ] Contributing recipes to conda-forge?
- [ ] Maintaining conda-forge feedstocks?
- [ ] conda-forge vs private channels?

## Research Topics

### Algorithm Deep Dives

- [ ] SAT solver algorithms in conda
- [ ] Graph theory in dependency resolution
- [ ] Constraint satisfaction approaches
- [ ] Alternative solver implementations

### Comparison Studies

- [ ] Conda vs Nix vs Guix
- [ ] Conda vs Poetry vs PDM
- [ ] Performance benchmarks
- [ ] Feature comparison matrix

### Future Directions

- [ ] What's next for conda?
- [ ] Emerging patterns in package management?
- [ ] WebAssembly and conda?
- [ ] Conda in edge computing?

## Documentation Gaps

### Need More Research

- [ ] Complete selector reference
- [ ] Environment variable reference
- [ ] Plugin API edge cases
- [ ] Advanced variant patterns

### Need Examples

- [ ] Complex multi-output recipes
- [ ] Cross-compilation examples
- [ ] Plugin error handling patterns
- [ ] Migration guides

### Need Clarification

- [ ] Ambiguous documentation sections
- [ ] Conflicting information sources
- [ ] Outdated documentation
- [ ] Missing API documentation

## Experiments to Run

### Recipe Experiments

- [ ] Multi-output recipe with variants
- [ ] Recipe with custom selectors
- [ ] Cross-compiled package
- [ ] Package with complex dependencies

### Plugin Experiments

- [ ] Plugin with multiple hooks
- [ ] Plugin dependency management
- [ ] Plugin configuration system
- [ ] Plugin error recovery

### Performance Experiments

- [ ] Variant build parallelization
- [ ] Solver performance profiling
- [ ] Cache effectiveness testing
- [ ] Large repository benchmarks

## Questions from Team

_Add questions that come up during development or reviews_

### From Code Review

- [ ] Question 1
- [ ] Question 2

### From User Feedback

- [ ] Question 1
- [ ] Question 2

### From Debugging

- [ ] Question 1
- [ ] Question 2

## How to Use This File

1. **Add Questions**: As they come up during work
2. **Research**: Mark with [RESEARCHING] when investigating
3. **Answer**: Replace question with link to documentation/code
4. **Archive**: Move answered questions to experiments.md or docs

## Related Files

- `notes/experiments.md` - Experiment results and learnings
- `docs/` - Documented answers to questions
- `prompts/` - Prompts for researching questions
