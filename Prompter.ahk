; AutoHotkey script to type a prompt into 5 Brave tabs and press Enter

; Prompt the user for input
InputBox, userInput, Enter Prompt, Type the text you want to search:

; Check if the user canceled the input
if (userInput = "")
{
    MsgBox, No input provided. Exiting script.
    ExitApp
}

; Activate Chrome window
WinActivate, ahk_exe brave.exe
WinWaitActive, ahk_exe brave.exe

; Loop through 5 tabs
Loop, 5
{
    ; Send the user's input to the active tab
    Send, %userInput%
    Sleep, 100 ; Small delay to ensure the text is typed

    ; Press Enter
    Send, {Enter}
    Sleep, 100 ; Small delay to allow the page to load

    ; Switch to the next tab (Ctrl + Tab)
    Send, ^+{Tab}
    Sleep, 100 ; Small delay to ensure the tab switch
}

MsgBox, Done! The prompt has been sent to 5 Brave tabs.
ExitApp