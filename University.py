from tkinter import (BOTH, LEFT, RIGHT, VERTICAL, Y, 
                    Button , Frame, Label, Listbox, Scrollbar, Tk, Toplevel)
from tkinter.messagebox import showinfo

def univeristy():
    def back():
        univRoot.destroy()
        
    def selected_item():
        for item in listbox.curselection():
            txt = listbox.get(item)
            l = txt.split('-')
            showinfo(l[1] , l[2])
                
    univRoot = Toplevel()
    univRoot.title('Univerities of Countries')
    univRoot.geometry('900x800')
    #banksRoot.attributes('-fullscreen' , True)
    univRoot.config(bg='#4A7A8C')

    label = Label(
        univRoot,
        text = "Universities of Arabic Countries",
        bg = "#4A7A8C",
        font = ('Arial' , 18)
        )
    label.pack(pady = 8)

    frame = Frame(univRoot)
    frame.pack(expand = True , fill = BOTH , padx = 20 , pady = 12)

    framebtn = Frame(univRoot , bg = "#4A7A8C")
    framebtn.pack()

    select  = Button(
        framebtn,
        text = 'Get Email',
        bg = 'black',
        font = (14),
        fg = 'white',
        command = selected_item
    )
    select.pack(side = LEFT , padx = 10)

    backbtn  = Button(
        framebtn,
        text = 'Back',
        bg = 'black',
        font = (14),
        fg = 'white',
        command = back
    )
    backbtn.pack(side = LEFT , padx = 10)

    listbox = Listbox(frame , font = ('Arial' , 15) , fg  = '#111111')
    listbox.pack(expand = True , fill = BOTH , side = LEFT)

    scrollbar = Scrollbar(frame, orient = VERTICAL)
    scrollbar.pack(fill = Y, side = RIGHT)
  
    listbox.configure(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
    
    from PlotingGraph import countries
    i = 0
    for country in countries:
        for uinversity , page in zip(country.getUniversity()['universities'],country.getUniversity()['pages']):
            listbox.insert(i, f"{country.getUniversity()['country']}-{uinversity}-{page}")
            i += 1

    univRoot.mainloop()