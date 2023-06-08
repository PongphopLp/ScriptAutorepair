import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect('ijadataset.db')
cursor = conn.cursor()

# Retrieve all verified pairs with consensus = 1
cursor.execute('''
    SELECT V.pairid, M1.id, M1.rtext AS left_raw_code, M1.Target_ESTest, M1.Target_ESTest_scaffolding,
           M2.id, M2.rtext AS right_raw_code, M2.Target_ESTest, M2.Target_ESTest_scaffolding
    FROM verifiedpairs V
    JOIN pairs P ON V.pairid = P.id
    JOIN methods M1 ON P.leftMethodID = M1.id
    JOIN methods M2 ON P.rightMethodID = M2.id
    WHERE V.consensus = 1
    ORDER BY V.pairid ASC
''')
results = cursor.fetchall()

# Iterate over the verified pairs and save them in their specific folders
for index, pair in enumerate(results, start=1):
    pair_id = pair[0]
    folder_name = f'Pair{index}'
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Create the folder for the current pair if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the modified raw code into Java files
    with open(os.path.join(folder_path, f'Pair{index}_Method1.java'), 'w', encoding='utf-8') as file1, \
            open(os.path.join(folder_path, f'Pair{index}_Method2.java'), 'w', encoding='utf-8') as file2:
        # Enclose the raw code of the left method with class definition
        left_method_code = f'public class Target {{\n  {pair[2].decode("utf-8")}\n}}'
        file1.write(left_method_code)

        # Enclose the raw code of the right method with class definition
        right_method_code = f'public class Target {{\n  {pair[6].decode("utf-8")}\n}}'
        file2.write(right_method_code)

    # Save the test cases into Java files
    with open(os.path.join(folder_path, f'Pair{index}_Method1_Test.java'), 'w', encoding='utf-8') as file3, \
            open(os.path.join(folder_path, f'Pair{index}_Method2_Test.java'), 'w', encoding='utf-8') as file4, \
            open(os.path.join(folder_path, f'Pair{index}_Method1_Test_Parent.java'), 'w', encoding='utf-8') as file5, \
            open(os.path.join(folder_path, f'Pair{index}_Method2_Test_Parent.java'), 'w', encoding='utf-8') as file6:
        file3.write(pair[3].decode('utf-8'))  # Write the test cases of the left method into PairN_Method1_Test.java
        file4.write(pair[7].decode('utf-8'))  # Write the test cases of the right method into PairN_Method2_Test.java
        file5.write(pair[4].decode('utf-8'))  # Write the scaffolding test cases of the left method into PairN_Method1_Test_Parent.java
        file6.write(pair[8].decode('utf-8'))  # Write the scaffolding test
