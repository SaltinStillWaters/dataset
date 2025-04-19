import csv
import re
import os

def convert_for_labelstudio(filenames, txt_dir, csv_dir):
    for name in filenames:
        txt_file = os.path.join(txt_dir, f"{name}.txt")
        csv_file = os.path.join(csv_dir, f"{name}.csv")

        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Skip the title line
        content = ''.join(lines[1:]).strip()

        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', content)
        clean_sentences = [s.strip() for s in sentences if s.strip()]

        # Write CSV compatible with Label Studio
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['text'], quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for sentence in clean_sentences:
                writer.writerow({'text': sentence})

        print(f"✅ Processed for Label Studio: {name}.csv")

# Setup
txt_dir = 'Khan_cleaned'
csv_dir = 'Khan_csv'
os.makedirs(csv_dir, exist_ok=True)
filenames = [str(i) for i in range(101, 151)]

convert_for_labelstudio(filenames, txt_dir, csv_dir)
