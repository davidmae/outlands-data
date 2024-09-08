import os
import glob

def get_last_journal_file(directory):
    """Returns the path to the last journal file in the given directory"""
    files = glob.glob(os.path.join(directory, '*.txt'))
    return max(files, key=os.path.getctime)

import re

import re

def extract_text_from_journal_file(file_path):
    """Extracts text from the given journal file"""
    with open(file_path, 'r') as file:
        text = file.read()
        pattern = r"You see: (.*)"
        matches = re.findall(pattern, text)
        item_counts = {}
        for match in matches:
            if match.startswith('(') or match.startswith('['):
                continue
            if match in item_counts:
                item_counts[match] += 1
            else:
                item_counts[match] = 1
        result = []
        for item, count in item_counts.items():
            if count > 1:
                result.append(f"- {item} x{count}")
            else:
                result.append(f"- {item}")
        return "\n".join(result)

import datetime

def main():
    directory = 'Client/JournalLogs'
    last_journal_file = get_last_journal_file(directory)
    text = extract_text_from_journal_file(last_journal_file)
    output_file_name = f"WTS-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
    with open(output_file_name, 'w') as file:
        file.write("\n=============================================\n                   WTS\n=============================================\n" + text + "\n=============================================")
    print(f"Output saved to {output_file_name}")

if __name__ == '__main__':
    main()