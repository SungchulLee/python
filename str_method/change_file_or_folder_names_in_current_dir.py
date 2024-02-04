import os

def change_file_or_folder_names_in_current_dir(old_name_part, new_name_part):
    """
    Rename files and folders in the current directory 
    by replacing a specified substring in their names.

    Parameters:
    - old_name_part (str): The substring to be replaced in the file or folder names.
    - new_name_part (str): The replacement substring.

    This function iterates through the files and folders in the current directory 
    and identifies those containing the specified 'old_name_part'. For each match, 
    it replaces 'old_name_part' with 'new_name_part' in the name and renames the file 
    or folder accordingly.

    Example:
    Suppose you have files named 'problem_1.txt', 'problem_2.txt', and 'problem_3.txt' 
    in the current directory. Calling 
    `change_file_or_folder_names_in_current_dir('problem_', '')` will rename these 
    files to '1.txt', '2.txt', and '3.txt' respectively.

    Note:
    - The renaming operation is case-sensitive.
    - This function only operates on files and folders in the current directory.
    """
    # Get a list of names containing the old_name_part
    matching_names = [name for name in os.listdir() if old_name_part in name]

    # Rename each matching file or folder
    for old_name in matching_names:
        new_name = old_name.replace(old_name_part, new_name_part) 
        os.rename(old_name, new_name)

def main():
    # Example usage: Remove 'problem_' from file names in the current directory
    old_name_part = 'problem_'
    new_name_part = ''
    change_file_or_folder_names_in_current_dir(old_name_part, new_name_part)

if __name__ == "__main__":
    main()

