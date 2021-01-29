#!/usr/bin/env bash
[ -z "$1" ] && echo "no endpoint name supplied" && exit 1

if [ -e "./src/endpoints/$1" ]; then
    echo "not creating - endpoint already exists"
    exit 1
else
    cp -r ./src/_template_ ./src/endpoints/$1
    echo "created new endpoint '$1'"
fi