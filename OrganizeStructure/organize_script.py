import os
import shutil

# Source directory
source_directory = 'data'

# Destination directory
destination_directory = 'output'

# Iterate over the pairs and methods
for pair_number in range(1, 1343):
    for method_number in range(1, 3):
        # Create the source and destination paths
        source_path = os.path.join(source_directory, f'Pair{pair_number}', f'Method{method_number}')
        destination_path = os.path.join(destination_directory, f'Pair{pair_number}', f'Pair{pair_number}_Method{method_number}', 'test')

        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Move the files
        source_file1 = os.path.join(source_path, 'Target_ESTest.java')
        destination_file1 = os.path.join(destination_path, 'Target_ESTest.java')
        shutil.move(source_file1, destination_file1)

        
