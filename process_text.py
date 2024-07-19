import re
from collections import Counter

class TextProcessor:
    # Get predefined words from a file and returns a set of words.
    def get_predefined_words(self, file_path):
        try:
            predefined_words = set()
            with open(file_path, 'r') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    predefined_words.add(word.lower())
        except FileNotFoundError:
            print(f"Error: The predefined word file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing the predefined words: {e}")
        return predefined_words

    # Process the input resource text file and count word matches.
    def process_text(self, file_path, predefined_words):
        counts = Counter()
        pattern = re.compile(r'\b\w+\b', re.IGNORECASE)
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    words = pattern.findall(line)
                    for word in words:
                        word = word.lower()
                        if word in predefined_words:
                            counts[word] += 1
        except FileNotFoundError:
            print(f"Error: The input file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while reading the input text file: {e}")
        return counts

    # Save the word match output to a file.
    def save_output(self, output_file, counts):
        try:
            with open(output_file, 'w') as f:
                f.write(f"{'Predefined word':<20} {'Match count':<10}\n")
                for word in counts:
                    f.write(f"{word:<20} {counts[word]:<10}\n")
        except Exception as e:
            print(f"An error occurred while saving the output match counts: {e}")

    # Get user input for the file resources, if no file provided, use the default one.
    def get_user_input(self, prompt, default):
        user_input = input(prompt)
        return user_input if user_input else default


# Main
sample_predefined_words_file = 'resources/predefined_words.txt'
sample_resource_file = 'resources/sample_resource.txt'
sample_output_file = "resources/output.txt"

textProcessor = TextProcessor()

print("Would you like to use the default sample data set? (Y/n)")
use_default = input().strip().lower()

if use_default in ('n', 'no'):
    predefined_words_file = textProcessor.get_user_input("Enter the path to the predefined words file: ", sample_predefined_words_file)
    input_text_file = textProcessor.get_user_input("Enter the path to the input text resouces file: ", sample_resource_file)
    output_file = textProcessor.get_user_input("Enter the path to the output file: ", sample_output_file)
else:
    predefined_words_file = sample_predefined_words_file
    input_text_file = sample_resource_file
    output_file = sample_output_file


predefined_words = textProcessor.get_predefined_words(predefined_words_file)
print(predefined_words)

counts = textProcessor.process_text(input_text_file, predefined_words)
print(counts)

textProcessor.save_output(output_file, counts)
