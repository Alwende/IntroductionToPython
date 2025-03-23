import os

def process_text(input_file, output_file):
    try:
        # Print the current working directory
        print(f"Current working directory: {os.getcwd()}")

        # List the files in the current directory
        print(f"Files in the current directory: {os.listdir()}")

        # Print the absolute path of the input file
        input_file_path = os.path.abspath(input_file)
        print(f"Absolute path of input file: {input_file_path}")

        # Read the contents of input.txt
        with open(input_file, 'r') as file:
            content = file.read()

        # Count the number of words in the file
        word_count = len(content.split())

        # Convert all text to uppercase
        processed_content = content.upper()

        # Write the processed text and the word count to output.txt
        with open(output_file, 'w') as file:
            file.write(processed_content)
            file.write(f"\n\nWord Count: {word_count}")

        # Print a success message
        print(f"Success! The processed text and word count have been written to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Define the input and output file paths
input_file = 'input.txt'
output_file = 'output.txt'

# Process the text
process_text(input_file, output_file)