"""
BiU - System Automation Script
Author: Muthana
Description:
This script demonstrates a basic automation task by listing
temporary files that can be cleaned from a system directory.
"""

import os

def list_temp_files(path):
    print(f"Scanning directory: {path}\n")
    try:
        files = os.listdir(path)
        if not files:
            print("No files found.")
            return

        for file in files:
            print(f"- {file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    temp_path = "/tmp" if os.name != "nt" else "C:\\Windows\\Temp"
    list_temp_files(temp_path)
