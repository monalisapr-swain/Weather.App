from tkinter import *
from tkinter import ttk
import requests

def data_get():

     city = city_name.get()
     data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=51b59aec58713614b38f106dda289645").json()
     w_label1.config(text=data["weather"][0]["main"])
     wd_label1.config(text=data["weather"][0]["description"])
     wt_label1.config(text=str(data["main"]["temp"]-273.15))
     pr_label1.config(text=data["main"]["pressure"])



win = Tk() 
win.title("Weather App by Monalisa")
win.config(bg="blue")
win.geometry("500x600")


name_label = Label(win,text="Weather App", font=("LEMON MILK",40))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Weather App",values=list_name, font=("LEMON MILK",25),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)



w_label = Label(win,text="Weather Climate", font=("LEMON MILK",15))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text="", font=("LEMON MILK",15))
w_label1.place(x=250,y=260,height=50,width=210)


wd_label = Label(win,text="Weather Description", font=("LEMON MILK",13))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1 = Label(win,text="", font=("LEMON MILK",13))
wd_label1.place(x=250,y=330,height=50,width=210)

wt_label = Label(win,text="Temperature", font=("LEMON MILK",13))
wt_label.place(x=25,y=400,height=50,width=210)
wt_label1 = Label(win,text="", font=("LEMON MILK",15))
wt_label1.place(x=250,y=400,height=50,width=210)

pr_label = Label(win,text="Pressure", font=("LEMON MILK",13))
pr_label.place(x=25,y=470,height=50,width=210)
pr_label1 = Label(win,text="", font=("LEMON MILK",15))
pr_label1.place(x=250,y=470,height=50,width=210)

done_button =Button(win,text="Done", font=("LEMON MILK",25),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()