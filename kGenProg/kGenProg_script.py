import os

def run_kgenprog(pair_dir, method_dir, test_dir):
    # Get the list of mutant subfolders
    mutant_subfolders = os.listdir(pair_dir)

    # Iterate over each mutant subfolder
    for mutant_subfolder in mutant_subfolders:
        mutant_subfolder_path = os.path.join(pair_dir, mutant_subfolder)

        # Check if it's a directory and not the "test" folder
        if os.path.isdir(mutant_subfolder_path) and mutant_subfolder != "test":
            # Specify the path to the mutant's .java file
            source_file = os.path.join(mutant_subfolder_path, f"{method_dir}.java")

            # Specify the path to the test directory
            test_directory = test_dir

            # Construct the kGenProg command
            command = f"java -jar kGenProg-1.8.2.jar -r ./ -s {source_file} -t {test_directory} -c evosuite-1.2.0.jar"

            # Run the kGenProg command
            os.system(command)

def iterate_all_pairs(root_directory):
    # Get the list of pair directories and sort numerically
    pair_directories = sorted([pair_dir for pair_dir in os.listdir(root_directory) if pair_dir.startswith("Pair")], key=lambda x: int(x[4:]))

    # Iterate over each pair directory
    for pair_dir in pair_directories:
        pair_dir_path = os.path.join(root_directory, pair_dir)

        # Check if it's a directory
        if os.path.isdir(pair_dir_path):
            # Iterate over each method directory
            for method_dir in os.listdir(pair_dir_path):
                method_dir_path = os.path.join(pair_dir_path, method_dir)

                # Check if it's a directory
                if os.path.isdir(method_dir_path):
                    # Specify the path to the test directory
                    test_dir = os.path.join(method_dir_path, "test")

                    # Get the list of mutant subfolders
                    mutant_subfolders = os.listdir(method_dir_path)

                    # Check if the mutant subfolders exist
                    if mutant_subfolders:
                        run_kgenprog(method_dir_path, method_dir, test_dir)
                    else:
                        print(f"No mutants found in {method_dir_path}. Skipping.")

# Path to the root directory of the target project
root_directory = 'data'

# Run kGenProg for all pairs
iterate_all_pairs(root_directory)
