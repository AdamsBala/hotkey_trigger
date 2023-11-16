from ahk import AHK
import time

ahk = AHK()


def find_window(title, run_cmd):
    # Check if the Windows Terminal is running
    win = ahk.find_window(title=title)
    if win is None:
        # If Windows Terminal is not running, start it
        print(run_cmd)
        ahk.run_script(run_cmd)  # Open windows terminal
        print(run_cmd)
        time.sleep(1)

    # Bring Windows Terminal to the foreground
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
        if user_input in command_dictionary:
            print(f"Starting Process: {user_input}")
            command_dictionary[user_input]()
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

command_dictionary = {
    "notepad": start_notepad,
    "vagrantup": vagrant_up,
    "vagrantssh": vagrant_ssh
}

# start the hotkey process thread
ahk.start_hotkeys()
ahk.block_forever()
