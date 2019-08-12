from ui.ui import UI
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


class Display(UI):
    def __init__(self):
        self.root = Tk()
        self.root.title(u'Пример tagcounter приложения')
        self.root.geometry('500x400+300+200')  # ширина=500, высота=400, x=300, y=200
        self.root.protocol('WM_DELETE_WINDOW', self.window_deleted)  # обработчик закрытия окна
        self.root.resizable(True, False)  # размер окна может быть изменён только по горизонтали
        sapp = Application(master=self.root)
        sapp.mainloop()

    def window_deleted(self):
        self.root.quit()  # явное указание на выход из программы

    def show(self):
        pass