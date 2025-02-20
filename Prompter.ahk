; AutoHotkey v2 script to type a prompt into 4 Brave Browser tabs and press Enter

; Prompt the user for input
userInput := InputBox("Enter Prompt", "Type the text you want to search:").Value

; Check if the user canceled the input
if (userInput = "")
{
    MsgBox("No input provided. Exiting script.")
    ExitApp
}

; Activate Brave Browser window
if !WinActivate("ahk_exe brave.exe")
{
    MsgBox("Brave Browser is not open. Please open Brave and try again.")
    ExitApp
}
WinWaitActive("ahk_exe brave.exe")

; Loop through 4 tabs
Loop 4
{
    ; Send the user's input to the active tab
    Send(userInput)
    Sleep(100) ; Small delay to ensure the text is typed

    ; Press Enter
    Send("{Enter}")
    Sleep(100) ; Small delay to allow the page to load

    ; Switch to the next tab (Ctrl + Tab)
    Send("^+{Tab}")
    Sleep(100) ; Small delay to ensure the tab switch
}

MsgBox("Done! The prompt has been sent to 4 Brave Browser tabs.")
ExitApp