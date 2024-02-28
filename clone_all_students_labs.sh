#!/bin/bash

# Prompt the user for their GitHub username and password (or use token-based authentication for security).
#USERNAME="HafizUsamz"
#PASSWORD="t"

USERNAME="engrnadirabbas"
PASSWORD="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"
# Organization name
ORG_NAME="ITULahore-CFP"

# Generate auth header
AUTH=$(echo -n $USERNAME:$PASSWORD | base64)

# Get repository URLs for organization members
curl -iH "Authorization: Basic "$AUTH https://api.github.com/orgs/${ORG_NAME}/members?per_page=200 | grep -w login  > members.txt

# Get repository URLs for outside collaborators
curl -iH "Authorization: Basic "$AUTH https://api.github.com/orgs/${ORG_NAME}/outside_collaborators?per_page=200 | grep -w login  > collaborators.txt

# Combine member and collaborator usernames
cat members.txt collaborators.txt > students.txt

cat students.txt | sed 's/^..............//'| sed 's/..$//' > students_clean.txt

#cat students_clean.txt | sed "s|^|https://github.com/${org_name}/${prefix}|" > students_c.txt
#cat students_c.txt | sed "s|$|.git|" > students_cp.txt

# Path to the file containing usernames
USERNAMES_FILE="students_clean.txt"

# Function to clone repository with retries
clone_with_retry() {
    local url="$1"
    local dest="$2"
    local retries=3
    local timeout=4  # Retry for 1.5 minutes (3 retries * 4 seconds)

    for ((i=0; i<retries; i++)); do
        git -C "$dest" clone "$url" && return 0
        sleep $timeout
    done
    return 1
}

while IFS= read -r GITHUB_USER || [[ -n "$GITHUB_USER" ]]; do
    DESTINATION_PATH="./downloads/${GITHUB_USER}"
    mkdir -p "$DESTINATION_PATH"

    for ((lab=1; lab<=14; lab++)); do
        if [ $lab -eq 1 ]; then
            PREFIX="2023-fall-se101a-lab${lab}-introduction-to-github-"
        elif [ $lab -eq 2 ]; then
            PREFIX="fall2023-se101a-pf-lab${lab}-introduction-to-flowchart-"
        elif [ $lab -eq 14 ]; then
            PREFIX="fall2023-se101a-pf-lab$((lab-9))-late-submission-"
        else
            PREFIX="fall2023-se101a-pf-lab${lab}-"
        fi

        REPO_URL="https://github.com/${ORG_NAME}/${PREFIX}${GITHUB_USER}.git"
        CLONE_URL="${REPO_URL/:\/\//:\/\/$USERNAME:$PASSWORD@}"

        clone_with_retry "$CLONE_URL" "$DESTINATION_PATH" || echo "Failed to clone $REPO_URL"
    done
done < "$USERNAMES_FILE"