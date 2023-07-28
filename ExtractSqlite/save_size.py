import sqlite3
import pandas as pd

# Connect to the SQLite database
try:
    conn = sqlite3.connect('ijadataset.db')
    cursor = conn.cursor()
except Exception as e:
    print(f"Error connecting to the database: {e}")
    exit(1)

# Prepare the SQL query
query = '''
    SELECT V.pairid, M1.size AS method1_size, M2.size AS method2_size
    FROM verifiedpairs V
    JOIN pairs P ON V.pairid = P.id
    JOIN methods M1 ON P.leftMethodID = M1.id
    JOIN methods M2 ON P.rightMethodID = M2.id
    WHERE V.consensus = 1
    ORDER BY V.pairid ASC
'''

try:
    # Execute the query and fetch the results
    cursor.execute(query)
    results = cursor.fetchall()

    # Create a list of dictionaries to hold the data
    data_list = []
    for index, pair in enumerate(results, start=1):
        pair_num = index
        method1_size = pair[1]
        method2_size = pair[2]
        data_list.append({'Pair Number': pair_num, 'Method1 Size': method1_size, 'Method2 Size': method2_size})

    # Convert the list of dictionaries to a DataFrame
    data = pd.DataFrame(data_list)

    # Save the DataFrame to an Excel file
    data.to_excel('method_sizes.xlsx', index=False)

    print("Data saved to 'method_sizes.xlsx'.")
except Exception as e:
    print(f"Error while fetching or processing data: {e}")
finally:
    # Close the database connection
    conn.close()
