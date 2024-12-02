import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def list_directory(commands):
    result = os.system(commands)
    return result
command = input("enter a command:  ")
list_directory(command)
# def main():
#     folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
#     command = input("Enter a command")
#     res = list_directory(command)
#     print(res)
#     for folder_path in folder_paths:
#         files, error_message = list_files_in_folder(folder_path)
#         if files:
#             print(f"Files in {folder_path}:")
#             for file in files:
#                 print(file)
#         else:
#             print(f"Error in {folder_path}: {error_message}")
#     for ls in res:
#         print(ls)

# if __name__ == "__main__":
#     main()