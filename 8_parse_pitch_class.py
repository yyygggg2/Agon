from music21 import converter, note, chord, stream
import csv

def process_element(elem, measure_pitch_classes, measure_number, current_measure_pitch_classes, ongoing_ties):
    """
    Process an individual element, updating the pitch class counts and handling ties.
    Count a note if it's not tied, if it's the start of a tie, or if it's a continuation of a tie from a previous measure.
    """
    if isinstance(elem, note.Note):
        pitch_class = elem.pitch.pitchClass
        if not elem.tie:
            # Note without a tie, count it normally
            measure_pitch_classes[measure_number][pitch_class] += 1
            current_measure_pitch_classes.add(pitch_class)
        else:
            if elem.tie.type == "start":
                # Start of a tie, count it and mark as ongoing
                measure_pitch_classes[measure_number][pitch_class] += 1
                current_measure_pitch_classes.add(pitch_class)
                ongoing_ties[pitch_class] = measure_number  # Mark this pitch class as tied in this measure
            elif elem.tie.type == "continue":
                # If it's a continuation from a previous measure, count it
                if ongoing_ties.get(pitch_class) != measure_number:
                    measure_pitch_classes[measure_number][pitch_class] += 1
                    current_measure_pitch_classes.add(pitch_class)
            elif elem.tie.type == "stop":
                # If stopping a tie, clear the tie status
                if pitch_class in ongoing_ties:
                    del ongoing_ties[pitch_class]
    elif isinstance(elem, chord.Chord):
        for pitch in elem.pitches:
            process_element(note.Note(pitch), measure_pitch_classes, measure_number, current_measure_pitch_classes, ongoing_ties)
    elif isinstance(elem, stream.Stream):
        # Recursively process nested streams, such as Voices
        for nested_elem in elem:
            process_element(nested_elem, measure_pitch_classes, measure_number, current_measure_pitch_classes, ongoing_ties)

def extract_pitch_classes_to_csv(file_path, output_csv_path):
    # Load the MusicXML file
    score = converter.parse(file_path)

    # Initialize structures for storing pitch class counts and tracking ongoing ties
    measure_pitch_classes = {}
    ongoing_ties = {}  # Track ongoing ties by pitch class

    # Iterate through all parts and measures to update pitch class counts
    for part in score.parts:
        for measure in part.getElementsByClass(stream.Measure):
            measure_number = measure.measureNumber
            current_measure_pitch_classes = set()
            if measure_number not in measure_pitch_classes:
                measure_pitch_classes[measure_number] = {pitch_class: 0 for pitch_class in range(12)}
            
            for elem in measure:
                process_element(elem, measure_pitch_classes, measure_number, current_measure_pitch_classes, ongoing_ties)

    # Write results to CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf_8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Measure'] + [f'Pitch Class {i}' for i in range(12)])
        for measure, _ in sorted(measure_pitch_classes.items()):
            writer.writerow([measure] + [measure_pitch_classes[measure][pitch_class] for pitch_class in range(12)])

    print(f"Results exported to {output_csv_path}")

# Specify the file paths and call the function
quatre_reduction = "1_pas_de_quatre_reduction.musicxml"
output_csv_path_quatre = '1_quatre_pitch_classes.csv'

double_reduction = "2_double_pas_de_quatre_reduction.musicxml"
output_csv_path_double = '2_double_pitch_classes.csv'

triple_reduction = "3_triple_pas_de_quatre_reduction.musicxml"
output_csv_path_triple = '3_triple_pitch_classes.csv'

interlude_reduction = "4_interlude_reduction.musicxml"
output_csv_path_interlude = '4_interlude_pitch_classes.csv'

saraband_reduction = "5_saraband_reduction.musicxml"
output_csv_path_saraband = '5_saraband_pitch_classes.csv'

gailliard_reduction = "6_gailliard_reduction.musicxml"
output_csv_path_gailliard = '6_gailliard_pitch_classes.csv'

duos_reduction = "7_four_duos_reduction.musicxml"
output_csv_path_duos = '7_duos_pitch_classes.csv'

# extract_pitch_classes_to_csv(quatre_reduction, output_csv_path_quatre)
extract_pitch_classes_to_csv(quatre_reduction, output_csv_path_quatre)
extract_pitch_classes_to_csv(double_reduction, output_csv_path_double)
extract_pitch_classes_to_csv(triple_reduction, output_csv_path_triple)
extract_pitch_classes_to_csv(interlude_reduction,output_csv_path_interlude)
extract_pitch_classes_to_csv(saraband_reduction,output_csv_path_saraband)
extract_pitch_classes_to_csv(gailliard_reduction,output_csv_path_gailliard)
extract_pitch_classes_to_csv(duos_reduction,output_csv_path_duos)