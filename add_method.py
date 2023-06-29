import os

def add_method_to_files(pure_folder, mutants_folder):
    for pair_folder in os.listdir(pure_folder): # Pair#

        pure_pair_folder = os.path.join(pure_folder, pair_folder) # pure_method/Pair#

        for method_folder in os.listdir(pure_pair_folder): # Method$

            pure_method_file = os.path.join(pure_pair_folder, method_folder, f'{pair_folder}_{method_folder}_pure.java') # pure_method/Pair#/Method$/Pair#_Method$_pure.java

            pair_method_folder = os.path.join(mutants_folder, pair_folder, f'{pair_folder}_{method_folder}') # mutants/Pair#/Pair#_Method$

            if not os.path.isdir(pair_method_folder):
                continue

            for root, dirs, files in os.walk(pair_method_folder):
                dirs[:] = [d for d in dirs if d.isdigit()]

                for file in files:
                    if file.endswith('.java'):
                        mutant_file_path = os.path.join(root, file)

                        with open(mutant_file_path, 'r') as mutant_file:
                            lines = mutant_file.readlines()

                        class_end_index = None
                        for i, line in enumerate(lines):
                            if line.strip().startswith('}'):
                                class_end_index = i
                                break

                        if class_end_index is not None:
                            with open(mutant_file_path, 'r+') as mutant_file:
                                lines.insert(class_end_index, '\n')
                                with open(pure_method_file, 'r') as pure_file:
                                    pure_lines = pure_file.readlines()
                                lines.insert(class_end_index, '  ' + ''.join(pure_lines) + '\n')
                                mutant_file.seek(0)
                                mutant_file.writelines(lines)

                            print(f'Method added to {mutant_file_path}')

# Usage example
pure_method_folder_path = 'pure_method'
mutants_folder_path = 'mutants'

add_method_to_files(pure_method_folder_path, mutants_folder_path)
