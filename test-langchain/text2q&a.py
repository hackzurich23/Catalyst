from typing import Dict
import csv


def append_q_and_a_to_csv(q_and_a: Dict[str, str]):
    output_file = "generated_q_and_a_correct.csv"

    with open(output_file, mode="a") as output_csv_file:
        csv_writer = csv.writer(output_csv_file)

        for row in csv_reader:
            if len(row) >= 2:
                # Combine everything after the first comma and wrap it in double quotes
                row = [row[0], '"' + ','.join(row[1:]) + '"']
            csv_writer.writerow(row)

    print(f'CSV file "{input_file}" has been modified and saved as "{output_file}".')