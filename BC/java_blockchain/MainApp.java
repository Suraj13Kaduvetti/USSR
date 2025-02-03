package java_blockchain;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainApp {
    private Blockchain blockchain;
    private Ledger ledger;
    
    public MainApp() {
        blockchain = new Blockchain();
        ledger = new Ledger();
        
        JFrame frame = new JFrame("Blockchain App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        
        // Input data and Add Block button
        JTextField dataInput = new JTextField();
        JButton addButton = new JButton("Add Block");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String data = dataInput.getText();
                blockchain.addBlock(data);
                ledger.addEntry(String.valueOf(System.currentTimeMillis()), data);
                dataInput.setText("");
            }
        });
        
        // Show Ledger button
        JButton showLedgerButton = new JButton("Show Ledger");
        showLedgerButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                displayLedger();
            }
        });
        
        // Show Visualization button
        JButton showVisualizationButton = new JButton("Show Blockchain Visualization");
        showVisualizationButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                BlockVisualizer.visualizeBlockchain(blockchain);
            }
        });
        
        // Close program button
        JButton closeButton = new JButton("Close Program");
        closeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ExcelExporter.exportLedgerToExcel(ledger.getEntries());
                System.exit(0);
            }
        });
        
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 1));
        panel.add(dataInput);
        panel.add(addButton);
        panel.add(showLedgerButton);
        panel.add(showVisualizationButton);
        panel.add(closeButton);
        
        frame.add(panel);
        frame.setVisible(true);
    }

    private void displayLedger() {
        StringBuilder ledgerText = new StringBuilder("Ledger:\n");
        for (String entry : ledger.getEntries()) {
            ledgerText.append(entry).append("\n");
        }
        JOptionPane.showMessageDialog(null, ledgerText.toString());
    }
    
    public static void main(String[] args) {
        new MainApp();
    }
}
