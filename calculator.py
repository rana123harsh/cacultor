# cacultor
#cacultor app code in python
# Code to be paste

from tkinter import *

from dlib import segmenter_type
from numpy import signedinteger

root = Tk()
root.title("Calculator App")
root.minsize(width=500, height=623)
root.maxsize(width=500, height=623)


# Code For Icon (Paste Here)

def ScitechzCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="Black")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, bg="gray", fg="gray5", text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

icon = PhotoImage(file="/home/harsh/workspace/scrip-python/data/img/calculator/iconfinder_Calculator_16_171352.png")  # Png , Jpg , Other.
root.tk.call('wm', 'iconphoto', root._w, icon)  # Image Should Be With The Python File.

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'Helvetica 22 italic', )
        self.pack(expand=YES, fill=BOTH)

        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display, justify='right', bd=20, fg="White", bg="cornsilk4").pack(side=TOP, expand=YES,
                                                                                             fill=BOTH)



        for clearBut in (["CLEAR"],):
            erase = ScitechzCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in ("789/", "456*", "123-", "0.+","%()"):
            FunctionNum = ScitechzCalc(self, TOP)
            for char in NumBut:
                    button(FunctionNum,LEFT,char,
                       lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))

        EqualsButton = ScitechzCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualsButton,RIGHT,iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                                lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualsButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("::Error::")




if __name__ == '__main__':
    app().mainloop()
