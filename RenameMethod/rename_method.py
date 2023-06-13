import os
import re

def rename_method_name(java_file):
    # Read the Java file with the correct encoding
    with open(java_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find the method declaration
    method_declaration = re.search(r'\w+ \w+\(.*?\)', content)
    if method_declaration:
        # Get the original method name
        original_method_name = method_declaration.group(0).split()[1].split('(')[0]

        # Generate a new method declaration with the renamed method
        new_method_declaration = method_declaration.group(0).replace(original_method_name, "__target__")

        # Replace the method declaration in the file
        modified_content = content.replace(method_declaration.group(0), new_method_declaration)

        # Write the modified content back to the Java file
        with open(java_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Renamed method name in {java_file} from '{original_method_name}' to '__target__'")

def rename_method_names(directory):
    # Iterate over each Pair directory
    for pair_dir in os.listdir(directory):
        pair_dir_path = os.path.join(directory, pair_dir)

        # Check if it's a directory
        if os.path.isdir(pair_dir_path):
            # Iterate over each Method directory
            for method_dir in os.listdir(pair_dir_path):
                method_dir_path = os.path.join(pair_dir_path, method_dir)

                # Check if it's a directory
                if os.path.isdir(method_dir_path):
                    # Iterate over each Java file in the Method directory
                    for filename in os.listdir(method_dir_path):
                        if filename.endswith('.java') and filename.startswith(pair_dir):
                            java_file_path = os.path.join(method_dir_path, filename)
                            rename_method_name(java_file_path)

# Path to the data directory
directory = 'data'

rename_method_names(directory)
