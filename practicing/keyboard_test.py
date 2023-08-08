import keyboard
while True:
    try:
        if keyboard.is_pressed('a'):
            print("you pressed space")
            break
    except:
        break