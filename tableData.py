from tkinter.messagebox import showinfo
from turtle import bgcolor
from PIL import ImageTk, Image
from tkinter import CENTER, NO, RIGHT, VERTICAL, Y, Button, Label, Scrollbar, Tk, Toplevel, ttk
from PlotingGraph import countries

cols = ("name" , "currencies" , 'capital' , "region" ,"languages" , "latlng" ,
        "area" , 'population' , "timezones" , "continents" , "flags")


def back():
        table.destroy()

def tree(root : Toplevel):
    tree = ttk.Treeview(root, column = cols , show = "headings")
    
    for i in range(len(cols)):
        if i == 0:
            width = 80
        else:
            width = 120
        
        tree.column(f"#{i + 1}" , anchor = CENTER , stretch = NO , width = width)
        tree.heading(f"#{i + 1}" , text = cols[i])
    
    for country in countries:
        tree.insert('' , 'end' , values = country.getRow())
        
    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            showinfo(title = 'Information', message=','.join(str(v) for v in record))
            
    tree.bind('<<TreeviewSelect>>', item_selected)
    
    scroll = Scrollbar(root, orient = VERTICAL , command = tree.yview)
    tree.config(yscrollcommand = scroll.set)
    scroll.pack(side = RIGHT , fill = Y)
    
    style = ttk.Style()
    style.theme_use('clam')
    tree.pack(pady = 50)

table = Toplevel()
table.title("Countries")
# table.geometry("700x500")
table.attributes('-fullscreen' , True)
bgimg = ImageTk.PhotoImage(Image.open("countries.jpg"))
img = Label(table, image = bgimg)
img.place(x = 0 , y = 0)

label = Label(
    table,
    text = "Data of Countries",
    font = ('Arial' , 20),
    bg = '#b48b8b',
    fg = '#f4d4bd'
)
label.pack(pady = 20)

tree(table)

backBttn = Button(
    table,
    text = 'back',
    bg = '#b48b8b',
    fg = "#fff",
    activebackground = 'white',
    activeforeground = 'black',
    font = ('Times', 16),
    padx = 10,
    pady = 10,
    command = back
    )

backBttn.pack(pady = 30)
table.mainloop()


