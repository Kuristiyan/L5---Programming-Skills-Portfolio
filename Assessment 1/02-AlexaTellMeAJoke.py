from tkinter import *
import random 


joke = Tk() # Creates the window
joke.title("Alexa, Tell Me A Joke!") # Window title
joke.geometry("1500x575") # Window size
joke.resizable(False, False) # Fixed window size
joke.configure(bg="#F7CACA") # Window background color

with open("randomJokes.txt", "r") as jokes_list: # Open .txt file for reading
    jokes = [] # Empty list to store the jokes
    for line in jokes_list: # Loops through each line in the file
        line = line.strip() # Removes any whitespaces from the line
        if "?" in line: # Checks if the line contains a question mark
            sections = line.split("?", 1) # Splits the line into two part at the first question mark
            setup = sections[0] + "?" # The first part of the joke, assumed as the setup
            punchline = sections[1] # The second part of the joke, assumed as the punchline
            jokes.append((setup, punchline)) # Adds the tuple to the jokes list


def tell_a_joke():
    global ongoing_joke # Sets up a global variable that stores current joke displayed
    ongoing_joke = random.choice(jokes) # Selects a random joke from the file
    stlabel.config(text=ongoing_joke[0]) # Updates the text of the label
    pl_button.config(state = "normal") # Enables the punchline button that can reveal the punchline of the displayed joke
    pllabel.config(text="Wanna know?") # Updates the text of the punchline label to ask the user if they want to know the punchline

def tell_the_punchline(): # Reveals the punchline
    pllabel.config(text=ongoing_joke[1]) # Updates the punchline label and reveals the punchline
    pl_button.config(state="disabled") # Disables the punchline button

titlel = Label(joke, text = "Alexa's Joke Generator", font = ("Arial Rounded MT Bold", 25), fg = "#C83232", bg = "#F7CACA") # Title Label
titlel.pack(pady = 20)

stlabel = Label(joke, text = "Input: Alexa, tell me a joke!", font = ("Arial Rounded MT Bold", 18), fg = "#C83232", bg = "#F7CACA") # Joke's setup Label
stlabel.place(x = 350, y = 150)

pllabel = Label(joke, font = ("Arial Rounded MT Bold", 18), fg = "#C83232", bg = "#F7CACA") # Joke's punchline label
pllabel.place(x = 350, y = 325)

stbutton = Button(joke, text = "Alexa, tell me a joke!", command = tell_a_joke, font = ("Arial Rounded MT Bold", 15), fg = "#4682B4", bd = 5) # Button that will display the setup of the joke
stbutton.place(x = 10, y = 150)

pl_button = Button(joke, text = "Tell the punchline!", command = tell_the_punchline, font = ("Arial Rounded MT Bold", 15), state = "disabled", fg = "#4682B4", bd = 5) # Button that will eventually display the punchline of the joke
pl_button.place(x = 10, y = 325)

qt_button = Button(joke, text = "Quit?", command = joke.quit, font = ("Arial Rounded MT Bold", 15), fg = "#4682B4", bd = 5) # Quit button that closes the program
qt_button.place(x = 10, y = 500)

ongoing_joke = None # Initializes stores the current joke during the session

joke.mainloop() # Runs the main window