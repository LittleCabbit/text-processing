# Text Processor

This Python script reads a file and finds matches against a predefined set of words. The output of the program shows the match count for each predefined word.

## Features

- Reads an input text file and a predefined words file.
- Counts occurrences of each predefined word in the input text file.
- Outputs the results to a specified output file.
- Supports case-insensitive matching.
- Provides an option for users to choose between the default dataset or a custom dataset.

## Requirements

- Python 3.x
- `collections` module (part of the Python Standard Library)
- `re` module (part of the Python Standard Library)

## Usage

### Input Files

- **Predefined Words File**: A text file containing the predefined words, each word separated by a newline. The file should not contain duplicates.
- **Input Text File**: A plain text (ASCII) file, with every record separated by a new line. The file size can be up to 20 MB.

### Running the Script

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/LittleCabbit/text-processing.git
   cd text-processing
   
2. **Run the Script**:
    ```bash
    python3 process_text.py
### Follow the Prompts

When you run the script, it will prompt you with the following:

1. **Use Default Dataset?**
   - **Prompt**: `Would you like to use the default data set? (Y/n)`
   - **Input Options**:
     - Enter `Y` or press **Enter** to use the default dataset.
     - Enter `N` or `n` to provide custom file paths.

2. **Custom File Paths**
   - If you choose to provide custom file paths, the script will ask for the following:
     - **Predefined Words File**: Enter the path to the file containing the predefined words.
     - **Input Text File**: Enter the path to the input text file.
     - **Output File**: Enter the path where you want to save the match counts.

### Example Interaction
Here\'s how the prompts might look during execution:
    
```bash
python3 process_text.py
```

- Prompt: Would you like to use the default data set? (Y/n)
    - Input: n
- Prompt: Enter the path to the predefined words file:
    - Input: resources/music_predefined_words.txt
- Prompt: Enter the path to the input text file:
    - Input: resources/musical_instruments_resource.txt
- Prompt: Enter the path to the output file:
    - Input: resources/music_output.txt




### Output Format

The output file will contain the match counts in the following format:
```yaml
Predefined word      Match count
detect               20        
name                 196       
ai                   2    
```


### Script Overview

The main components of the script are:

- **`get_predefined_words(self, file_path)`**: Get predefined words from a file and returns a set of words.
- **`process_text(self, file_path, predefined_words)`**: Process the input resource text file and count word matches.
- **`save_output(self, output_file, counts)`**: Save the word match output to a file.
- **`get_user_input(self, prompt, default)`**: Helper function to get user input with a default value.

### Example Files

You can create sample files to test the script:

- Sample Predefined Words File (`predefined_words.txt`, `music_predefined_words.txt`):
- Sample Input Text File (`sample_resource.txt`, `musical_instruments_resource.txt`):

### Testing
Testing done by utilizing the search function in sublime and type `\bword\b` into the search box (replace word with specific word) to check the count result. 

Verified that results are as expected. For example, file musical_instruments_resource.txt has 20 "detect", 196 "name", and 2 "ai".