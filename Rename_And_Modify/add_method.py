import os

def add_method(pure_test_file, mutant_test_file):
    with open(pure_test_file, 'r', encoding='utf-8') as pure_file:
        pure_lines = pure_file.readlines()

    with open(mutant_test_file, 'r', encoding='utf-8') as mutant_file:
        mutant_lines = mutant_file.readlines()

    class_declaration_index = -1

    # Find the class declaration in the mutant test file
    for i, line in enumerate(mutant_lines):
        if 'class' in line:
            class_declaration_index = i
            break

    if class_declaration_index != -1:
        mutant_lines.insert(class_declaration_index + 1, '\n')
        mutant_lines[class_declaration_index + 2: class_declaration_index + 2] = pure_lines

        with open(mutant_test_file, 'w', encoding='utf-8') as modified_file:
            modified_file.writelines(mutant_lines)

        print('Method added successfully!')
    else:
        print('Class declaration not found in the mutant test file.')



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

                        add_method(pure_method_file, mutant_file_path)
                        print(f'Method added to {mutant_file_path}')


# Usage example
pure_method_folder_path = 'pure_method'
mutants_folder_path = 'mutants'

add_method_to_files(pure_method_folder_path, mutants_folder_path)
