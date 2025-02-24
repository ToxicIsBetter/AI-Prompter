import pyautogui
import time
import pygetwindow as gw
import subprocess
import platform  # Import the platform module

# Number of tabs to type into
num_tabs = 5

# Prompt for user input
prompt = input("Enter the text to type into each tab's search bar: ")

# --- Brave Launch Logic (Platform-Specific) ---

def launch_brave():
    """Launches Brave browser based on the operating system."""
    system = platform.system()

    if system == "Windows":
        try:
            # Try the most common installation path
            subprocess.Popen([r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"])
            return
        except FileNotFoundError:
            try:
                # Try the 32-bit installation path (less common)
                subprocess.Popen([r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"])
                return
            except FileNotFoundError:
                try:  #Last attempt for a user-specific install
                    subprocess.Popen([f"{os.environ['LOCALAPPDATA']}\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"])
                    return
                except:
                    pass

        print("Error: Brave Browser executable not found.  Please ensure it's installed in a standard location.")
        exit()


    elif system == "Darwin":  # macOS
        try:
            subprocess.Popen(["/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"]) #Correct path
            return
        except FileNotFoundError:
            print("Error: Brave Browser.app not found in /Applications. Please ensure it's installed correctly.")
            exit()

    elif system == "Linux":
        #  Common ways to launch Brave on Linux (you might need to add more)
        try:
            subprocess.Popen(["brave-browser"])  # Try the standard command
            return
        except FileNotFoundError:
            try:
                subprocess.Popen(["/usr/bin/brave-browser"]) # Try explicit path
                return
            except FileNotFoundError:
                print("Error: Brave Browser executable not found. Please ensure it's installed and in your PATH.")
                exit()

    else:
        print(f"Unsupported operating system: {system}")
        exit()

# Function to check if Brave is open
def is_brave_open():
    return any("Brave" in window.title for window in gw.getWindowsWithTitle('Brave'))

# Launch Brave if it's not open
if not is_brave_open():
    print("Brave is not running. Launching Brave now...")
    launch_brave()
    time.sleep(5)  # Wait a few seconds for Brave to launch, increased for slower systems


# --- Focus Brave and Prepare ---

def focus_brave():
    """Focuses the Brave window (handles cases where it might be minimized)."""
    try:
        brave_windows = gw.getWindowsWithTitle('Brave')
        if not brave_windows:
            raise Exception("Brave window not found after launching.")

        brave_window = brave_windows[0]
        brave_window.restore()   # Restore if minimized
        brave_window.activate()  # Bring to foreground
        print("Brave focused successfully.")

    except Exception as e:
        print(f"Error focusing Brave: {e}.  Please ensure Brave is running and try again.  You may need to focus it manually.")
        exit()  # Exit if we can't focus Brave

focus_brave() #Now, focus the brave after we are sure that it launched.

time.sleep(2)    # Short pause after focusing

# --- Main Typing Loop ---

for i in range(num_tabs):
    print(f"Typing in tab {i+1}")

    # Type the prompt and submit
    pyautogui.write(prompt, interval=0.05)  # Slightly faster typing
    pyautogui.press('enter')
    time.sleep(1.5)  # Wait for search (adjust as needed)

    # Switch to the next tab (Ctrl + Tab)  *except* on the last tab
    if i < num_tabs - 1:
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)  # Wait for tab switch (faster)

print("Script execution completed.")