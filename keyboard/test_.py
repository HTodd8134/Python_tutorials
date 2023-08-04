import keyboard

def press():
    while True:
        try:
            if keyboard.is_pressed("a"):
                return "a was pressed"
        except:
            break

print(press())

#seems to need administrator so needs sudo python on terminal