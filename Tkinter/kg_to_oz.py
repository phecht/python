''' Converts to kg to oz, lbs and grams '''
from tkinter import Tk, Button, Entry, Text, Label, StringVar, END

WINDOW = Tk()

# 1 kg = 35.27392 oz

def kg_to_oz():
    ''' kg_to_oz converts kg to oz. '''
    print('km_to_miles')
    print(ENTERED_KG.get())
    kg_converted = float(ENTERED_KG.get())
    oz_converted = kg_converted * 35.27392
    g_converted = kg_converted * 1000
    lb_converted = oz_converted / 16
    TEXT_OZ.delete(1.0, END)
    TEXT_OZ.insert(END, oz_converted)
    TEXT_G.delete(1.0, END)
    TEXT_G.insert(END, g_converted)
    TEXT_LB.delete(1.0, END)
    TEXT_LB.insert(END, lb_converted)


BUTTON_CONVERT = Button(WINDOW, text="Convert", command=kg_to_oz)
BUTTON_CONVERT.grid(row=0, column=0)

LABEL_KG = Label(WINDOW, text="KG")
LABEL_KG.grid(row=0, column=1)

ENTERED_KG = StringVar()
ENTRY_KG = Entry(WINDOW, textvariable=ENTERED_KG)
ENTRY_KG.grid(row=0, column=2)

LABEL_G = Label(WINDOW, text="GM:")
LABEL_G.grid(row=1, column=0)

LABEL_OZ = Label(WINDOW, text="OZ:")
LABEL_OZ.grid(row=1, column=1)

LABEL_LB = Label(WINDOW, text="LB:")
LABEL_LB.grid(row=1, column=2)

TEXT_G = Text(WINDOW, height=1, width=20)
TEXT_G.grid(row=2, column=0)

TEXT_OZ = Text(WINDOW, height=1, width=20)
TEXT_OZ.grid(row=2, column=1)

TEXT_LB = Text(WINDOW, height=1, width=20)
TEXT_LB.grid(row=2, column=2)

WINDOW.mainloop()
