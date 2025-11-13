import pyperclip
import pyautogui
import keyboard
import time

def type_clipboard_contents():
    """
    Gets text from the clipboard and types it out.
    """
    try:
        # Give a tiny pause. This helps prevent the hotkey 
        # (e.g., the 'alt' key) from "sticking" or interfering.
        time.sleep(0.3) 
        
        # Get the text from the clipboard
        text_to_type = pyperclip.paste()
        
        # Type the text, just like before
        pyautogui.typewrite(text_to_type, interval=0.001)
        
    except Exception as e:
        print(f"Error while typing clipboard: {e}")

# --- Main Part of the Script ---

# 1. Register the hotkey. When 'alt+/' is pressed, 
#    it will call the 'type_clipboard_contents' function.
keyboard.add_hotkey('alt+/', type_clipboard_contents)

print("Hotkey listener started...")
print("Press 'Alt + /' to type your clipboard.")
print("\n(This window must stay open. Press 'Esc' to stop the script.)")

# 2. Keep the script running. 
#    It will wait until you press the 'esc' key to quit.
keyboard.wait('esc')

print("Script stopped.")
