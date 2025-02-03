package java_blockchain;
import java.util.ArrayList;

public class Ledger {
    private ArrayList<String> ledgerEntries;
    
    public Ledger() {
        this.ledgerEntries = new ArrayList<>();
    }
    
    // Add an entry to the ledger
    public void addEntry(String timestamp, String dataType) {
        ledgerEntries.add("Timestamp: " + timestamp + " | Data Type: " + dataType);
    }
    
    // Get ledger entries
    public ArrayList<String> getEntries() {
        return ledgerEntries;
    }
}
