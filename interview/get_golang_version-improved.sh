#!/usr/bin/env bash

# 1. Useless use of `cat`.
# 2. Simplify regex.
# 3. Use a here string (in a pipeline the commands run in a subshell, the vars can get "lost") instead of `echo`.
# 4. No need for the `GOLANG_VERSION`.
# 5. Use shell built-in commands.

set -eo pipefail

GOMOD_VERSION=$(awk '/^go\s(.[0-9])*/{print $2}' go.mod)
awk -F. '{ print $1 "." $2 }' <<< "$GOMOD_VERSION"

