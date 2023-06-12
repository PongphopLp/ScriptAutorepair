import os
import subprocess

# Specify the path to Mutanerator.jar
mutanerator_jar_path = 'build/libs/Mutanerator.jar'

# Specify the path to the folder containing the pairs
pairs_folder = 'data'

# Specify the output directory
output_directory = 'output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each pair
for pair_number in range(1, 1343):
    pair_folder_name = f'Pair{pair_number}'
    pair_folder_path = os.path.join(pairs_folder, pair_folder_name)

    # Loop through each method (Method1 and Method2)
    for method_number in range(1, 3):
        method_folder_name = f'Method{method_number}'
        method_folder_path = os.path.join(pair_folder_path, method_folder_name)

        # Specify the path to the Java file to be mutated
        java_file_path = os.path.join(method_folder_path, f'Pair{pair_number}_Method{method_number}.java')

        # Specify the path for the CSV log file
        csv_log_file = os.path.join(output_directory, pair_folder_name, f'Pair{pair_number}_Method{method_number}', 'log.csv')

        # Create the method folder in the output directory
        output_method_folder = os.path.join(output_directory, pair_folder_name, f'Pair{pair_number}_Method{method_number}')
        os.makedirs(output_method_folder)

        # Construct the command to run Mutanerator.jar
        command = f'java -jar {mutanerator_jar_path} -f {java_file_path} -l {csv_log_file}'

        # Run the command
        subprocess.run(command, shell=True, check=True)

        # Check if mutation files are generated
        mutations_directory = 'mutations'
        if os.listdir(mutations_directory):
            # Move the mutated files to the method folder
            for mutation_file in os.listdir(mutations_directory):
                mutation_file_path = os.path.join(mutations_directory, mutation_file)
                mutation_output_path = os.path.join(output_method_folder, mutation_file)
                os.rename(mutation_file_path, mutation_output_path)

            # Move the log.csv file to the method folder
            os.rename(csv_log_file, os.path.join(output_method_folder, 'log.csv'))

print('Mutation process completed successfully!')
