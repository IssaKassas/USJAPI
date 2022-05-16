from tkinter import TOP, Button, Canvas, Label, OptionMenu, StringVar, Tk, Toplevel
from PIL import ImageTk, Image

Countries = [
    "Lebanon",
    "Egypt",
    "Yemen",
    "Morocco",
    "United Arab Emirates",
    "Oman",
    "Saudi Arabia",
    "Bahrain",
    "Syria",
    "Qatar",
    "Kuwait",
    "Algeria"
    ]

def covid19(api : str):

    def back():
        covidRoot.destroy()
        
    def country():
        choiceCountry = countryVariable.get()
        return choiceCountry
    
    def plotCountry():
        from PlotingGraph import plotLine
        plotLine(country())
            
    def drawPie():
        from PlotingGraph import plotPie
        plotPie()
    
    covidRoot = Toplevel()
    covidRoot.geometry("800x600")
    #covidRoot.attributes('-fullscreen', True)
        
    bg = ImageTk.PhotoImage(Image.open("Covid-19.jpg"))

    canvas = Canvas(covidRoot , width = 900 , height = 600)
    canvas.create_image(0, 0, image = bg , anchor = "nw")
    
    label = Label(
        canvas,
        text = api,
        font = ('bold' , 23),
        fg='#fff',
        bg = "#000"
    )
    
    countryVariable = StringVar(covidRoot)
    countryVariable.set(Countries[0])
    
    optionsCountries = OptionMenu(
        canvas,
        countryVariable,
        *Countries
    )
    optionsCountries.config(bg = "black" , fg = "#f5f5f5")
    optionsCountries["menu"].config(bg = "#f5f5f5" , fg = "#000")
    
    pieButton = Button(
        canvas,
        text = "Pie Char",
        bg = 'black',
        fg = "#fff",
        activebackground = 'white',
        activeforeground = 'black',
        font = ('Times', 16),
        padx = 10,
        pady = 10,
        command = drawPie
    )
    
    view = Button(
        canvas,
        text = "View Data",
        bg = 'black',
        fg = "#fff",
        activebackground = 'white',
        activeforeground = 'black',
        font = ('Times', 16),
        padx = 10,
        pady = 10,
        command = plotCountry
    )
    
    backBttn = Button(
        canvas,
        text = 'back',
        bg = 'black',
        fg = "#fff",
        activebackground = 'white',
        activeforeground = 'black',
        font = ('Times', 16),
        padx = 10,
        pady = 10,
        command = back
    )
    
    canvas.pack(side = TOP , fill = "both", expand = True)
    label.pack(pady = 30 , side = TOP)
    optionsCountries.pack(pady = 30 , side = TOP)
    pieButton.pack(pady = 30 , side = TOP , padx = 20)
    view.pack(pady = 30 , side = TOP , padx = 20)
    backBttn.pack(pady = 30 , side = TOP)
    
    covidRoot.mainloop()
    
# covid19('Covid 19')