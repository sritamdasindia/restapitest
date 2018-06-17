
import requests 
from tkinter import *
import json

id = None

def fun ():
        data.configure(text = "Loading your data.. ")
        id = int(field.get())
        r = requests.get("https://reqres.in/api/users/{}".format(id))
        response_text = json.loads(r.text)
        firstname = response_text["data"]["first_name"]
        print(firstname)
        data . configure ( text = firstname )
   

window = Tk()

field = Entry(window )
field.pack()
data = Label( window , text = 'No Search Yet...')
data . pack()


okay = Button( window , text = 'Okay', command = fun )
okay . pack() 

window . mainloop() 
