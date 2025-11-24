import time
from datetime import datetime


INPUT_FILE = "uha-input.txt"
OUTPUT_DATA_FILE = "uha-output.txt"

def store_archive_entry(entry):
    """Store a single entry to the archive with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #Parse entry: "user,action" (no space)
    parts = entry.split(',', 1)
    
    if len(parts) == 2:
        user, action = parts
        formatted_entry = f"{timestamp} | {user} | {action}\n"
        
        with open(OUTPUT_DATA_FILE, "a") as f:
            f.write(formatted_entry)
        
    else:
        print(f"Warning: Invalid entry format: {entry}.") 
        print("Entry should be in the following format: user,action")

def clear_input_file():
    with open(INPUT_FILE, "w+") as f:
        f.write("")

def check_request_type(file):

    with open(file, "r+") as f:
        first_line = f.readline()
        
    #check for empty file (no requests incoming)
    if not(first_line.strip()):
        return 1

    elif(first_line == "erase"):
        f.write("")
        return 0

    #otherwise, this is archive input
    else:
        return first_line

def erase_archive_file():
    with open(OUTPUT_DATA_FILE, "w+") as f:
        f.write("")
        print("Archive erased.")

#checking input from main program
def read_input():
    while True:
        try: 
            with open(INPUT_FILE, "r+") as f:

                file_result = check_request_type(f)

                if file_result == 0:
                    erase_archive_file()

                elif file_result == 1:
                    return

                else:
                    #store input
                    store_archive_entry(file_result)

        except FileNotFoundError:
            print("Error: file not found")
            return
        
        time.sleep(1)



