import csv

# Define the path to the input CSV file
input_csv_path = "1_quatre_pitch_classes.csv"
input_csv_path = "2_double_pitch_classes.csv"
input_csv_path = "3_triple_pitch_classes.csv"
input_csv_path = "4_interlude_pitch_classes.csv"
input_csv_path = "5_saraband_pitch_classes.csv"
input_csv_path = "6_gailliard_pitch_classes.csv"
input_csv_path = "7_duos_pitch_classes.csv"


# Define the path to the output CSV file
output_csv_path = '1_quatre_summary.csv'
output_csv_path = '2_double_summary.csv'
output_csv_path = '3_triple_summary.csv'
output_csv_path = '4_interlude_summary.csv'
output_csv_path = '5_saraband_summary.csv'
output_csv_path = '6_gailliard_summary.csv'
output_csv_path = '7_duos_summary.csv'

# Function to parse the CSV and generate the desired output
def parse_and_summarize_pitch_classes(input_csv_path, output_csv_path):
    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        # Initialize a set to keep track of all pitch classes used up to the current measure
        all_used_pitch_classes = set()
        # Prepare the data for the output CSV
        output_data = [['Measure', 'Used Pitch Classes',
                        'Cumulative Used Pitch Classes',
                        'Used Count', 'Cumulative Count']]

        for row in reader:
            measure = row[0]
            used_pitch_classes = [str(i) for i, count in enumerate(
                row[1:], start=0) if int(count) > 0]
            all_used_pitch_classes.update(used_pitch_classes)
            output_data.append([measure, ','.join(used_pitch_classes), ','.join(sorted(
                all_used_pitch_classes, key=int)), len(used_pitch_classes), len(all_used_pitch_classes)])

    # Write the results to the output CSV file
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerows(output_data)

    return output_csv_path


# Call the function and print the path to the output CSV file
output_csv_path = parse_and_summarize_pitch_classes(
    input_csv_path, output_csv_path)
