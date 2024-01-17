import os

# List of student IDs
student_ids = [
    'bsce19035', 'bsee20008', 'bsee20029', 'bsee20047', 'bsee20048', 'bsee20053', 'bsee20061', 'bsee20063',
    'bsee20067', 'bsee20069', 'bsee20072', 'bsee20076', 'bsee20077', 'bsee20079', 'bsee20080', 'bsee20083',
    'bsee20084', 'bsee22004', 'bsee22007', 'bsee22008', 'bsee22009', 'bsee22010', 'bsee22012', 'bsee22013',
    'bsee22015', 'bsee22016', 'bsee22018', 'bsee22019', 'bsee22021', 'bsee22022', 'bsee22024', 'bsee22025',
    'bsee22026', 'bsee22027', 'bsee22029', 'bsee22031', 'bsee22033', 'bsee22034', 'bsee22035', 'bsee22038',
    'bsee22039', 'bsee22040', 'bsee22041', 'bsee22042', 'bsee22045', 'bsee22046', 'bsee22047', 'bsee22050',
    'bsee22053', 'bsee22054', 'bsee22056', 'bsee22057', 'bsee22058', 'bsee22059', 'bsee22061', 'bsee22064',
    'bsee22065', 'bsee22069', 'bsee22074', 'bsee22078', 'bsee22081', 'bsee22082', 'bsee22085', 'bsee22088',
    'bscs18012', 'bsee19062', 'bsee21026'
]

# Get the current working directory
base_directory = os.getcwd()

def create_folders(student_ids, base_directory):
    for student_id in student_ids:
        folder_path = os.path.join(base_directory, student_id)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

# Call the function to create folders
create_folders(student_ids, base_directory)
