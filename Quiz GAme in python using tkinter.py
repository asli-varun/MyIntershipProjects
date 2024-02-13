from tkinter import *
from tkinter import ttk
y = 0
a = ttk.Notebook()
Frame1 = ttk.Frame(a)
Frame2 = ttk.Frame(a)
Frame3 = ttk.Frame(a)
Frame4 = ttk.Frame(a)
Frame5 = ttk.Frame(a)
Frame6 = ttk.Frame(a)
Frame7 = ttk.Frame(a)
Frame8 = ttk.Frame(a)
Frame9 = ttk.Frame(a)
Frame10 = ttk.Frame(a)

root = ttk.Frame(a)

def quiz(y):
    a.add(Frame1, text="Question 1")
    a.add(Frame2, text="Question 2")
    a.add(Frame3, text="Question 3")
    a.add(Frame4, text="Question 4")
    a.add(Frame5, text="Question 5")
    a.add(Frame6, text="Question 6")
    a.add(Frame7, text="Question 7")
    a.add(Frame8, text="Question 8")
    a.add(Frame9, text="Question 9")
    a.add(Frame10, text="Question 10")

    Label(Frame1, text="1)Who is the prime minster of India ?", font=("sans-serif",50,"bold")).grid(row=1,column=1)
    Button(Frame1, text="A. Rahul Gandhi", font=("sans-serif",20,"bold"),bg="green",command=a_wrong).grid(row=2,column=1)
    Button(Frame1, text="B. Arvind Kejriwal", font=("sans-serif",20,"bold"),bg="green",command=a_wrong).grid(row=3,column=0)
    Button(Frame1, text="C. Mahmohan Singh", font=("sans-serif",20,"bold"),bg="green",command=a_wrong).grid(row=4,column=0)
    Button(Frame1, text="D. Narendra Modi", font=("sans-serif",20,"bold"),bg="green",command=a_right).grid(row=5,column=0)

    Label(Frame2, text="2)Who is the President of India ?", font=("sans-serif",50,"bold")).grid(row=1,column=1)
    Button(Frame2, text="A. Ramnath Govind", font=("sans-serif",20,"bold"),bg="green",command=a2_wrong).grid(row=2,column=1)
    Button(Frame2, text="B. Venkiah Naidu", font=("sans-serif",20,"bold"),bg="green",command=a2_wrong).grid(row=3,column=1)
    Button(Frame2, text="C. Yogi Adithyanth", font=("sans-serif",20,"bold"),bg="green",command=a2_wrong).grid(row=4,column=1)
    Button(Frame2, text="D. Drupati Murmu", font=("sans-serif",20,"bold"),bg="green",command=a2_right).grid(row=5,column=1)

    Label(Frame3, text="3)Smallest State of India according to area?", font=("sans-serif", 50, "bold")).grid(row=1, column=1)
    Button(Frame3, text="A. Goa", font=("sans-serif",20,"bold"),bg="green",command=a3_right).grid(row=2,column=1)
    Button(Frame3, text="B. Mizoram", font=("sans-serif",20,"bold"),bg="green",command=a3_wrong).grid(row=3,column=1)
    Button(Frame3, text="C. Kerala", font=("sans-serif",20,"bold"),bg="green",command=a3_wrong).grid(row=4,column=1)
    Button(Frame3, text="D. Nagaland", font=("sans-serif",20,"bold"),bg="green",command=a3_wrong).grid(row=5,column=1)

    Label(Frame4, text="4)Which state contribute most to the economy of India?", font=("sans-serif", 50, "bold")).grid(row=1, column=1)
    Button(Frame4, text="A. Uttar Pradesh", font=("sans-serif",20,"bold"),bg="green",command=a4_wrong).grid(row=2,column=1)
    Button(Frame4, text="B. Delhi", font=("sans-serif",20,"bold"),bg="green",command=a4_wrong).grid(row=3,column=1)
    Button(Frame4, text="C. Maharashtra", font=("sans-serif",20,"bold"),bg="green",command=a4_right).grid(row=4,column=1)
    Button(Frame4, text="D. Telengna", font=("sans-serif",20,"bold"),bg="green",command=a4_wrong).grid(row=5,column=1)

    Label(Frame5, text="5)Which year India got Independence?", font=("sans-serif", 50, "bold")).grid(row=1, column=1)
    Button(Frame5, text="A. 1945", font=("sans-serif",20,"bold"),bg="green",command=a5_wrong).grid(row=2,column=1)
    Button(Frame5, text="B. 1946", font=("sans-serif",20,"bold"),bg="green",command=a5_wrong).grid(row=3,column=2)
    Button(Frame5, text="C. 1947", font=("sans-serif",20,"bold"),bg="green",command=a5_right).grid(row=4,column=3)
    Button(Frame5, text="D. 1950", font=("sans-serif",20,"bold"),bg="green",command=a5_wrong).grid(row=5,column=4)

    Label(Frame6, text="6)Who is the first President of India?", font=("sans-serif", 50, "bold")).grid(row=1, column=1)
    Button(Frame6, text="A. Rajendra Parsad", font=("sans-serif",20,"bold"),bg="green",command=a6_right).grid(row=2,column=1)
    Button(Frame6, text="B. Rajeev Gandhi", font=("sans-serif",20,"bold"),bg="green",command=a6_wrong).grid(row=3,column=2)
    Button(Frame6, text="C. Motilal Nehru", font=("sans-serif",20,"bold"),bg="green",command=a6_wrong).grid(row=4,column=3)
    Button(Frame6, text="D. Indira Gandhi", font=("sans-serif",20,"bold"),bg="green",command=a6_wrong).grid(row=5,column=4)

    Label(Frame7, text="7)Who is the first Prime Minster of India?", font=("sans-serif", 50, "bold")).grid(row=1, column=1)
    Button(Frame7, text="A. Rajendra Parsad", font=("sans-serif",20,"bold"),bg="green",command=a7_wrong).grid(row=2,column=1)
    Button(Frame7, text="B. Jawharlal Nehru", font=("sans-serif",20,"bold"),bg="green",command=a7_right).grid(row=3,column=2)
    Button(Frame7, text="C. Motilal Nehru", font=("sans-serif",20,"bold"),bg="green",command=a7_wrong).grid(row=4,column=3)
    Button(Frame7, text="D. Indira Gandhi", font=("sans-serif",20,"bold"),bg="green",command=a7_wrong).grid(row=5,column=4)

    Label(Frame8, text="8)Who is the current Chief Minster of Uttar Pradesh?", font=("sans-serif", 50, "bold")).grid(row=1, column=1)
    Button(Frame8, text="A. Yogi Adithyanath", font=("sans-serif",20,"bold"),bg="green",command=a8_right).grid(row=2,column=1)
    Button(Frame8, text="B. Nitish Kumar", font=("sans-serif",20,"bold"),bg="green",command=a8_wrong).grid(row=3,column=1)
    Button(Frame8, text="C. Akhilesh Yadav", font=("sans-serif",20,"bold"),bg="green",command=a8_wrong).grid(row=4,column=1)
    Button(Frame8, text="D. Indira Gandhi", font=("sans-serif",20,"bold"),bg="green",command=a8_wrong).grid(row=5,column=4)

    Label(Frame9, text="9)Who is the current Chief Minster of Bihar?", font=("sans-serif", 50, "bold")).grid(row=1, column=1)
    Button(Frame9, text="A. Yogi Adithyanath", font=("sans-serif",20,"bold"),bg="green",command=a9_wrong).grid(row=2,column=1)
    Button(Frame9, text="B. Nitish Kumar", font=("sans-serif",20,"bold"),bg="green",command=a9_right).grid(row=3,column=1)
    Button(Frame9, text="C. Akhilesh Yadav", font=("sans-serif",20,"bold"),bg="green",command=a9_wrong).grid(row=4,column=1)
    Button(Frame9, text="D. Indira Gandhi", font=("sans-serif",20,"bold"),bg="green",command=a9_wrong).grid(row=5,column=1)

    Label(Frame10, text="10)Who wrote National Anthem of India?", font=("sans-serif", 50, "bold")).grid(row=1,column=1)
    Button(Frame10, text="A. Rabindra Nath Tagore", font=("sans-serif",20,"bold"),bg="green",command=a10_right).grid(row=2,column=1)
    Button(Frame10, text="B. Munshi Premchand", font=("sans-serif",20,"bold"),bg="green",command=a10_wrong).grid(row=3,column=1)
    Button(Frame10, text="C. Harivansh Rai", font=("sans-serif",20,"bold"),bg="green",command=a10_wrong).grid(row=4,column=1)
    Button(Frame10, text="D. Janardhan Singh", font=("Sans-serif",20,"bold"),bg="green",command=a10_wrong).grid(row=5,column=1)

