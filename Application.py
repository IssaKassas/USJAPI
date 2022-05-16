from tkinter import Button, Canvas, Label, OptionMenu, StringVar, Tk
from tkinter.messagebox import askquestion, showinfo
from PIL import ImageTk, Image

APILIST = [
    "Covid 19",
    "Universities",
    "Population",
    "Data of countries"
    ]

def destroy(root : Tk):
    message = askquestion(title = 'Exit Application', message = 'Are you sure to close?')
    
    if message == 'yes':
       root.destroy()
    else:
        showinfo('Returning' , 'You will return')

def display_selected():
    choice = variable.get()
    return choice

def openTop(api : str):
    if api == APILIST[2]:
        def viewBar():
            from PlotingGraph import plotBar
            plotBar()
        viewBar()
        
    if api == APILIST[0]:
        from Covid19 import covid19
        covid19(api)
        
    if api == APILIST[1]:
        from University import univeristy
        univeristy()
        
    if api == APILIST[3]:
        import tableData
        tableData
        
app = Tk()
app.geometry("1000x600")
app.title("Countries API")
#app.attributes('-fullscreen', True)
app.config(bg = "#defde4")

bg = ImageTk.PhotoImage(Image.open("world.png"))

canvas = Canvas(app , width = 700 , height = 600)
canvas.create_image(0, 0, image = bg , anchor = "nw")

label1 = Label(
    canvas,
    text = "Countries API",
    font = ('bold' , 23),
    fg='#3e6787'
)

label2 = Label(
    canvas,
    text = "Choose an option to view data",
    font = ('bold' , 15),
    fg='#3e6787',
)

variable = StringVar(app)
variable.set(APILIST[0])

optionsAPI = OptionMenu(
    canvas,
    variable,
    *APILIST
    )

optionsAPI.config(bg = "#3e6787" , fg = "#f4f4bd")
optionsAPI["menu"].config(bg = "#3e6787" , fg = "#f4f4bd")

click = Button(
    canvas,
    text = "Click here",
    width = 20,
    height = 2,
    bg = '#3e6787',
    fg = "#b48b8b",
    activebackground = 'black',
    activeforeground = 'white',
    font = ('Times', 16),
    padx = 10,
    pady = 10,
    command = lambda : openTop(display_selected())
)

exit = Button(
    canvas,
    text = "Exit Application",
    width = 20,
    height = 2,
    bg = '#3e6787',
    fg = "#b48b8b",
    activebackground = 'black',
    activeforeground = 'white',
    font = ('Times', 16),
    padx = 10,
    pady = 10,
    command = lambda : destroy(app),
)

canvas.pack(side = "top", fill = "both", expand = True)
label1.place(x = 950 , y = 50)
label2.place(x = 920 , y = 150)
optionsAPI.place(x = 1000 , y = 250)
click.place(x = 920 , y = 350)
exit.place(x = 920 , y = 500)

app.mainloop()