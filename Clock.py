# Designed and Developed by Muhammad Umair Yaqub.
# P A K I S T A N

from ctypes.wintypes import SIZE
import time
from tkinter import *
import tkinter as TK

class Drag ( TK.Tk ) :
    
    def __init__( self ) :
        
        super().__init__()
        super().overrideredirect( True )
        self._offsetx = 0
        self._offsety = 0
        super().bind( "<Button-1>" , self.clickwin )
        super().bind( "<B1-Motion>", self.dragwin )

    def dragwin ( self, event ) :
        x = super().winfo_pointerx() - self._offsetx
        y = super().winfo_pointery() - self._offsety
        super().geometry( f"+{x}+{y}" ) 

    def clickwin( self, event ):
        self._offsetx = super().winfo_pointerx() - super().winfo_rootx()
        self._offsety = super().winfo_pointery() - super().winfo_rooty()

window = Drag()

window.title("Clock")
window.geometry("170x120")
window.overrideredirect( 1 )
window.attributes('-alpha', 0.9)
window.eval( 'tk::PlaceWindow . center')

close_btn  = Label ( window, width = 50, height = 50, bg = "#ededed" )
close_btn.grid ( row = 1, column =  3 )
close        = Button ( close_btn, text = "✕", anchor='e', justify = LEFT, font = ('Roboto', 10, 'normal'), fg = "#737373", width = 2, height = 1, bd = 0, bg = "#ededed", cursor = "hand2", command = window.destroy).grid ( row = 1,   column = 3, padx = 2, pady = 1 )

Date         = Label ( window, font = ('Roboto', 15, 'normal'), fg = "#737373", bg = "#ededed", bd = 0, justify = LEFT )
Date.grid ( row = 1, column =  1 )
Time         = Label ( window, font = ('Roboto', 30, 'normal'), fg = "#737373", bg = "#ededed", bd=0, justify = LEFT )
Time.grid ( row = 2, column =  1 )
Meridiem     = Label ( window, font = ('Roboto', 13, 'normal'), fg = "#737373", bg = "#ededed", bd=0, justify = CENTER )
Meridiem.grid ( row = 2, column =  2 )

def date () :

    date_input = time.strftime( " %a, %d %b")
    time_input = time.strftime( "\n%#I:%M" )
    meridiem_input = time.strftime("\n\n\n %p")
    Date.config ( text = date_input )
    Time.config ( text = time_input)
    Meridiem.config ( text = meridiem_input.lower() )

date ()

window.mainloop()
