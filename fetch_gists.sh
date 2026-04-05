#!/bin/bash

# fetch_gists.sh - Fetches recent public gists for a GitHub user
# Usage: ./fetch_gists.sh [username] [limit] [fetch_content (yes/no)]

USER=${1:-jmikedupont2}
LIMIT=${2:-10}
FETCH_CONTENT=${3:-"no"}

echo "Fetching top $LIMIT gists for user: $USER..."

# Use gh api to fetch gists and jq to format the output
GISTS=$(gh api "users/$USER/gists?per_page=$LIMIT")

if [ "$FETCH_CONTENT" == "yes" ]; then
    echo "$GISTS" | jq -r '.[] | .id' | while read -r GIST_ID; do
        echo "--- Gist: $GIST_ID ---"
        gh gist view "$GIST_ID"
        echo -e "-------------------------\n"
    done
else
    echo "$GISTS" | jq -r '.[] | "[\(.id)] \(.files | keys | .[0]) - \(.description // "No description")"'
fi
