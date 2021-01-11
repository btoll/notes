#!/usr/bin/env bash
# shellcheck disable=2002

GOMOD_VERSION=$(cat go.mod | awk '/^go[ \t]+[0-9]+\.[0-9]+(\.[0-9]+)?[ \t]*$/{print $2}')
GOLANG_VERSION=$(echo "$GOMOD_VERSION" | awk -F. '{ print $1 "." $2 }')
echo "$GOLANG_VERSION"