def a_right():
     Label(Frame1, text="CORRECT", font=("sans-serif",40,"bold"), background="green",fg="yellow").grid(row=5,column=2)
     Label(Frame1, text="Marks Obtained: 1", font=("sands-serif",40,"bold"), background="black",fg="white").grid(row=1,column=6)

def a_wrong():
     Label(Frame1, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
     Label(Frame1, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=2, column=2)

def a2_right():
    Label(Frame2, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame2, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a2_wrong():
    Label(Frame2, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame2, text="Marks Obtained: O", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a3_right():
    Label(Frame3, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame3, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid( row=1, column=3)

def a3_wrong():
    Label(Frame3, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame3, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a4_right():
    Label(Frame4, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame4, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a4_wrong():
    Label(Frame4, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame4, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a5_right():
    Label(Frame5, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame5, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a5_wrong():
    Label(Frame5, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame5, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a6_right():
    Label(Frame6, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame6, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a6_wrong():
    Label(Frame6, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame6, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a7_right():
    Label(Frame7, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame7, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a7_wrong():
    Label(Frame7, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame7, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a8_right():
    Label(Frame8, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame8, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a8_wrong():
    Label(Frame8, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame8, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a9_right():
    Label(Frame9, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame9, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a9_wrong():
    Label(Frame9, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame9, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a10_right():
    Label(Frame10, text="CORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame10, text="Marks Obtained: 1", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

def a10_wrong():
    Label(Frame10, text="INCORRECT", font=("sans-serif", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(Frame10, text="Marks Obtained: 0", font=("sands-serif", 40, "bold"), background="black", fg="white").grid(row=1, column=3)

quiz(y)
a.pack()
root.mainloop()