import speech_recognition as sr
from tkinter import *
def n1():
    global e1
    r=sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listning...")
        audio=r.listen(source)
        print("Recognizing....")
    tmp=r.recognize_google(audio)
    num = int(tmp.replace(" ", ""))
    print(num)
    e1.insert(0,str(num))





global e1

w= Tk()

w.title("Calculator")
Label(w, text='First Number').grid(row=0)
Label(w, text='Second Number').grid(row=1)
e1=Entry(w)
e1.grid(row=0, column=1)
e2=Entry(w)
e2.grid(row=1, column=1)
b1=Button(w,text="Speak!",command=n1)
b1.grid(column=3,row=0)
b2=Button(w,text="Speak!")
b2.grid(column=3,row=1)
"""
r=sr.Recognizer()
mic = sr.Microphone()

with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listning...")
        audio=r.listen(source)
        print("Recognizing....")

tmp=r.recognize_google(audio)
print(tmp)
"""

w.mainloop()
