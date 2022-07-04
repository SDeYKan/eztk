# DEPENDENCIES
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

# todo: add treeview, image, combobox, progressbar, canvas?
# todo: addscrollbar() upgraded function
# todo: change nomenclature to add clarity

def ezvalue(object):
    if isinstance(object, (widgets.mk_listbox, widgets.mk_radiobuttons)):
        return object.getvar()
    if isinstance(object, (tk.Entry, tk.Text, tk.scrolledtext.ScrolledText)):
        return object.get("1.0","end-1c")
    else: 
        print("Wrong or not recognized object. Must include the object, not its variable, as argument! Supported objects:")
        print("[EZTK]: widgets.mk_listbox & widgets.mk_radiobuttons\n[TKINTER]: tkinter.Entry & tkinter.Text & tkinter.ScrolledText")
        return False

def ezplace(object, x, y, side, fill=None):
    # Place is the default method for an easy xy coords object placements
    # Because it can take longer than pack() or grid() to place correctly, it can be unconfortable for some
    # If you don't want to use it, you can either just overwrite it by using other method in the next line
    # You can add a side="" argument to change it for pack()
    # Grid needs too many arguments. You can still manually write it in a new line under the declaration!
    if not side:
        object.place(x=x, y=y)
    elif side:
        object.pack(side=side, fill=fill)

