import tkinter as tk
from gui import BlockchainApp

def run_application():
    root = tk.Tk()
    app = BlockchainApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_application()
