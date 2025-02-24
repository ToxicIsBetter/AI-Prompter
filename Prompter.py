import pyautogui
import time
import pygetwindow as gw
import subprocess

# Number of tabs to type into
num_tabs = 5

# Prompt for user input
prompt = input("Enter the text to type into each tab's search bar: ")

# Function to check if Brave is open
def is_brave_open():
    return any("Brave" in window.title for window in gw.getWindowsWithTitle('Brave'))

# Launch Brave if it's not open
if not is_brave_open():
    print("Brave is not running. Launching Brave now...")
    try:
        subprocess.Popen("brave")  # Open Brave (works if Brave is in system PATH)
        time.sleep(5)  # Wait a few seconds for Brave to launch
    except Exception as e:
        print(f"Failed to launch Brave: {e}")
        exit()

# Ensure Brave is open and give time to prepare
print("Attempting to focus Brave...")
time.sleep(5)

# Focus Brave window
try:
    brave_windows = gw.getWindowsWithTitle('Brave')
    if not brave_windows:
        raise Exception("Brave window not found after launching.")
    
    brave_window = brave_windows[0]  # Pick the first Brave window
    brave_window.restore()  # Restore in case it's minimized
    brave_window.activate()  # Focus the Brave window
    print("Brave focused successfully.")
except Exception as e:
    print(f"Error focusing Brave: {e}. Please focus it manually.")
time.sleep(9)  # Wait for focus

# Loop to type into each existing tab
for i in range(num_tabs):
    print(f"Typing in tab {i+1}")

    # Type the prompt and submit
    pyautogui.write(prompt, interval=0.1)
    pyautogui.press('enter')
    time.sleep(1)  # Wait for search to process
    
    # Switch to next tab (Ctrl + Tab)
    if i < num_tabs - 1:
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(1)  # Wait for tab switch

print("Script execution completed.")
