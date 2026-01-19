#!/bin/bash

set -euxo pipefail

# Install the Python package
${PYTHON} -m pip install . -vv --no-deps --no-build-isolation

echo "Build complete: hello-python installed"
