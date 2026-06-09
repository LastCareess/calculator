import tkinter as tk

#основное окно
root = tk.Tk()

root.geometry("1020x580")

#текст
label = tk.Label(text="Привет я медоед")
#поставили текст в очередь
label.grid(row=0, column=0)


clicks = 0
winner_label = tk.Label(text="Ты герой!", fg="red")

#Кнопка
def first_button():
    global clicks
    clicks += 1
    click_label.config(text=f"Кликов: {clicks}")
    print("кто-то кликнул", clicks)
    if clicks >= 10:
        winner_label.grid(row=2,column=0)
    if clicks == 11:
        winner_label.config(text=" ")

button = tk.Button(text="ТКНИ СЮДА", command=first_button)
button.grid(row=0,column=1)

click_label = tk.Label(text=f"Кликов: {clicks}", font=("Arial",25), fg="blue")
click_label.grid(row=0,column=3)


#Пароль и логин
userinp_login = tk.Entry()
userinp_login.grid(row=4,column=0)

userinp_password = tk.Entry()
userinp_password.grid(row=4,column=1)





#Подтверждение



def submit():
    text = userinp_login.get()
    textp = userinp_password.get()
    login = tk.Label(text=f"Ваш логин: {text}, ваш пароль: {textp}")
    login.grid(row=4,column=3)
    print(text)

submitt = tk.Button(text="Отправить", command=submit)
submitt.grid(row=4,column=2)



label = tk.Label(text="Выбери свой путь")
label.grid(row=6,column=0)

cb1 = tk.Checkbutton(text="Выключение")
cb1.grid(row=6, column=1)

cb2 = tk.Checkbutton(text="Приключение")
cb2.grid(row=6, column=2)


selected_option = tk.StringVar(value="тест")

rb1 = tk.Radiobutton(text="Выключение",variable=selected_option, value="delete")
rb1.grid(row=7, column=0)

rb2 = tk.Radiobutton(text="Приключение", variable=selected_option, value="Adventure")
rb2.grid(row=7, column=1)



root.mainloop()