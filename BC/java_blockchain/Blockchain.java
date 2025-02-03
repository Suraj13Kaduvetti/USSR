package java_blockchain;
import java.util.ArrayList;

public class Blockchain {
    private ArrayList<Block> chain;
    
    // Constructor to initialize the blockchain
    public Blockchain() {
        this.chain = new ArrayList<>();
        createGenesisBlock();
    }
    
    // Create the first block (genesis block)
    private void createGenesisBlock() {
        chain.add(new Block("Genesis Block", "null"));
    }
    
    // Add a new block
    public void addBlock(String data) {
        String previousHash = chain.get(chain.size() - 1).getHash();
        Block newBlock = new Block(data, previousHash);
        chain.add(newBlock);
    }
    
    // Get all blocks
    public ArrayList<Block> getChain() {
        return chain;
    }
    
    // Get the number of blocks
    public int getBlockCount() {
        return chain.size();
    }
}
