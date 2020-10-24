from tkinter import *

import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.title('stage_2')
root.geometry('750x325+300+250')
root.minsize(750, 325)
root.state('zoomed')
dataload = pd.read_excel('dataset.xlsx')


def yukle():
    global dataload
    print(dataload)
    visu = dataload.plot.scatter(x='a', y='b', rot=0)


def visual():
    global visu
    plt.show()


def Rk():
    pass


root.configure(bg='#5A4A88')

LoadButton = Button(root, text='Load', fg='white', bg='#3A225B', padx=10, pady=5, command=yukle)
LoadButton.pack()
LoadButton.place(relwidth=0.1, relheight=0.05, relx=0.20, rely=0.1)

VisuButton = Button(root, text='Visualize', fg='white', bg='#3A225B', padx=10, pady=5, command=visual)
VisuButton.pack()
VisuButton.place(relwidth=0.1, relheight=0.05, relx=0.45, rely=0.1)

RkButton = Button(root, text='R Square', fg='white', bg='#3A225B', padx=10, pady=5, command=Rk)
RkButton.pack()
RkButton.place(relwidth=0.1, relheight=0.05, relx=0.70, rely=0.1)

label = Label(root, text="VISUALISATION OF STAGE_2")
label.pack()
sahe = Frame(root, bg='#FFA115', padx=10, pady=5)
sahe.pack()
sahe.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.4)
root.mainloop()
