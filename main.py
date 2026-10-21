import tkinter #tk - interface (graphic user interface) library)

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0,0,0],[0,0,0],[0,0,0]] #3x3 board
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

#window setup
window = tkinter.Tk() #create window
window.title("Tic Tac Toe") #window title
window.resizable(True,True) #window size cannot be changed
frame = tkinter.Frame(window) #create frame
label = tkinter.Label(frame, text=curr_player +"'s Turn", font=("Arial", 20),background = color_gray , foreground="white") #create label
label.pack() #pack label
frame.pack() #pack frame


window.mainloop()
