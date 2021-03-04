from tkinter import *
import requests

def temp():
    city=ent.get()
    key = 'b4a76dfcc88a260b880967b0d6bdffe7'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'imperial'}
    result = requests.get(url, params=params)
    temp = result.json()
    faren = temp["main"]["temp"]
    cels = round((faren-32)*(5/9))
    lab['text'] = f'{str(temp["name"])}: {cels}C'

root=Tk()
root.title('Temperature')
root.geometry('300x250')
root.wm_attributes('-alpha', 0.7)
root.resizable(width=False, height=False)

frame1 = Frame(root, bg='yellow')
frame1.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.3)

frame2 = Frame(root, bg='yellow')
frame2.place(relx=0.15, rely=0.6, relwidth=0.7, relheight=0.1)

ent = Entry(frame1, font=30)
ent.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.35)

but = Button(frame1, text='Find out the temperature', bg='white', command=temp)
but.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.35)

lab = Label(frame2, bg='yellow', fg='black', font=10)
lab.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.55)

root.mainloop()