import os
import shutil

source_directory = input("Enter the source directory: ")
target_directory = input("Enter the target directory: ")

# Ensure the target directory exists
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Ask the user whether to copy or move
operation = input("Do you want to copy or move the files? Enter 'copy' or 'move': ").lower()

# Validate user input
if operation not in ['copy', 'move']:
    print("Invalid operation. Please enter 'copy' or 'move'.")
    exit()

# Traverse through the source directory and its subdirectories
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.docx'):
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_directory, file)

            # Perform copy or move based on user input
            if operation == 'copy':
                shutil.copy(source_path, target_path)
            elif operation == 'move':
                shutil.move(source_path, target_path)

print(f"All .docx files moved from {source_directory} and its subdirectories to {target_directory}")