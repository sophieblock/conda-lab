#!/bin/bash

set -euxo pipefail

# Build the C program
${CC} ${CFLAGS} ${LDFLAGS} -o hello-c hello.c

# Install to PREFIX
mkdir -p ${PREFIX}/bin
cp hello-c ${PREFIX}/bin/

echo "Build complete: hello-c installed to ${PREFIX}/bin/"
