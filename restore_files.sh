#!/bin/bash

TREE_HASH="bf74d3a66f69f3dc54404d68fccc9efe295a6265"

git ls-tree $TREE_HASH | while read mode type hash filename; do
  echo "Restoring $filename ..."
  git show $hash > "$filename"
done

echo "All files restored from tree $TREE_HASH"Get-ChildItem -Path C:\Users\YourName\Documents\ -Recurse -Force -Directory -Filter ".git" -ErrorAction SilentlyContinue

