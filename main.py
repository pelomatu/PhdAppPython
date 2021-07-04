
from tkinter import *

class Per:
   def __init__(self, root):
       self.firstname = Label(root, text="Enter Your First Name")
       self.lastname = Label(root, text="Enter Your Surname")
       self.ID = Label(root, text="Enter Your ID NO.")
       self.DOB = Label(root, text="Enter Your Date Of Birth")
       self.firstname.place(x=0, y=10)
       self.lastname.place(x=0, y=30)
       self.ID.place(x=0, y=50)
       self.DOB.place(x=0, y=70)
       self.firstname = StringVar()
       self.lastname = StringVar()
       self.ID = StringVar()
       self.DOB = StringVar()
       self.txtname = Entry(root, textvariable=self.firstname)
       self.txtSname = Entry(root, textvariable=self.lastname)
       self.txtID = Entry(root, textvariable=self.ID)
       self.txtDOB = Entry(root, textvariable=self.DOB)
       self.txtname.place(x=150, y=10)
       self.txtSname.place(x=150, y=30)
       self.txtID.place(x=150, y=50)
       self.txtDOB.place(x=150, y=70)
       self.v0 = IntVar()
       self.r1 = Radiobutton(root, text="PhD Examiner", variable=self.v0, value=1, command=lambda: checkedexa(root))
       self.r2 = Radiobutton(root, text="PhD Student", variable=self.v0, value=2, command=lambda: checkedstu(root))
       self.r1.pack()
       self.r2.pack()
       self.r1.place(x=0, y=100)
       self.r2.place(x=150, y=100)




class checkedexa(Per):
    def __init__(self, root):
        self.stfnum = Label(root, text="Enter Your  Staff Number", width="25")
        self.hrate = Label(root, text="Enter Your Hourly Rate", width="20")
        self.nhour = Label(root, text="Enter number of hours", width="20")
        self.stfnum.place(x=0, y=140)
        self.hrate.place(x=0, y=160)
        self.nhour.place(x=0, y=180)
        self.stfnum = StringVar()
        self.hrate = DoubleVar()
        self.nhour = DoubleVar()
        self.txtstfnumber = Entry(root, textvariable=self.stfnum, width="20")
        self.txthrate = Entry(root, textvariable=self.hrate, width="20")
        self.txtnhour = Entry(root, textvariable=self.nhour, width="20")
        self.txtstfnumber.place(x=190, y=140)
        self.txthrate.place(x=190, y=160)
        self.txtnhour.place(x=190, y=180)
        sub = Button(root, text="Submit", command=lambda: clickedExa())
        sub.place(x=20, y=220)

        
class checkedstu(Per):

    def __init__(self, root):
        self.stdnum = Label(root, text="Enter Your First Student Number", width="25")
        self.intm = Label(root, text="Enter Your Internal Mark", width="20")
        self.extm = Label(root, text="Enter Your External Mark", width="20")

        self.stdnum.place(x=0, y=140)
        self.intm.place(x=0, y=160)
        self.extm.place(x=0, y=180)
        self.stdnum = StringVar()
        self.intm = DoubleVar()
        self.extm = DoubleVar()
        self.txtstdnumber = Entry(root, textvariable=self.stdnum, width="20")
        self.txtintm = Entry(root, textvariable=self.intm, width="20")
        self.txtextm = Entry(root, textvariable=self.extm, width="20")
        self.txtstdnumber.place(x=190, y=140)
        self.txtintm.place(x=190, y=160)
        self.txtextm.place(x=190, y=180)
        sub = Button(root, text="Submit", command=lambda: clickedStu())
        sub.place(x=20, y=220)


def clickedStu():
    stu = checkedstu(root)
    Stud = PhDStudent(stu.stdnum.get(), stu.intm.get(), stu.extm.get(), stu.firstname.get(), stu.lastname, stu.ID.get(), stu.DOB.get())
    o.set(Stud.__str__())

def clickedExa():
    exa = checkedexa(root)
    Stud = PhdExaminer(exa.stfnum.get(), exa.nhour.get(), exa.hrate.get(), exa.firstname.get(), exa.lastname, exa.ID.get(),exa.DOB.get())
    o.set(Stud.__str__())

root = Tk()
root.geometry("500x500")
root.title("PhD App")
loadd = Per(root)
val = loadd.v0
if val == 1:
    exam = checkedexa(root)
elif val == 2:
    stu = checkedstu(root)

o = StringVar()
res = Label(root, textvariable=o, relief = RAISED )
o.set("Full Report")
res.place(x= 0, y= 260)

root.mainloop()


class Person:
    def __init__(self,fName,Sname,ID,DOB):
        self.fName=fName
        self.Sname = Sname
        self.ID = ID
        self.DOB = DOB

    def set_fName(self,name):
        self.fName=name

    def get_fName(self):
      return self.fName

    def set_Sname(self, Sname):
        self.Sname = Sname

    def get_Sname(self):
        return self.Sname

    def set_ID(self, ID):
        self.ID = ID

    def get_ID(self):
        return self.ID

    def set_DOB(self, DOB):
        self.DOB = DOB

    def get_DOB(self):
        return self.DOB

    def __str__(self):
        str=""
        str=str+"Your Name Is: " + self.fName
        str = str + "\n" + "Your Surname Is: " + self.Sname
        str = str + "\n" + "Your ID NO. Is: " + self.ID
        str = str + "\n" + "Your Date Of Birth Is: "+ self.DOB
        return str


class PhDStudent(Person):
    def __init__(self,stdnumber,intmark,extmark,fName,Sname,ID,DOB):
        super().__init__(self, fName, Sname, ID, DOB)
        self.stdnumber = stdnumber
        self.intmark = intmark
        self.extmark = extmark


    def set_stdnumber(self, stdnumber):
        self.stdnumber = stdnumber

    def get_stdnumber(self):
        return self.stdnumber

    def set_intmark(self,intmark):
        self.intmark = intmark

    def get_intmark(self):
        return self.intmark

    def set_extmark(self,extmark):
        self.extmark = extmark

    def get_extmark(self):
        return self.extmark

    def avg(self):
        return(self.extmark + self.intmark)/2

    def __str__(self):
        str ="Your PhD Student details: "
        str=str+"\n"+super().__str__()
        str = str + "\n" + "Your Student Number Is: "+self.stdnumber
        str = str + "\n" + "Your External Mark Is: " +self.extmark
        str = str + "\n" + "Your Internal Mark Is: " +self.intmark
        str = str + "\n" + "Your Average Mark Is: " + self.avg()
        return str


class PhdExaminer(Person):
    def __init__(self, stfnumber, nhours, hrate, fName, Sname, ID, DOB):
        self.stfnumber = stfnumber
        self.nhours = nhours
        self.hrate = hrate
        super().__init__(self,fName, Sname, ID, DOB)

    def get_stfnumber(self):
        return self.stfnumber

    def get_nrate(self):
        return self.hrate

    def get_nhours(self):
        return self.nhours

    def tot(self):
        return self.nhours*self.hrate

    def __str__(self):
        str = "Your PhD Examiner details: "
        str = str + "\n" + super().__str__()
        str = str + "\n" + "Your Staff Number Is: " + self.stfnumber
        str = str + "\n" + "Your Hourly Rate Is: " + self.hrate
        str = str + "\n" + "Your Number Of Hours Is: " + self.nhours
        str = str + "\n" + "Your Salary Is: " + self.tot()
        return str

