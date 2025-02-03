import networkx as nx
import matplotlib.pyplot as plt
from blockchain import Blockchain

def visualize_blockchain(blockchain):
    G = nx.DiGraph()

    # Create nodes and edges from blockchain data
    for block in blockchain.chain:
        G.add_node(block.index, label=block.data)
        if block.prev_hash:
            G.add_edge(block.prev_hash, block.self_hash)

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10)
    plt.show()

# Example usage:
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_new_block("First data")
    blockchain.add_new_block("Second data")
    visualize_blockchain(blockchain)
