import os

directory = 'data'

# Loop through each pair
for pair in range(1, 1343):
    # Loop through each method
    for method in range(1, 3):
        # Define the file path
        file_path = os.path.join(directory, f'Pair{pair}', f'Method{method}', 'Target_ESTest.java')

        # Read the file content
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Modify the content
        modified_content = []
        for line in content:
            if line.startswith('@RunWith(EvoRunner.class)'):
                line = '//' + line
            elif 'public class Target_ESTest extends Target_ESTest_scaffolding {' in line:
                line = '//' + line
                modified_content.append(line)
                modified_content.append('public class Target_ESTest {\n')
                continue
            modified_content.append(line)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_content)
