from tools import *
from tkinter import *
frm =form("600x600")

fr1=frame(frm)
fr1.pack(pady=5)
fr2=frame(frm)
fr2.pack(pady=5)
radio(frm,"male").pack()
label(fr2,"name").pack(pady=5)
bgall(frm,"lightblue")
fontall(frm,"None 20")
fgall(frm,"navy")

bgall(fr2,"red")
fontall(fr2,"None 20")
fgall(fr2,"navy")

frm.mainloop()
