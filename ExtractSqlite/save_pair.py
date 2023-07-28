import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect('ijadataset.db')
cursor = conn.cursor()

# Retrieve all verified pairs with consensus = 1
cursor.execute('''
    SELECT V.pairid, M1.id, M1.rtext AS left_raw_code, M1.Target_ESTest, 
           M2.id, M2.rtext AS right_raw_code, M2.Target_ESTest
    FROM verifiedpairs V
    JOIN pairs P ON V.pairid = P.id
    JOIN methods M1 ON P.leftMethodID = M1.id
    JOIN methods M2 ON P.rightMethodID = M2.id
    WHERE V.consensus = 1
    ORDER BY V.pairid ASC
''')
results = cursor.fetchall()
# [0] = pairid, [1] = Method1 id, [2] = Method1 raw code, [3] = Method1 test case
# [4] = Method2 id, [5] = Method2 raw code, [6] = Method2 test case

# Create the main output directory if it doesn't exist
output_directory = 'data'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate over the verified pairs and save them in their specific folders
for index, pair in enumerate(results, start=1):
    pair_directory = os.path.join(output_directory, f'Pair{index}')
    
    # Create the pair directory
    if not os.path.exists(pair_directory):
        os.makedirs(pair_directory)
    
    # Create Method1 and Method2 subdirectories
    method1_directory = os.path.join(pair_directory, 'Method1')
    method2_directory = os.path.join(pair_directory, 'Method2')
    
    if not os.path.exists(method1_directory):
        os.makedirs(method1_directory)
    
    if not os.path.exists(method2_directory):
        os.makedirs(method2_directory)
    
    # Save the modified raw code into Java files
    with open(os.path.join(method1_directory, f'Target.java'), 'w', encoding='utf-8') as file1, \
            open(os.path.join(method2_directory, f'Target.java'), 'w', encoding='utf-8') as file2:
        # Enclose the raw code of the left method with class definition
        left_method_code = f'import java.util.*;\n\npublic class Target {{\n  {pair[2].decode("utf-8")}\n}}'
        file1.write(left_method_code)

        # Enclose the raw code of the right method with class definition
        right_method_code = f'import java.util.*;\n\npublic class Target {{\n  {pair[5].decode("utf-8")}\n}}'
        file2.write(right_method_code)

    # Save the test cases and scaffolding into Java files
    with open(os.path.join(method1_directory, f'Target_ESTest.java'), 'w', encoding='utf-8') as file3, \
            open(os.path.join(method2_directory, f'Target_ESTest.java'), 'w', encoding='utf-8') as file4:
        file3.write(pair[3].decode('utf-8')) # Write the test cases of the left method into Target_ESTest.java
        file4.write(pair[6].decode('utf-8')) # Write the test cases of the right method into Target_ESTest.java
