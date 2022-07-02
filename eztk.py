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
    # PLAIN TEXT
    def mklabel(self, text="Sample", x=0, y=0, side=""):
        return self.mk_label.make(self.tk, text, x, y, side)
    class mk_label():
        def make(parent, text, x, y, side):
            self = tk.Label(parent, text=text)
            ezplace(self, x, y, side)
            return self
    # SMALL INPUT BOX
    def mkentry(self, var="", x=0, y=0, side=""):
        return self.mk_entry.make(self.tk, var, x, y, side)
    class mk_entry():
        def make(parent, var, x, y, side):
            self = tk.Entry(parent, textvariable=var)
            ezplace(self, x, y, side)
            return self
    # SIMPLE BUTTON
    def mkbutton(self, text="Sample", command="", width=15, height=1, x=0, y=0, side=""):
        return self.mk_button.make(self.tk, text, command, width, height, x, y, side)
    class mk_button():
        def make(parent, text, command, width, height, x, y, side):
            self = tk.Button(parent, text=text, width=width, height=height, command=command)
            ezplace(self, x, y, side)
            return self
    # CHECKBOX
    def mkcheck(self, var, text="Sample", x=0, y=0, side="", bg="#FFFFFF", activebg="#FFFFFF"):
        return self.mk_check.make(self.tk, var, text, x, y, side, bg, activebg)
    class mk_check():
        def make(parent, var, text, x, y, side, bg, activebg):
            self = tk.Checkbutton(parent, text=text, variable=var, bg=bg, activebackground=activebg)
            ezplace(self, x, y, side)
            return self
    # LIST OF RADIO BUTTONS
    def mkradiobuttons(self, names=["Sample"], x=0, y=0, side="", clearx=0, cleary=20, bg="#FFFFFF", activebg="#FFFFFF"):
        return self.mk_radiobuttons(self.tk, names, x, y, side, clearx, cleary, bg, activebg)
    class mk_radiobuttons():
        # This creates several objects at the same time so it doesn't return a tkinter object
        # Use only if accessing other variables after being created is not necessary.
        # The variable that stores the number of the option selected is self.variable, you can get it with self.getvar()
        def __init__(self, parent, names, x, y, side, clearx, cleary, bg, activebg):
            self.parent = parent
            self.variable = IntVar()
            self.lastposition = 0
            self.buttons = {}
            names = list(names)
            self.add(names, x, y, side, clearx, cleary, bg, activebg)
        def add(self, names, x=0, y=0, side="", clearx=0, cleary=20, bg="#FFFFFF", activebg="#FFFFFF"):
            names = list(names)
            for i in range(len(names)):
                self.buttons[names[i]] = tk.Radiobutton(self.parent, text=names[i], variable=self.variable, value=self.lastposition, bg=bg, activebackground=activebg)
                ezplace(self.buttons[names[i]], x+clearx*i, y+cleary*i, side=side)
                self.lastposition += 1
        def getvar(self):
            return self.variable.get()
    # LIST
    def mklistbox(self, names=["Sample"], start_position=-1, width=80, height=150, x=0, y=0, side="", bg="#FFFFFF"):
        return self.mk_listbox(self.tk, names, start_position, width, height, x, y, side, bg)
    class mk_listbox():
        # This will also not return a tkinter object as it needs multiple children objects, again self.getvar() to get the selected box
        def __init__(self, parent, names, start_position, width, height, x, y, side, bg):
            self.parent = parent
            self.object = tk.Listbox(parent, width=width, height=height, bg=bg)
            ezplace(self.object, x, y, side)
            self.lastposition = 0
            self.selection = int
            self.add(names, start_position)
        def add(self, names, start_position):
            names = list(names)
            if start_position < -1:
                print("Wrong index!")
                return 1
            if start_position >= self.lastposition or start_position == -1:
                for i in range(len(names)):
                    self.object.insert(self.lastposition, names[i])
                    self.lastposition += 1
            else:
                for i in range(len(names)):
                    if start_position < self.lastposition:
                        self.object.delete(start_position)
                        self.object.insert(start_position, names[i])
                        start_position += 1
                    if start_position >= self.lastposition:
                        self.lastposition += 1
        def getvar(self):
            return self.object.curselection()[0]
    # BIG INPUT BOX
    def mktextbox(self, x=0, y=0, width=50, height=50, side=""):
        return self.mk_textbox.make(self.tk, x, y, width, height, side)
    class mk_textbox():
        def make(parent, x, y, width, height, side):
            self = Text(parent, width=width, height=height)
            ezplace(self, x, y, side)
            return self
    # BIG INPUT BOX WITH SCROLL BAR
    def mkscrolledtextbox(self, x=0, y=0, width=50, height=50, side=""):
        return self.mk_scrolledtextbox.make(self.tk, x, y, width, height, side)
    class mk_scrolledtextbox():
        def make(parent, x, y, width, height, side):
            self = ScrolledText(parent, width=width, height=height)
            ezplace(self, x, y, side)
            return self
    # TOP VIEW MENU
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
    def mkscrollbar(self, width=18, orient="vertical", fill="none", side="right"):
        scrollbar = tk.Scrollbar(self.tk, orient=orient, width=width)
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