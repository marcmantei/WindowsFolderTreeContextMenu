import winreg

def remove_context_menu_entry_for_current_user():
    """
    Removes the context menu entry that was added for the current user.

    The entry was added for folders, and when clicked, it ran the "tree" command in 
    the right-clicked folder and output the result into a text file in the parent 
    directory. This function removes that entry.
    """
    # Accessing the registry key for folder context menu entries for the current user.
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\\Classes\\Directory\\shell', 0, winreg.KEY_ALL_ACCESS)

    # Deleting the key for our custom command.
    winreg.DeleteKey(key, 'FolderTreeCommand\\command')
    winreg.DeleteKey(key, 'FolderTreeCommand')

    # Closing the key to write changes and free up system resources.
    winreg.CloseKey(key)

if __name__ == "__main__":
    remove_context_menu_entry_for_current_user()
