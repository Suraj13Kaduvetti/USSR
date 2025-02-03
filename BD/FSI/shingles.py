import string

def generate_shingles_by_char(text, shingle_size):
    shingles = []
    for i in range(len(text) - shingle_size + 1):
        shingles.append(text[i:i + shingle_size])
    return shingles

def generate_shingles_by_word(text, shingle_size):
    words = text.split()
    shingles = []
    for i in range(len(words) - shingle_size + 1):
        shingles.append(' '.join(words[i:i + shingle_size]))
    return shingles

def remove_punctuation(text):
    # Create a translation table that removes punctuation
    return text.translate(str.maketrans('', '', string.punctuation))

def process_text_file(file_name, shingle_size=3):
    # Open and read the file content
    with open(file_name, 'r') as file:
        text = file.read()

    # Remove punctuation from the text
    cleaned_text = remove_punctuation(text)

    # Generate shingles for characters
    char_shingles = generate_shingles_by_char(cleaned_text, shingle_size)
    
    # Generate shingles for words
    word_shingles = generate_shingles_by_word(cleaned_text, shingle_size)

    # Save character-based shingles to character.txt
    with open(f'character_{file_name}', 'w') as char_file:
        for shingle in char_shingles:
            char_file.write(shingle + '\n')

    # Save word-based shingles to word.txt
    with open(f'word_{file_name}', 'w') as word_file:
        for shingle in word_shingles:
            word_file.write(shingle + '\n')

    # Display the shingles in the required format
    display_shingles(char_shingles, word_shingles)

def display_shingles(char_shingles, word_shingles):
    # Display the character shingles
    print("Character Shingles: {")
    print("[" + "], [".join(char_shingles) + "]")
    print("}")

    # Display the word shingles
    print("\nWord Shingles: {")
    print("[" + "], [".join(word_shingles) + "]")
    print("}")

def process_multiple_files(file_names, shingle_size=3):
    # Process each file
    for file_name in file_names:
        process_text_file(file_name, shingle_size)

# Example usage for multiple files
file_names = ['input_1.txt', 'input_2.txt', 'input_3.txt']  # Add your input files here
shingle_size = 3
process_multiple_files(file_names, shingle_size)
