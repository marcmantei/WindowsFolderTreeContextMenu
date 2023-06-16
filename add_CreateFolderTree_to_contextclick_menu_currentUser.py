import winreg

def add_context_menu_entry_for_current_user():
    """
    Adds a context menu entry in Windows Explorer for the current user only.

    The entry is added for folders, and when clicked, it runs the "tree" command in 
    the right-clicked folder and outputs the result into a text file in the parent 
    directory.
    """
    # Accessing the registry key for folder context menu entries for the current user.
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\\Classes\\Directory\\shell', 0, winreg.KEY_SET_VALUE)

    # Creating a new key for our custom command.
    cmd_key = winreg.CreateKey(key, 'FolderTreeCommand')

    # Setting the default value for the key, which will be the name of the context menu entry.
    winreg.SetValue(cmd_key, '', winreg.REG_SZ, 'Create Directory Tree')

    # Creating a key for the command that will be run.
    cmd_sub_key = winreg.CreateKey(cmd_key, 'command')

    # Setting the value for the command key.
    # The '%1' is a placeholder for the folder path.
    command = 'cmd.exe /c tree "%1" /A /F > "%1"\\..\\listing.txt'
    winreg.SetValue(cmd_sub_key, '', winreg.REG_SZ, command)

    # Closing the keys to write changes and free up system resources.
    winreg.CloseKey(cmd_sub_key)
    winreg.CloseKey(cmd_key)
    winreg.CloseKey(key)

if __name__ == "__main__":
    add_context_menu_entry_for_current_user()
