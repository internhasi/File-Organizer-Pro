import os
import shutil

# Specify the path of the folder you want to organize
# Change 'YourName' to your actual computer username
base_path = 'C:/Users/YourName/Downloads'

# Define the file categories and their corresponding extensions
FILE_TYPES = {
    'IMAGES': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'DOCUMENTS': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'VIDEOS': ['.mp4', '.mov', '.avi', '.mkv'],
    'ARCHIVES': ['.zip', '.rar', '.7z']
}

def organize_files():
    # Loop through each file in the specified directory
    for filename in os.listdir(base_path):
        filepath = os.path.join(base_path, filename)

        # Process only files (ignore subdirectories)
        if os.path.isfile(filepath):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False

            # Check if the file extension matches any defined category
            for category, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    target_folder = os.path.join(base_path, category)
                    
                    # Create the category folder if it doesn't exist
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    
                    # Move the file to the category folder
                    shutil.move(filepath, os.path.join(target_folder, filename))
                    print(f"Moved: {filename} -> {category}")
                    moved = True
                    break
            
            # If the file type is not in our list, skip it
            if not moved:
                print(f"Skipped: {filename} (Unknown type)")

if __name__ == "__main__":
    print("Starting File Organizer...")
    organize_files()
    print("Organization Complete!")
