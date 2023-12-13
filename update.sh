#!/bin/bash

# Fetch the latest changes from the remote repository
git fetch origin

# Reset the local branch to match the remote branch
git reset --hard origin/main  # Replace 'main' with your branch name if different

# Optionally, pull the changes (Use with caution as this might override local changes)
# git pull origin main
