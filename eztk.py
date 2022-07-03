# DEPENDENCIES
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

# todo: add treeview, add separator, add messagebox(if useful)
# todo: add a way to include a scrollbar to a widget
# todo: change nomenclature to add clarity
# todo: add a function to add listboxes and radiobuttons without the need for a parent object

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
    def mklistbox(parent, names=["Sample"], width=80, height=150, x=0, y=0, side="", bg="#FFFFFF"):
        listbox = tk.Listbox(parent, width=width, height=height, bg=bg)
        ezplace(listbox, x=x, y=y, side=side)
        list(names)
        for i in range(len(names)):
            listbox.insert(index=i, elements=names[i])
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
                listbox.insert(index=startposition, elements=names[i])
                startposition += 1
        return listbox
    # BIG INPUT BOX TODO: FIX CHANGE TO FUNCTION
    def mktextbox(self, x=0, y=0, width=50, height=50, side=""):
        return self.mk_textbox.make(self.tk, x, y, width, height, side)
    class mk_textbox():
        def make(parent, x, y, width, height, side):
            self = Text(parent, width=width, height=height)
            ezplace(self, x, y, side)
            return self
    # BIG INPUT BOX WITH SCROLL BAR TODO: FIX CHANGE TO FUNCTION
    def mkscrolledtextbox(self, x=0, y=0, width=50, height=50, side=""):
        return self.mk_scrolledtextbox.make(self.tk, x, y, width, height, side)
    class mk_scrolledtextbox():
        def make(parent, x, y, width, height, side):
            self = ScrolledText(parent, width=width, height=height)
            ezplace(self, x, y, side)
            return self
    # TOP VIEW MENU TODO: FIX CHANGE TO FUNCTION
    def mktopmenu(self):
        return self.mk_topmenu(self.tk)
    class mk_topmenu():
        def __init__(self, parent):
            self.menu = tk.Menu()
            parent.config(menu=self.menu)
        def mkentry(self, name="Sample"):
            return self.mk_entry(self, name)
        class mk_entry():
            def __init__(self, parent, name="Sample"):
                self.menu = tk.Menu()
                parent.menu.add_cascade(label=name, menu=self.menu)
            def mkentry(self, name="Sample"):
                nestedentry = mkwindow.mk_topmenu.mk_entry(self, name)
                return nestedentry
            def mkoption(self, name="Sample", command=""):
                return self.mk_option(self.menu, name, command)
            class mk_option():
                def __init__(self, parent, name, command):
                    parent.add_command(label=name, command=command)                 
            def mkseparator(self):
                return self.mk_separator(self.menu)
            class mk_separator():
                def __init__(self, parent):
                    parent.add_separator()
    def mkscrollbar(parent, width=18, orient="vertical", fill="none", side="right"):
        scrollbar = tk.Scrollbar(parent, orient=orient, width=width)
        ezplace(scrollbar, x="", y="", side=side, fill=fill)
        return scrollbar
#    # LABELED FRAME
#    def mklabelframe(self, name="Sample", width=50, height=50, x=0, y=0, side=""):
#        return self.mk_labelframe(self.tk, name, width, height, x, y, side)
#    class mk_labelframe(): # TODO: Add inheritance to be able to add widgets to this
#        def __init__(self, parent, name, width, height, x, y, side):
#            self.tk = ttk.Labelframe(parent, text=name, width=width, height=height)
#            ezplace(self.tk, x, y, side)
#    # NOTEBOOK
#    def mknotebook(self, x=0, y=0, side=""):
#        return self.mk_notebook(self.tk, x, y, side)
#    class mk_notebook():
#        def __init__(self, parent, x=0, y=0, side=""):
#            self.tk = ttk.Notebook(parent)
#            ezplace(self.tk, x, y, side)
#        def mktab(self, name="Sample", widht=50, height=50):
#            return self.mk_tab(self.tk, name, widht, height)
#        class mk_tab(): # TODO: Add inheritance to be able to add widgets to this
#            def __init__(self, parent, name, width, height):
#                self.tk = ttk.Frame(parent, width=width, height=height)
#                parent.add(self.tk, text=name)


class mkwindow(widgets):
    def __init__(self, title="tk", size="852x480", bg="#FFFFFF", icon="", hResizable="False", wResizable="False", whenClose=None):
        self.tk = Tk()
        self.tk.title(title)
        self.tk.geometry(size)
        self.tk.configure(bg=bg)
        self.tk.resizable(wResizable, hResizable)
        if icon:
            self.tk.iconbitmap(icon)
        if whenClose:
            self.tk.protocol("WM_DELETE_WINDOW", whenClose)
    # LABELED FRAME
    def mklabelframe(self, name="Sample", width=50, height=50, x=0, y=0, side=""):
        return self.mk_labelframe(self.tk, name, width, height, x, y, side)
    class mk_labelframe(widgets):
        def __init__(self, parent, name, width, height, x, y, side):
            self.tk = ttk.Labelframe(parent, text=name, width=width, height=height)
            ezplace(self.tk, x, y, side)
        def mklabelframe(self, name="Sample", width=50, height=50, x=0, y=0, side=""):
            return mkwindow.mk_labelframe(self.tk, name, width, height, x, y, side)
    # NOTEBOOK
    def mknotebook(self, x=0, y=0, side=""):
        return self.mk_notebook(self.tk, x, y, side)
    class mk_notebook():
        def __init__(self, parent, x=0, y=0, side=""):
            self.tk = ttk.Notebook(parent)
            ezplace(self.tk, x, y, side)
        def mktab(self, name="Sample", width=50, height=50):
            return self.mk_tab(self.tk, name, width, height)
        class mk_tab(widgets):
            def __init__(self, parent, name, width, height):
                self.tk = ttk.Frame(parent, width=width, height=height)
                parent.add(self.tk, text=name)
            def mknotebook(self, x=0, y=0, side=""):
                return mkwindow.mk_notebook(self.tk, x, y, side)