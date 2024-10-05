import pyperclip
import pyautogui
import time
import keyboard

def type_clipboard_contents():
    # Wait for 1 second before typing
    time.sleep(0.5)

    # Get the clipboard contents
    clipboard_text = pyperclip.paste()

    # Type out the clipboard contents
    for char in clipboard_text:
        pyautogui.typewrite(char, interval=0.01) # Reduced delay to 0.01 seconds
        # time.sleep(0.01) # Uncomment this line if you want to use the sleep method instead
    
    # Wait for 0.5 seconds before exiting
    time.sleep(0.5)

# Set the keybind to activate the script
keyboard.add_hotkey('alt+/', type_clipboard_contents)

# Run the script in the background
print("Script is running. Press Alt+/ to type out the clipboard contents.")
keyboard.wait()