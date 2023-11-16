from ahk import AHK
import time

ahk = AHK()


def find_window(title, run_cmd):
    """
    Searches for a window with the specified title and brings it to the foreground.
    If the window is not found, executes a command to open the window.

    Parameters:
    title (str): The title of the window to search for.
    run_cmd (str): The command to execute if the window is not found.

    Returns:
    object: An object representing the found window, or None if the window is not found.
    """
    win = ahk.find_window(title=title)
    if win is None:
        ahk.run_script(run_cmd)
        time.sleep(1)

    win = ahk.find_window(title=title)
    return win


def process_user_input(command):
    win = find_window('ahk_exe WindowsTerminal.exe', 'Run wt')
    if win:
        win.activate()
        ahk.send_input(f'{command}\n')


def input_gui():
    user_input = ahk.input_box(prompt='Command:', title='Enter Command')
    if user_input:
        if user_input in predefined_commands:
            print(f"Starting Process: {user_input}")
            predefined_commands[user_input]()
        else:
            process_user_input(user_input)


def hotkey_triggered():
    input_gui()


def start_notepad():
    win = find_window('ahk_exe notepad++.exe', 'Run notepad++')
    if win:
        win.activate()
        ahk.send_input('^n')


def vagrant_up():
    win = find_window('ahk_exe WindowsTerminal.exe', 'Run wt')
    if win:
        win.activate()
        ahk.send_input('cd Z:\\VirtualBox\\\\Vagrant \n')
        ahk.send_input('vagrant up\n')


def vagrant_ssh():
    win = find_window('ahk_exe WindowsTerminal.exe', 'Run wt')
    if win:
        win.activate()
        ahk.send_input('cd Z:\\VirtualBox\\\\Vagrant \n')
        ahk.send_input('ssh vagrant@localhost -p 17122\n')
        time.sleep(10)
        ahk.send_input('vagrant\n')


# ALT + Z
ahk.add_hotkey('!z', callback=hotkey_triggered)

predefined_commands = {
    "notepad": start_notepad,
    "vagrantup": vagrant_up,
    "vagrantssh": vagrant_ssh
}

# start the hotkey process thread
ahk.start_hotkeys()
ahk.block_forever()
