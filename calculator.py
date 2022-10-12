from tkinter import*
from math import*

expression=""


def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)




  
def react():
    try:
        global expression
        total=str(eval(expression))

        equation.set(total)

        expression=""



    except:
        equation.set("syntax error")
        expression=""

def clear():
    global expression
    equation.set("")

if __name__ == "__main__":
    parent=Tk()
    parent.title("calculator")
    parent.geometry("238x390")
    equation=StringVar()


    x =Entry(parent,width = 1,bg = "grey",textvariable=equation)
    x.grid(columnspan=4,ipadx=112,ipady=50)


    butmc =Button(parent,text = "MC", fg = "black",width=3,height=1 ).grid(row = 1,column=0,sticky = "w")
    butmr =Button(parent,text = "MR", fg = "white",bg="black",width=3,height=1 ).grid(row = 1,column=0,sticky = "e")
    butm =Button(parent,text = "M+", fg = "white",bg =  "black",width=3,height=1 ).grid(row = 1,column=1,sticky = "w")
    butm =Button(parent,text = "M-", fg = "white",bg =  "black",width=3,height=1 ).grid(row = 1,column=1,sticky = "e")
    butms =Button(parent,text = "MS", fg = "white",bg =  "black",width=7,height=1 ).grid(row = 1,column=2,sticky = "w")
    butm =Button(parent,text = "M", fg = "grey",bg =  "black",width=7,height=1 ).grid(row = 1,column=3,sticky = "w")

    but =Button(parent,text = "%", fg = "white",bg= "grey", width=7,height=2 ).grid(row = 2,column=0)
    but =Button(parent,text = "CE", fg = "white",bg= "grey",width=7,height=2 ).grid(row = 2,column=1)
    but =Button(parent,text = "C", fg = "white",bg= "grey",width=7,height=2 ).grid(row = 2,column=2)
    but =Button(parent,text = "DEL", fg = "white",bg= "grey",command=clear,width=7,height=2 ).grid(row = 2,column=3)

    but1=Button(parent,text = "⅛",fg="white",bg =  "grey",width = 7,height = 2).grid(row = 3,column=0)
    but2=Button(parent,text = "x^2",fg="white",bg =  "grey",command=lambda:press('**'),width = 7,height = 2).grid(row = 3,column=1)
    but3=Button(parent,text = "2√x",fg="white",bg =  "grey",width = 7,height = 2).grid(row = 3,column=2)
    but3=Button(parent,text = "÷ ",fg="white",bg =  "grey",command=lambda:press("/"),width = 7,height = 2).grid(row = 3,column=3)
    but4=Button(parent,text = "7",fg="white",bg =  "black",width = 7,command=lambda:press(7),height = 2).grid(row = 4,column=0)
    but5=Button(parent,text = "8",fg="white",bg =  "black",width = 7,command=lambda:press(8),height = 2).grid(row = 4,column= 1)
    but3=Button(parent,text = "9",fg="white",bg =  "black",width = 7,command=lambda:press(9),height = 2).grid(row = 4,column=2)
    but3=Button(parent,text = "x",fg="white",bg =  "grey",width = 7,command=lambda:press("*"),height = 2).grid(row = 4,column=3)
    but3=Button(parent,text = "4",fg="white",bg =  "black",command=lambda:press(4),width = 7,height = 2).grid(row = 5,column=0)
    but3=Button(parent,text = "5",fg="white",bg =  "black",command=lambda:press(5),width = 7,height = 2).grid(row = 5,column=1)
    but3=Button(parent,text = "6",fg="white",bg =  "black",command=lambda:press(6),width = 7,height = 2).grid(row = 5,column=2)
    but3=Button(parent,text = "-",fg="white",bg =  "grey",command=lambda:press("-"),width = 7,height = 2).grid(row = 5,column=3)
    but3=Button(parent,text = "1",fg="white",bg =  "black", command=lambda:press(1),width = 7,height = 2).grid(row = 6,column=0)
    but3=Button(parent,text = "2",fg="white",bg =  "black",command=lambda:press(2),width = 7,height = 2).grid(row = 6,column=1)
    but3=Button(parent,text = "3",fg="white",bg =  "black",command=lambda:press(3),width = 7,height = 2).grid(row = 6,column=2)
    but3=Button(parent,text = "+",fg="white",bg =  "grey",command=lambda:press("+"),width = 7,height = 2).grid(row = 6,column=3)
    but3=Button(parent,text = "+/-",fg="white",bg =  "black",width = 7,height = 2).grid(row = 7,column=0)
    but3=Button(parent,text = "0",fg="white",bg =  "black",command=lambda:press(0),width = 7,height = 2).grid(row = 7,column=1)
    but3=Button(parent,text = ".",fg="white",bg =  "black",width = 7,height = 2).grid(row = 7,column=2)
    but3=Button(parent,text = "=",fg="black",bg =  "grey",command=react,width = 7,height = 2).grid(row = 7,column=3)

    parent.mainloop()
    


