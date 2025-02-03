import tkinter as tk

# Sample Block class


# Function to visualize blocks
def visualize_blocks(blockchain, canvas):
    # Set the starting y-position for the first block in the graph
    x_start = 50  # Starting x-coordinate
    y_start = 50  # Starting y-coordinate
    y_gap = 200   # Gap between blocks vertically (you can adjust it)

    # Iterate over the blockchain and draw blocks in a graph-like manner
    for idx, block in enumerate(blockchain.get_chain()):
        # Draw a rectangle for each block
        x1 = x_start
        y1 = y_start + idx * y_gap
        x2 = x1 + 200  # Width of the block (adjust as necessary)
        y2 = y1 + 100  # Height of the block (adjust as necessary)
        
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
        
        # Display the timestamp text in the middle of the block
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(block.timestamp), fill="white", font=("Arial", 10))

# Set up the Tkinter root window and canvas
root = tk.Tk()
root.title("Blockchain Visualization")

canvas = tk.Canvas(root, width=500, height=1000)
canvas.pack()

# Create a sample blockchain and add blocks
blockchain = Blockchain()
blockchain.add_block(Block("2025-01-01 12:00", "Data Block 1"))
blockchain.add_block(Block("2025-01-02 13:00", "Data Block 2"))
blockchain.add_block(Block("2025-01-03 14:00", "Data Block 3"))
blockchain.add_block(Block("2025-01-04 15:00", "Data Block 4"))

# Visualize the blockchain
visualize_blocks(blockchain, canvas)

# Start the Tkinter mainloop
root.mainloop()
