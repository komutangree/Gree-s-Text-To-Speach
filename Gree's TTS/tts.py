from tkinter import *
import pyttsx3
from tkinter import filedialog as fd




root = Tk()
root.title("Gree's Text To Speach")
#root.filename = fd.askopenfile(initialdir="/convertedmp3", title="Select a folder to save")
engine = pyttsx3.init()

e = Entry(root)
e.pack()
e.get() 

def say():
    say = e.get()
    engine.say(say)
    engine.runAndWait()
    succes1 = Label(root, text="Succesfully Tested")
    succes1.pack()

def say2():
    say2 = e.get()
    engine.save_to_file(say2, 'Converted_By_Gree.mp3')
    engine.runAndWait()
    succes = Label(root, text="Succesfully Downloaded as mp3 to the path where this program exists")
    succes.pack()
    
    


Download = Button(root, text="Test", command = say)
Download.pack()
Download2= Button(root, text="Download as MP3", command = say2)
Download2.pack()


root.mainloop()
