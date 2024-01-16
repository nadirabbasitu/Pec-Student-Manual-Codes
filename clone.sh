#!/bin/bash

# Prompt the user for their GitHub username and password (or use token-based authentication for security).
#USERNAME="HafizUsamz"
#PASSWORD="t"

USERNAME="naditu"
PASSWORD="gUHFLVfIc4UZyx0"

# Organization name
ORG_NAME="ITU-Lahore-CFP"

# Prompt the user for their GitHub username
echo "Enter the GitHub username for which you want to download assignments:"
read GITHUB_USER

# Path where you want to clone the repository
DESTINATION_PATH="./downloads/${GITHUB_USER}"

# Create the download directory if it doesn't exist.
mkdir -p $DESTINATION_PATH

# Generate auth header
AUTH=$(echo -n $USERNAME:$PASSWORD | base64)

# Clone the specific repositories for labs 2 to 13
# Clone the specific repositories for labs 1 to 13
for ((lab=1; lab<=13; lab++))
do
  if [ $lab -eq 1 ]; then
    # Define the assignment prefix for lab 1
    PREFIX="fall2023-ce100-cfp-lab${lab}-"
  else
    # Define the assignment prefix for labs 2 to 13
    PREFIX="fall2023-ce100-cfp-lab${lab}-"
  fi
  
  # URL of the specific GitHub repository you want to download
  REPO_URL="https://github.com/${ORG_NAME}/${PREFIX}${GITHUB_USER}.git"
  
  # Insert username:password after protocol:// to generate clone URL
  CLONE_URL=$(echo "$REPO_URL" | sed "s/:\/\/git/:\/\/$USERNAME\:$PASSWORD\@git/")
  
  # Clone the specific repository
  git -C $DESTINATION_PATH clone $CLONE_URL
done
