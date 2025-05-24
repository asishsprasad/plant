from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import cv2 as cv
import numpy as np
a = Tk()
a.title("Detection of Adulteration in Fruits")
a.geometry("1000x600")


def prediction(var, e_var1):
    import pandas as pd
    import joblib

    #loading the saved model
    load_model=joblib.load("Project_Saved_Models/pipeline_knn_model_99acc.sav")

    info=[]
    parameters=['fruit_label','ppm']

    fruit_label=var.get()
    ppm=e_var1.get()

    if fruit_label=='Select' or ppm=='':
        message.set("fill the empty field!!!")
    else:
        list_box.insert(1, "Loading Values")
        list_box.insert(2, "")
        list_box.insert(3, "Loading Model")
        list_box.insert(4, "")
        list_box.insert(5, "Prediction")
        message.set("")
        print(fruit_label)

        if fruit_label=='Apple':
            my_fruit_label=1
        elif fruit_label=='Orange':
            my_fruit_label=2

        print(my_fruit_label)
        info.append(my_fruit_label)
        ppm=float(ppm)
        print(type(ppm))
        info.append(ppm)



        my_dict=dict(zip(parameters,info))

        #convert dict into dataframe
        my_data=pd.DataFrame(my_dict,index=[0])

        # dataframe is putting into the MODEL to make PREDICTION
        my_pred = load_model.predict(my_data)
        print(my_pred)
        my_pred = my_pred[0]
        print(my_pred)

        print("Result:")
        if my_pred==0:
            a="UNSAFE"
            print("UNSAFE")
        if my_pred==1:
            a="SAFE"
            print("SAFE")

        out_label.config(text="Output : "+a)


   
def Check():
    global f
    f.pack_forget()

    f = Frame(a, bg="white")
    f.pack(side="top", fill="both", expand=True)

    global f1
    f1 = Frame(f, bg="light goldenrod")
    f1.place(x=0, y=0, width=760, height=320)
    f1.config()

    input_label = Label(f1, text="INPUT", font="arial 16 bold", bg="light goldenrod")
    input_label.pack(padx=0, pady=10)

    label1 = Label(f1, text="Fruit Name :", font="arial 12 bold", bg="light goldenrod")
    label1.place(x=130, y=80)
    label2 = Label(f1, text="Formaldehyde Content(ppm) :",
                   font="arial 12 bold", bg="light goldenrod")
    label2.place(x=130, y=140)

    var = StringVar()
    var.set("Select")
    options = ["Apple", "Orange"]
    op1 = OptionMenu(f1, var, *options)
    op1.place(x=370, y=80)

    global message
    e_var1 = StringVar()
    message = StringVar()

    entry1 = Entry(f1, textvariable=e_var1, bd=2, width=25)
    entry1.place(x=370, y=140)

    msg_label = Label(f1, text="", textvariable=message,
                      bg='light goldenrod').place(x=370, y=170)

    predict_button = Button(
        f1, text="Predict", command=lambda: prediction(var, e_var1), bg="hot pink")
    predict_button.pack(side="bottom", pady=80)
    global f2
    f2 = Frame(f, bg="turquoise")
    f2.place(x=0, y=320, width=760, height=300)
    f2.config(pady=20)

    result_label = Label(f2, text="RESULT", font="arial 16 bold", bg="turquoise")
    result_label.pack(padx=0, pady=0)

    global out_label
    out_label = Label(f2, text="", bg="turquoise", font="arial 16 bold")
    out_label.pack(pady=40)

    f3 = Frame(f, bg="SkyBlue2")
    f3.place(x=760, y=0, width=240, height=690)
    f3.config()

    name_label = Label(f3, text="Process", font="arial 14", bg="SkyBlue2")
    name_label.pack(pady=20)

    global list_box
    list_box = Listbox(f3, height=12, width=31)
    list_box.pack()


def Home():
    global f
    f.pack_forget()

    f = Frame(a, bg="salmon")
    f.pack(side="top", fill="both", expand=True)

    front_image = Image.open("ppp.jpg")
    front_photo = ImageTk.PhotoImage(front_image.resize((a.winfo_width(), a.winfo_height()), Image.ANTIALIAS))
    front_label = Label(f, image=front_photo)
    front_label.image = front_photo
    front_label.pack()

    home_label = Label(f, text="Fruit Adulteration Detection",
                       font="arial 35", bg="white")
    home_label.place(x=270, y=250)


f = Frame(a, bg="salmon")
f.pack(side="top", fill="both", expand=True)
front_image1 = Image.open("ppp.jpg")
front_photo1 = ImageTk.PhotoImage(front_image1.resize((1000, 600), Image.ANTIALIAS))
front_label1 = Label(f, image=front_photo1)
front_label1.image = front_photo1
front_label1.pack()

home_label = Label(f, text="Fruit Adulteration Detection",
                   font="arial 35", bg="white")
home_label.place(x=270, y=250)

m = Menu(a)
m.add_command(label="Home", command=Home)
checkmenu = Menu(m)
m.add_command(label="Check", command=Check)
a.config(menu=m)


a.mainloop()
