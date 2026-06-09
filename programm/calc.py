import tkinter as tk
import operator

actions = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,}


root = tk.Tk()

root.geometry("1020x580")
root.config(bg="black")

def press_button(event):
    button_text = event.widget.cget("text")
    newout = output.cget("text")+button_text
    output.config(text=newout)






name = tk.Label(text="calculator output: ", font=("Verdana", 25))
name.grid(row=0, column=0)

output = tk.Label(text="")
output.grid(row=0, column=1)






button1 = tk.Button(text="1", font=("Arial",25))
button1.grid(row=1,column=10)
button1.bind("<Button-1>", press_button)

button2 = tk.Button(text="2", font=("Arial",25))
button2.grid(row=1,column=11)
button2.bind("<Button-1>", press_button)

button3 = tk.Button(text="3", font=("Arial",25))
button3.grid(row=1,column=12)
button3.bind("<Button-1>", press_button)

button4 = tk.Button(text="4", font=("Arial",25))
button4.grid(row=2,column=10)
button4.bind("<Button-1>", press_button)

button5 = tk.Button(text="5", font=("Arial",25))
button5.grid(row=2,column=11)
button5.bind("<Button-1>", press_button)

button6 = tk.Button(text="6", font=("Arial",25))
button6.grid(row=2,column=12)
button6.bind("<Button-1>", press_button)

button7 = tk.Button(text="7", font=("Arial",25))
button7.grid(row=3,column=10)
button7.bind("<Button-1>", press_button)

button8 = tk.Button(text="8", font=("Arial",25))
button8.grid(row=3,column=11)
button8.bind("<Button-1>", press_button)

button9 = tk.Button(text="9", font=("Arial",25))
button9.grid(row=3,column=12)
button9.bind("<Button-1>", press_button)


multiplybutton = tk.Button(text="*", font=("Arial",25))
multiplybutton.grid(row=1,column=14)
multiplybutton.bind("<Button-1>", press_button)

splitbutton = tk.Button(text="/", font=("Arial",25))
splitbutton.grid(row=2,column=14)
splitbutton.bind("<Button-1>", press_button)

appendbutton = tk.Button(text="+", font=("Arial",25))
appendbutton.grid(row=3,column=14)
appendbutton.bind("<Button-1>", press_button)

subtractbutton = tk.Button(text="-", font=("Arial",25))
subtractbutton.grid(row=4,column=14)
subtractbutton.bind("<Button-1>", press_button)


def equals():
    history = {}
    operations = []
    iteration = 0
    for num in output.cget("text"):
        if num.isdigit():
            if iteration in history:
                newnum = history[iteration] + num
                history[iteration] = newnum
            else:
                history[iteration] = num
        else:
            operations.append(num)
            iteration += 1

    result = int(history[0])


    for i, op in enumerate(operations):
        next_num = int(history[i + 1])

        result = actions[op](result, next_num)

    output.config(text=str(result))
    

def clear_screen():
    output.config(text="") 




equalsbutton = tk.Button(text="=", font=("Arial",25), command=equals)
equalsbutton.grid(row=3,column=15)



clearbutton = tk.Button(text="C", font=("Arial",25), command=clear_screen)
clearbutton.grid(row=4,column=15)



root.mainloop()