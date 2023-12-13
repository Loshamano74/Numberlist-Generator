#!/bin/bash

# Stash any local changes in untracked files or directories
git stash push --include-untracked

# Fetch the latest changes from the remote repository
git fetch origin

# Reset the local branch to match the remote branch
git reset --hard origin/main  # Replace 'main' with your branch name if different

# Optionally, apply the stashed changes back, if any
git stash apply
