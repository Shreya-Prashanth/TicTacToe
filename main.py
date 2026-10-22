import tkinter #tk - interface (graphic user interface) library)

def set_tile(row,column):
  pass

def new_game():
  pass
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
label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
  for column in range(3):
    board[row][column]=tkinter.Button(frame,text="",font=("Consolas",50,"bold"),background=color_gray,foreground=color_blue,width=4,height=1,command=lambda row=row,column=column:set_tile(row,column))

    board[row][column].grid(row=row+1,column=column)
button=tkinter.Button(frame,text="restart",font=("Consolas",20),background=color_gray,foreground="white",command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")

frame.pack() #pack frame
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
window_width=window.winfo_screenwidth()
window_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


                                                          
window.mainloop()
