import os

def check_target_occurrence(java_file):
    # Read the Java file
    with open(java_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Count the number of occurrences of "__target__"
    target_count = content.count("__target__")

    # Check if "__target__" appears only once
    if target_count == 1:
        return True
    else:
        return False

def check_target_occurrences(directory):
    for pair_dir in os.listdir(directory):
        pair_dir_path = os.path.join(directory, pair_dir)

        if os.path.isdir(pair_dir_path):
            for method_dir in os.listdir(pair_dir_path):
                method_dir_path = os.path.join(pair_dir_path, method_dir)

                if os.path.isdir(method_dir_path):
                    for filename in os.listdir(method_dir_path):
                        if filename=='Target.java':
                            java_file_path = os.path.join(method_dir_path, filename)
                            if not check_target_occurrence(java_file_path):
                                print(f"File {java_file_path} does not contain a single occurrence of '__target__' or contains it multiple times.")

# Path to the data directory
directory = 'data'
check_target_occurrences(directory)
