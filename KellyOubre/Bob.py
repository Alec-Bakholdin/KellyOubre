from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

with open("Names.txt", "r") as file:
    file_contents = file.read()

names = file_contents.split("\n")
target_index = -1

def print_names(names):
    global target_index
    for name in names:
        is_target = target_index >= 0 and target_index < len(names) and name == names[target_index]
        print("{:<2}{:<5}".format(">" if is_target else "", name))


print_names(names)

#
# handle keypresses
#
def on_press(key):
    global target_index
    # move the targert index (increase/move down on down arrow and decrease/move up on up arrow)
    if key == Key.down:
        target_index = 0 if target_index < 0 or target_index >= len(names) - 1 else target_index + 1
    elif key == Key.up:
        target_index = len(names) - 1 if target_index == 0 else target_index - 1

    print("\n\n\n\n\n\n\n\n\n")
    print_names(names)
    
    # press control f and type target name
    if key == Key.down or key == Key.up:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('f')
            keyboard.release('f')
        keyboard.type(names[target_index])
        


            

    if(key == Key.f10):
        print("Terminating program")
        return False


#
# handle key release
#
def on_release(key):
    return True

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
