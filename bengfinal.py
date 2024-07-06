import pandas as pd
from pandas._config import display
from sklearn import linear_model
from tkinter import *

df=pd.read_csv(r"C:\Users\Rakshith CM \Desktop\lab\homeprices_banglore.csv")
x=df.drop(columns=['price'])
y=df.drop(columns=['bedrooms','area','age'],axis='columns')


window=Tk()
window.title("BENGALARU HOUSE PRICE")
window.geometry("800x300+100+75")

srtlabel=Label(text="Enter sqrt  :",)
srtlabel.grid(column=0,row=0)
srt=Entry(width=40)
srt.grid(row=0,column=1)

bedslabel=Label(text="Enter beds:")
bedslabel.grid(column=0,row=1)
beds=Entry(width=40)
beds.grid(column=1,row=1)

ageslabel=Label(text="Enter age :")
ageslabel.grid(column=0,row=2)
ages=Entry(width=40)
ages.grid(row=2,column=1)

b1=Button(window,text="Find",width=9,height=2,fg="#FFFFFF",bg="#303F9F",command=lambda: find())
b1.grid(row=4,column=1)

display=Label(window,text=" ",width=120,height=4,fg="#FFFFFF",bg="#303F9F")
display.grid(row=6,column=0,columnspan=3)

model=linear_model.LinearRegression()
model.fit(x,y)

n=1
def find():
 global n
 while n==1:
    sqrt = int(srt.get())
    bed = int(beds.get())
    age = int (ages.get())
    amount=model.predict([[sqrt,bed,age]])
    display.config(text=f"{"The Assessed Value for the House with",sqrt,"sqrt with",age,"years old house for RS:",float(amount[0][0])}")
    n+=1

window.mainloop()