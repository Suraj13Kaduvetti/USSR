package java_blockchain;
import java.security.MessageDigest;
import java.util.Date;

public class Block {
    private String previousHash;
    private String hash;
    private String data;
    private long timestamp;
    private String selfAddress;
    
    // Constructor for the first block
    public Block(String data, String previousHash) {
        this.previousHash = previousHash;
        this.data = data;
        this.timestamp = new Date().getTime();
        this.selfAddress = Integer.toHexString(this.hashCode()); // Simple self address
        this.hash = calculateHash();
    }
    
    // Method to calculate the hash
    public String calculateHash() {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            String input = previousHash + data + timestamp + selfAddress;
            byte[] hashBytes = digest.digest(input.getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                hexString.append(String.format("%02x", b));
            }
            return hexString.toString();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    
    // Getters and Setters
    public String getHash() { return hash; }
    public String getPreviousHash() { return previousHash; }
    public String getData() { return data; }
    public long getTimestamp() { return timestamp; }
    public String getSelfAddress() { return selfAddress; }
}
