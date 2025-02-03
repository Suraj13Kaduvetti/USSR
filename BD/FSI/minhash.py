import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix, save_npz
import os

# Function to read shingles from a file
def read_shingles(file_path):
    with open(file_path, 'r') as f:
        shingles = f.read().splitlines()
    return shingles

# Function to create input matrix from shingles
def create_input_matrix(shingles):
    shingles_set = set(shingles)
    shingle_index = {shingle: idx for idx, shingle in enumerate(shingles_set)}
    
    # Create binary matrix: rows are shingles, columns are documents
    matrix = np.zeros((len(shingles_set), len(shingles)), dtype=int)
    
    for col_idx, shingle in enumerate(shingles):
        matrix[shingle_index[shingle], col_idx] = 1  # Set presence of shingle as 1
    
    return matrix, shingle_index

# Function to compute Jaccard Similarity between two sets of shingles
def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union

# Function to pad matrices to the same size
def pad_matrices_to_equal_size(matrix_list):
    max_rows = max(matrix.shape[0] for matrix in matrix_list)
    max_cols = max(matrix.shape[1] for matrix in matrix_list)
    
    padded_matrices = []
    for matrix in matrix_list:
        # Pad rows and columns to match the largest dimensions
        padded_matrix = np.zeros((max_rows, max_cols), dtype=int)
        padded_matrix[:matrix.shape[0], :matrix.shape[1]] = matrix  # Copy original matrix into padded one
        padded_matrices.append(padded_matrix)
    
    return padded_matrices

# Function to compute similarity using the input matrix
def compute_similarity(matrix_list):
    # Ensure matrices have the same shape by padding them
    padded_matrices = pad_matrices_to_equal_size(matrix_list)
    
    num_files = len(padded_matrices)
    similarity_matrix = np.zeros((num_files, num_files))
    
    for i in range(num_files):
        for j in range(i, num_files):
            sim = np.sum(padded_matrices[i] == padded_matrices[j]) / padded_matrices[i].shape[0]
            similarity_matrix[i, j] = sim
            similarity_matrix[j, i] = sim
    
    return similarity_matrix

# Function to write a matrix to a file
def write_matrix_to_file(matrix, file_path):
    with open(file_path, 'w') as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

# Function to plot a matrix
def plot_matrix(matrix, title, filename):
    plt.figure(figsize=(8, 8))
    plt.imshow(matrix, cmap='viridis', aspect='auto')
    plt.colorbar()
    plt.title(title)
    plt.xlabel('Documents')
    plt.ylabel('Shingles')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Function to save the matrix in Matrix Market format
def save_matrix_market(matrix, filename):
    sparse_matrix = coo_matrix(matrix)  # Convert to COO format for sparse matrix representation
    save_npz(filename, sparse_matrix)  # Save in Matrix Market format (.npz)
    print(f"Matrix saved as {filename}")

# Main function to execute all steps
def main():
    # Create directories for outputs
    output_dirs = {
        'input_matrices': 'output/input_matrices',
        'similarity_matrices': 'output/similarity_matrices',
        'matrix_plots': 'output/matrix_plots',
        'matrix_market': 'output/matrix_market'
    }

    for directory in output_dirs.values():
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Step 1: Read shingles from all input files
    char_shingles_1 = read_shingles('character_input_1.txt')
    char_shingles_2 = read_shingles('character_input_2.txt')
    char_shingles_3 = read_shingles('character_input_3.txt')
    
    word_shingles_1 = read_shingles('word_input_1.txt')
    word_shingles_2 = read_shingles('word_input_2.txt')
    word_shingles_3 = read_shingles('word_input_3.txt')

    # Step 2: Create input matrices for all files
    char_matrix_1, _ = create_input_matrix(char_shingles_1)
    char_matrix_2, _ = create_input_matrix(char_shingles_2)
    char_matrix_3, _ = create_input_matrix(char_shingles_3)
    
    word_matrix_1, _ = create_input_matrix(word_shingles_1)
    word_matrix_2, _ = create_input_matrix(word_shingles_2)
    word_matrix_3, _ = create_input_matrix(word_shingles_3)

    # Step 3: Save input matrices to file
    write_matrix_to_file(char_matrix_1, os.path.join(output_dirs['input_matrices'], 'char_matrix_1_input.txt'))
    write_matrix_to_file(char_matrix_2, os.path.join(output_dirs['input_matrices'], 'char_matrix_2_input.txt'))
    write_matrix_to_file(char_matrix_3, os.path.join(output_dirs['input_matrices'], 'char_matrix_3_input.txt'))
    
    write_matrix_to_file(word_matrix_1, os.path.join(output_dirs['input_matrices'], 'word_matrix_1_input.txt'))
    write_matrix_to_file(word_matrix_2, os.path.join(output_dirs['input_matrices'], 'word_matrix_2_input.txt'))
    write_matrix_to_file(word_matrix_3, os.path.join(output_dirs['input_matrices'], 'word_matrix_3_input.txt'))

    # Step 4: Create similarity matrix across the three character and word matrices
    char_similarity_matrix = compute_similarity([char_matrix_1, char_matrix_2, char_matrix_3])
    word_similarity_matrix = compute_similarity([word_matrix_1, word_matrix_2, word_matrix_3])

    # Step 5: Save similarity matrices to file
    write_matrix_to_file(char_similarity_matrix, os.path.join(output_dirs['similarity_matrices'], 'char_similarity_matrix.txt'))
    write_matrix_to_file(word_similarity_matrix, os.path.join(output_dirs['similarity_matrices'], 'word_similarity_matrix.txt'))

    # Step 6: Plot similarity matrices
    plot_matrix(char_similarity_matrix, 'Character Similarity Matrix', os.path.join(output_dirs['matrix_plots'], 'char_similarity_plot.png'))
    plot_matrix(word_similarity_matrix, 'Word Similarity Matrix', os.path.join(output_dirs['matrix_plots'], 'word_similarity_plot.png'))

    # Step 7: Save similarity matrices in Matrix Market format
    save_matrix_market(char_similarity_matrix, os.path.join(output_dirs['matrix_market'], 'char_similarity_matrix.mm'))
    save_matrix_market(word_similarity_matrix, os.path.join(output_dirs['matrix_market'], 'word_similarity_matrix.mm'))

    print("Similarity matrices generated and saved.")

if __name__ == '__main__':
    main()
