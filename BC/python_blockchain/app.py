import tkinter as tk
from tkinter import messagebox
from blockchain import Blockchain

class BlockchainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain App")
        self.blockchain = Blockchain()
        
        self.data_entry = tk.Entry(root)
        self.data_entry.pack()

        self.add_block_button = tk.Button(root, text="Add Block", command=self.add_block)
        self.add_block_button.pack()

        self.view_ledger_button = tk.Button(root, text="View Ledger", command=self.view_ledger)
        self.view_ledger_button.pack()

        self.close_button = tk.Button(root, text="Close Program", command=self.close_program)
        self.close_button.pack()

    def add_block(self):
        data = self.data_entry.get()
        if data:
            self.blockchain.add_new_block(data)
            messagebox.showinfo("Success", "Block added successfully!")
            self.data_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter some data.")

    def view_ledger(self):
        ledger = self.blockchain.get_ledger()
        ledger_window = tk.Toplevel(self.root)
        ledger_window.title("Ledger")
        
        ledger_text = tk.Text(ledger_window, width=80, height=20)
        ledger_text.pack()
        
        for entry in ledger:
            ledger_text.insert(tk.END, f"Timestamp: {entry['Timestamp']}, DataType: {entry['DataType']}, Data: {entry['Data']}\n")

    def close_program(self):
        self.blockchain.save_ledger_to_excel()  # Save ledger before closing
        messagebox.showinfo("Exit", "Data saved. Program is closing.")
        self.root.quit()


# Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = BlockchainApp(root)
    root.mainloop()
