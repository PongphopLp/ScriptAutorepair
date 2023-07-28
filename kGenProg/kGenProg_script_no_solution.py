import os
import csv
import shutil

def run_kgenprog(method_dir_path, method_dir, test_dir):
    # Get the list of mutant subfolders
    mutant_subfolders = [folder for folder in os.listdir(method_dir_path) if folder.isdigit()]

    # Iterate over each mutant subfolder
    for mutant_subfolder in mutant_subfolders:
        mutant_subfolder_path = os.path.join(method_dir_path, mutant_subfolder)

        # Check if it's a directory
        if os.path.isdir(mutant_subfolder_path):
            # Specify the path to the mutant's .java file
            source_file = os.path.join(mutant_subfolder_path, f"Target.java")

            # Specify the path to the test directory
            test_file = os.path.join(test_dir, f"Target_ESTest.java")

            # Construct the kGenProg command
            command = f"java -jar kGenProg-1.8.2.jar -r ./ -s {source_file} -t {test_file} -c evosuite-1.2.0.jar -o output_no_sol --patch-output"

            # Run the kGenProg command
            os.system(command)

            # Path to the result CSV file
            result_csv = 'result_no_sol.csv'

            # Check if the command was successful
            if os.path.exists("output_no_sol"):
                # Check if there are files in the output directory
                output_dir = "output_no_sol"
                if len(os.listdir(output_dir)) > 0:
                    print("There are files in the output directory")

                    # Rename the folder inside the output directory
                    for folder_name in os.listdir(output_dir):
                        folder_path = os.path.join(output_dir, folder_name)
                        if os.path.isdir(folder_path):
                            renamed_folder = f"{method_dir}_{mutant_subfolder}"
                            renamed_folder_path = os.path.join(output_dir, renamed_folder)
                            os.rename(folder_path, renamed_folder_path)

                            # Move the renamed folder to 'all_pairs_patch' directory
                            all_pairs_patch_dir = os.path.join(os.path.dirname(output_dir), 'all_pairs_patch_no_sol')
                            if not os.path.exists(all_pairs_patch_dir):
                                os.makedirs(all_pairs_patch_dir)
                            shutil.move(renamed_folder_path, os.path.join(all_pairs_patch_dir, renamed_folder))
                            break

                    write_result_to_csv(result_csv, method_dir, mutant_subfolder, "success")

                else:
                    print("No files in the output directory")
                    write_result_to_csv(result_csv, method_dir, mutant_subfolder, "failed")
            else:
                print("Error occurred during kGenProg execution and there is no output directory")
                write_result_to_csv(result_csv, method_dir, mutant_subfolder, "skipped")

def write_result_to_csv(result_csv, method_dir, mutant_subfolder, result):
    # Check if the result CSV file exists
    if os.path.isfile(result_csv):
        # Append a new row to the CSV file
        with open(result_csv, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([f"{method_dir}_{mutant_subfolder}", result])
    else:
        # Create a new CSV file and write the header and row
        with open(result_csv, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Method", "Result"])
            writer.writerow([f"{method_dir}_{mutant_subfolder}", result])

def iterate_all_pairs(root_directory):
    # Get the list of pair directories and sort numerically
    sorted_directories = sorted([pair_dir for pair_dir in os.listdir(root_directory) if pair_dir.startswith("Pair")], key=lambda x: int(x[4:]))

    # Iterate over each pair directory
    for pair_dir in sorted_directories:
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
                    mutant_subfolders = [folder for folder in os.listdir(method_dir_path) if folder.isdigit()]

                    # Check if the mutant subfolders exist
                    if mutant_subfolders:
                        run_kgenprog(method_dir_path, method_dir, test_dir)
                    else:
                        print(f"No mutants found in {method_dir_path}. Skipping.")

# Path to the root directory of the target project
root_directory = 'data_no_sol'

# Delete the result CSV file if it exists
if os.path.isfile('result_no_sol.csv'):
    os.remove('result_no_sol.csv')

# Run kGenProg for all pairs
iterate_all_pairs(root_directory)
