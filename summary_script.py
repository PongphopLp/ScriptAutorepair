import csv
from collections import defaultdict

def count_mutants(input_file, output_file):
    pair_method_counts = defaultdict(lambda: {"total_mutants": 0, "success": 0, "failed": 0, "skipped": 0})

    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader:
            method_name, result = row
            pair_method = method_name.split('_')[0] + "_" + method_name.split('_')[1]

            pair_method_counts[pair_method]["total_mutants"] += 1
            pair_method_counts[pair_method][result] += 1

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ["Pair_Method", "total_mutants", "success", "failed", "skipped"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for pair_method, counts in pair_method_counts.items():
            writer.writerow({
                "Pair_Method": pair_method,
                "total_mutants": counts["total_mutants"],
                "success": counts["success"],
                "failed": counts["failed"],
                "skipped": counts["skipped"]
            })

if __name__ == "__main__":
    input_csv_file = "result.csv"
    output_csv_file = "output.csv"
    count_mutants(input_csv_file, output_csv_file)
