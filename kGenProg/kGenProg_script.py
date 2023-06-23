import os

def run_kgenprog(method_dir_path, method_dir, test_dir):
    # Get the list of mutant subfolders
    mutant_subfolders = [folder for folder in os.listdir(method_dir_path) if folder.isdigit()]

    # print("mutant_subfolders =",mutant_subfolders)

    # Iterate over each mutant subfolder
    for mutant_subfolder in mutant_subfolders:
        mutant_subfolder_path = os.path.join(method_dir_path, mutant_subfolder) # data/PairN/PairN_MethodM/number

        # Check if it's a directory
        if os.path.isdir(mutant_subfolder_path):
            # Specify the path to the mutant's .java file
            source_file = os.path.join(mutant_subfolder_path, f"{method_dir}.java") # data/PairN/PairN_MethodM/number/PairN_MethodM.java

            # Specify the path to the test directory
            test_directory = test_dir # data/PairN/PairN_MethodM/test

            # Construct the kGenProg command
            command = f"java -jar kGenProg-1.8.2.jar -r ./ -s {source_file} -t {test_directory} -c evosuite-1.2.0.jar" 
            # {source_file} = data/PairN/PairN_MethodM/number/PairN_MethodM.java || {test_directory} = data/PairN/PairN_MethodM/test

            # Run the kGenProg command
            os.system(command)

def iterate_all_pairs(root_directory):
    # Get the list of pair directories and sort numerically
    sorted_directories = sorted([pair_dir for pair_dir in os.listdir(root_directory) if pair_dir.startswith("Pair")], key=lambda x: int(x[4:])) # Sort by PairN++

    # Iterate over each pair directory
    for pair_dir in sorted_directories: # Pair1-1342
        pair_dir_path = os.path.join(root_directory, pair_dir) # data/PairN

        # Check if it's a directory
        if os.path.isdir(pair_dir_path): # data/PairN = folder?
            # Iterate over each method directory
            for method_dir in os.listdir(pair_dir_path): # PairN_MethodM/
                method_dir_path = os.path.join(pair_dir_path, method_dir) # data/PairN/PairN_MethodM

                # Check if it's a directory
                if os.path.isdir(method_dir_path): # data/PairN/PairN_MethodM = folder?
                    # Specify the path to the test directory
                    test_dir = os.path.join(method_dir_path, "test") # data/PairN/PairN_MethodM/test

                    # Get the list of mutant subfolders
                    mutant_subfolders = [folder for folder in os.listdir(method_dir_path) if folder.isdigit()] # [N, N+, N++, ...]
                    

                    # print("mutant_subfolders =",mutant_subfolders)


                    # Check if the mutant subfolders exist
                    if mutant_subfolders:
                        run_kgenprog(method_dir_path, method_dir, test_dir)
                    else:
                        print(f"No mutants found in {method_dir_path}. Skipping.")

# Path to the root directory of the target project
root_directory = 'data'

# Run kGenProg for all pairs
iterate_all_pairs(root_directory)
