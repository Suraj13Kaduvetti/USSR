import os
import random

# Sample words for sentence generation
nouns = ['cat', 'dog', 'car', 'house', 'tree', 'computer', 'book', 'city', 'ocean', 'mountain']
verbs = ['jumps', 'runs', 'drives', 'flies', 'reads', 'writes', 'paints', 'sings', 'dances', 'thinks']
adjectives = ['quick', 'lazy', 'happy', 'sad', 'bright', 'dark', 'tall', 'short', 'beautiful', 'ugly']
adverbs = ['quickly', 'silently', 'happily', 'sadly', 'brightly', 'darkly']

# Function to generate random English-like sentences
def generate_random_sentences(num_sentences=10):
    sentences = []
    
    for _ in range(num_sentences):
        # Randomly select a structure for the sentence
        structure = random.choice([ 
            "{adjective} {noun} {verb} {adverb}.", 
            "{noun} {verb} {adjective} {noun}.", 
            "{noun} {verb} {adverb}.", 
            "{adjective} {noun} {verb}.",
        ])
        
        # Fill in the structure with random words
        sentence = structure.format(
            noun=random.choice(nouns).capitalize(),
            verb=random.choice(verbs),
            adjective=random.choice(adjectives),
            adverb=random.choice(adverbs)
        )
        
        sentences.append(sentence)
    
    return ' '.join(sentences)

# Function to write random text to a file
def create_random_text_file(file_name, num_sentences=10):
    random_text = generate_random_sentences(num_sentences)
    with open(file_name, 'w') as file:
        file.write(random_text)

# Create three files with random data
def create_multiple_files(num_files=3, num_sentences=10):
    for i in range(1, num_files + 1):
        file_name = f'input_{i}.txt'
        
        # Check if the file exists, if not, create it with random sentences
        if os.path.exists(file_name):
            print(f"File {file_name} is already present.")
        else:
            create_random_text_file(file_name, num_sentences)
            print(f"File {file_name} created successfully with {num_sentences} random English-like sentences!")

# Create three files with random sentences
create_multiple_files(num_files=3, num_sentences=10)
