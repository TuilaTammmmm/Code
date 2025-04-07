import os

def remove_comments_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if '//' not in line:
                file.write(line)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.cpp'):  # Only process .cpp files
                file_path = os.path.join(root, file)
                remove_comments_in_file(file_path)

folder_path = r'd:\Tam\Code\CodePTIT'
process_folder(folder_path)