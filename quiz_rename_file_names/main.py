import os

def main():
    # Get the current working directory
    current_directory = os.getcwd()

    # Iterate through all items in the current working directory
    for item in os.listdir(current_directory):
        # Check if the item is a directory and starts with "problem_"
        if os.path.isdir(item) and item.startswith("problem_"):
            # Construct the new name by removing the "problem_" prefix
            new_name = item[len("problem_"):]

            # Construct the full paths for the old and new names
            old_path = os.path.join(current_directory, item)
            new_path = os.path.join(current_directory, new_name)

            # Rename the directory
            os.rename(old_path, new_path)

            print(f'Renamed: {item} to {new_name}')

if __name__ == "__main__":
    main()
