import os

# Specify the range of folder names
start_number = 23001
end_number = 23070

# Specify the base folder name
base_folder_name = "bsee"

# Create folders
for number in range(start_number, end_number + 1):
    folder_name = f"{base_folder_name}{number:05d}"
    os.makedirs(folder_name)

print(f"Folders created from {base_folder_name}{start_number:05d} to {base_folder_name}{end_number:05d}")