class widgets():
    # MAIN WINDOW
    def mkwindow(title="tk", size="852x480", bg="#FFFFFF", icon="", hResizable="False", wResizable="False", whenClosed=None):
        tk = Tk()
        tk.title(title)
        tk.geometry(size)
        tk.configure(bg=bg)
        tk.resizable(wResizable, hResizable)
        if icon:
            tk.iconbitmap(icon)
        if whenClosed:
            tk.protocol("WM_DELETE_WINDOW", whenClosed)
        return tk
    # PLAIN TEXT
    def mklabel(parent, text="Sample", x=0, y=0, side="", bg="#FFFFFF"):
        label = tk.Label(parent, text=text, bg=bg)
        ezplace(label, x, y, side)
        return label
    # SMALL INPUT BOX
    def mkentry(parent, var="", x=0, y=0, side="", bg="#FFFFFF"):
        entry = tk.Entry(parent, textvariable=var, bg=bg)
        ezplace(entry, x, y, side)
        return entry
    # SEPARATOR
    def mkseparator(parent, height=400, width=2, x=10, y=10):
        # ORIENTATION DOESN't WORK FOR SOME REASON SO USER CAN SPECIFY DIMENSIONS
        separator = ttk.Separator(parent)
        separator.place(height=height, width=width, x=x, y=y)
        return separator
    # SIMPLE BUTTON
    def mkbutton(parent, text="Sample", command="", width=15, height=5, x=0, y=0, side="", bg="#FFFFFF", activebg="#FFFFFF"):
        button = tk.Button(parent, text=text, width=width, height=height, command=command, bg=bg, activebackground=activebg)
        ezplace(button, x, y, side)
        return button
    # CHECKBOX
    def mkcheck(parent, variable, text="Sample", x=0, y=0, side="", bg="#FFFFFF", activebg="#FFFFFF"):
        check = tk.Checkbutton(parent, text=text, variable=variable, bg=bg, activebackground=activebg)
        ezplace(check, x, y, side)
        return check
    # LIST OF RADIO BUTTONS
    def mkradiobutton_multiple(parent, names=["Sample"], x=0, y=0, side="", clearx=0, cleary=20, bg="#FFFFFF", activebg="#FFFFFF"):
        # This will return a dictionary which contains: the buttons as tkinter objects, and the variable that stores which button of the same group is active
        variable = IntVar()
        buttons = []
        names = list(names)
        for i in range(len(names)):
            buttons[i] = tk.Radiobutton(parent, text=names[i], variable=variable, value = i, bg=bg, activebackground=activebg)
            ezplace(buttons[i], x+clearx*i, y+cleary*i, side=side)
        returned = {"variable": variable, "buttons": buttons}
        return returned
    def mkradiobutton_single(parent, name, variable, value, x=0, y=0, side="", bg="#FFFFFF", activebg="FFFFFF"):
        radiobutton = tk.Radiobutton(parent, text=name, variable=variable, value=value, bg=bg, activebackground=activebg)
        ezplace(radiobutton, x=x, y=y, side=side)
        return radiobutton
    # LISTBOX
    def mklistbox(parent, names=["Sample"], width=80, height=20, x=0, y=0, side="", bg="#FFFFFF"):
        listbox = tk.Listbox(parent, width=width, height=height, bg=bg)
        ezplace(listbox, x=x, y=y, side=side)
        list(names)
        for i in range(len(names)):
            listbox.insert(i, names[i])
        return listbox
    def modifylistbox(listbox, startposition=0, names=["Sample"], delete=[-1, -1]):
        # Can either replace single or pultiple entries starting from a specific position(with startposition and names[])
        # Or delete several entries with delete[] (can't do both) with delete, you need to pass a list with two indexes, like this: [first_index, last_index]
        # Both are included and the positions will remain empty (even though it will not be rendered blank on the GUI), for you to replace the spaces
        if delete[0] >= 0 and delete[1] >=0:
            listbox.delete(delete[0], delete[1])
        else:
            for i in range(len(names)):
                listbox.delete(startposition)
                listbox.insert(startposition, names[i])
                startposition += 1
        return listbox
    # BIG INPUT BOX
    def mktextbox(parent, x=0, y=0, width=50, height=50, side=""):
        textbox = Text(parent, width=width, height=height)
        ezplace(textbox, x, y, side)
        return textbox
    # BIG INPUT BOX WITH SCROLL BAR
    def mkscrolledtextbox(parent, x=0, y=0, width=50, height=50, side=""):
        scrolledbox = ScrolledText(parent, width=width, height=height)
        ezplace(scrolledbox, x, y, side)
        return scrolledbox
    # TOP VIEW MENU
    def mktopmenu(parent):
        menu = tk.Menu()
        parent.config(menu=menu)
        return menu
    def mkmenuentry(parent, name="Sample"):
        menu = tk.Menu()
        parent.add_cascade(label=name, menu=menu)
        return menu
    def mkmenuoption(parent, name="Sample", command=""):
        option = parent.add_command(label=name, command=command)  
        return option               
    def mkmenuseparator(parent):
        parent.add_separator()
    # SCROLL BAR
#    def mkscrollbar(parent, width=18, orient="vertical", fill="none", side="right"):
#        scrollbar = tk.Scrollbar(parent, orient=orient, width=width)
#        ezplace(scrollbar, x="", y="", side=side, fill=fill)
#        return scrollbar
    # FRAME
    def mkframe(parent, width=50, height=50, x=0, y=0, side="", bg="#EEEEEE"):
        frame = tk.Frame(parent, width=width, height=height, bg=bg)
        ezplace(frame, x=x, y=y, side=side)
        return frame
    # LABELED FRAME
    def mklabelframe(parent, text="Sample", width=50, height=50, x=0, y=0, side=""):
        labelframe = ttk.LabelFrame(parent, text=text, width=width, height=height)
        ezplace(labelframe, x, y, side)
        return labelframe
    # NOTEBOOK
    def mknotebook(parent, x=0, y=0, side=""):
        notebook = ttk.Notebook(parent)
        ezplace(notebook, x, y, side)
        return notebook
    def mktab(parent, name="Sample", width=50, height=50):
        tab = ttk.Frame(parent, width=width, height=height)
        parent.add(tab, text=name)
        return tab
if __name__ == "__main__":
    root = widgets.mkwindow()
    list = widgets.mklistbox(root, ["hola"])
    root.mainloop()