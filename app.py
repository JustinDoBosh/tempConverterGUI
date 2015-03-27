from Tkinter import *
import tkMessageBox

#Our window class inherits from the Frame container widget
class Window(Frame):

    #initalize the Frame and the window
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()


    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit", command=self.quit)

        # placing the button on the window
        quitButton.place(x=0, y=0)

        #Create our vars we need in our app and make them integer vars
        convertedToFahrenheit = IntVar()
        convertedToCelsius = IntVar()
        tempInput = IntVar()
       
        # make the entry field and label for the user to enter in their text
        tLabel = Label(self, text="Enter Temperature")
        temp_entry = Entry(self, textvariable=tempInput)

        #Binds the label to the frame
        tLabel.pack( )
        #Binds the entry field to the frame
        temp_entry.pack()



        # Fahrenheit converter function 
        def convert_to_Fahrenheit():
            #gets the temp the user entered 
            CelsiusTemp = tempInput.get()
            #The temp conversion formula
            convertedToFahrenheit = (CelsiusTemp * 9/5) + 32
            #The message box pop up
            tkMessageBox.showinfo("Fahrenheit Temperature", str(convertedToFahrenheit) + " F")
        
        # Celsius converter function 
        def convert_to_Celsius():
            #gets the temp the user entered 
            FahrenheitTemp = tempInput.get()
            #The temp conversion formula
            convertedToCelsius = (FahrenheitTemp - 32) * 5/9
            #The message box pop up 
            tkMessageBox.showinfo("Celsius Temperature", str(convertedToCelsius) + " C")

        #The Fahrenheit btn that calls the convert_to_Fahrenheit function when clicked 
        convert_to_FahrenheitBtn = Button(root, text='convert to Fahrenheit', command=convert_to_Fahrenheit)
        #Binds the button to the frame
        convert_to_FahrenheitBtn.pack()

        #The Celsius btn that calls the convert_to_Celsius function when clicked 
        convert_to_CelsiusBtn = Button(root, text='convert to Celsius', command=convert_to_Celsius)
        #Binds the button to the frame
        convert_to_CelsiusBtn.pack()

            
#initialize Tkinter, we have to create a Tk root widget.
#This is an ordinary window, with a title bar and other decoration provided by your window manager. 
#You should only create one root widget for each program, and it must be created before any other widgets.
root = Tk()

#size of the window
root.geometry("400x300")

#we create the instance of the application class
app = Window(root)

#the window will not appear until we have entered the Tkinter event loop
root.mainloop()  