import os
import shutil
import pandas as pd
from ledger import Ledger

def save_ledger(ledger):
    ledger.save_to_excel("ledger.xlsx")
    print("Ledger saved to Excel.")

def delete_data():
    if os.path.exists("ledger.xlsx"):
        os.remove("ledger.xlsx")
        print("Ledger data deleted.")
