import os

def create_readme_if_not_exists(folder_path):
    readme_path = os.path.join(folder_path, 'README.md')
    
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as readme_file:
            readme_file.write("")

def process_folders_in_current_directory():
    current_directory = os.getcwd()

    # Get a list of directories in the current directory
    subdirectories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]

    # Iterate through each directory
    for folder in subdirectories:
        folder_path = os.path.join(current_directory, folder)
        create_readme_if_not_exists(folder_path)

if __name__ == "__main__":
    process_folders_in_current_directory()
