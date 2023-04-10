from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import pymysql


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1300x530+107+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.grab_set()
        self.root.resizable(False, False)

        # =====Title =========#
        title = Label(self.root, text="Add Student Results", font=(
            "goudy old style", 20, "bold"), bg="#5e7cd2", fg="white")
        title.place(x=10, y=10, width=1340, height=40)

        # ==== Variables ==== #
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_english = IntVar(value="")
        self.var_hindi = IntVar(value="")
        self.var_maths = IntVar(value="")
        self.var_science = IntVar(value="")
        self.var_computer = IntVar(value="")

        self.roll_list = []
        self.fetch()
        # ====== Labels ====== #
        lbl_select = Label(self.root, text="Select Student", font=(
            "goudy old style", 20, "bold"), bg="white").place(x=50, y=70)
        lbl_name = Label(self.root, text="Name", font=(
            "goudy old style", 20, "bold"), bg="white").place(x=50, y=120)

        lbl_txt = Label(self.root, text="Enter Marks Obtained Out of 100.", font=(
            "times new roman", 18, "bold"), bg="#5e7cd2", fg="white").place(x=50, y=170)

        lbl_english = Label(self.root, text="English", font=(
            "goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_hindi = Label(self.root, text="Hindi", font=(
            "goudy old style", 20, "bold"), bg="white").place(x=50, y=270)
        lbl_maths = Label(self.root, text="Maths", font=(
            "goudy old style", 20, "bold"), bg="white").place(x=50, y=320)
        lbl_science = Label(self.root, text="Science", font=(
            "goudy old style", 20, "bold"), bg="white").place(x=50, y=370)
        lbl_computer = Label(self.root, text="Computer Science", font=(
            "goudy old style", 20, "bold"), bg="white").place(x=50, y=420)

        # ====Entry Fields ===== #
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=(
            "goudy old style", 18, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=70)
        self.txt_student.set("Select")

        btn_search = Button(self.root, command=self.search,text="Search", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white")
        btn_search.place(x=570, y=70, width=130, height=32)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 20), bg="lightyellow", state='readonly')
        txt_name.place(x=280, y=120, width=300, height=30)

        txt_english = Entry(self.root, textvariable=self.var_english, font=(
            "goudy old style", 20), bg="lightyellow")
        txt_english.place(x=280, y=220, width=300, height=30)

        txt_hindi = Entry(self.root, textvariable=self.var_hindi, font=(
            "goudy old style", 20), bg="lightyellow")
        txt_hindi.place(x=280, y=270, width=300, height=30)

        txt_maths = Entry(self.root, textvariable=self.var_maths, font=(
            "goudy old style", 20), bg="lightyellow")
        txt_maths.place(x=280, y=320, width=300, height=30)

        txt_scinece = Entry(self.root, textvariable=self.var_science, font=(
            "goudy old style", 20), bg="lightyellow")
        txt_scinece.place(x=280, y=370, width=300, height=30)

        txt_computer = Entry(self.root, textvariable=self.var_computer, font=(
            "goudy old style", 20), bg="lightyellow")
        txt_computer.place(x=280, y=420, width=300, height=30)

        # ==== Buttons ==== #
        btn_add = Button(self.root, command=self.add, text="Save", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white").place(x=300, y=470, width=110, height=40)

        btn_clear = Button(self.root, command=self.clear, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white").place(x=430, y=470, width=110, height=40)
        
        # ==== Image ==== #
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((600,550),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg_img = Label(self.root, image=self.bg_img).place(x=720, y=50)

#===============================================================================#
    def fetch(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows :
                    self.roll_list.append(row[0])
        except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}", parent = self.root)

    def search(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select name from student where roll = %s",self.var_roll.get())
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
            else:
                messagebox.showerror("Error", "No record found!", parent = self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}", parent = self.root)
    
    def add(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror(
                    "Error", "First Search Student Record.", parent=self.root)
            else:
                cur.execute("select * from result where roll = %s",
                            self.var_roll.get())
                row = cur.fetchone()

                if (row != None):
                    messagebox.showerror("Error", "Result already present.", parent = self.root)
                else:
                    cur.execute("insert into result (roll, name, english, hindi, maths, science, computer) values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_english.get(),
                        self.var_hindi.get(),
                        self.var_maths.get(),
                        self.var_science.get(),
                        self.var_computer.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Result Added Successfully.", parent=self.root)
                    self.clear()
        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}", parent=self.root)


    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_english.set(""),
        self.var_hindi.set(""),
        self.var_maths.set(""),
        self.var_science.set(""),
        self.var_computer.set(""),
 
if __name__ == "__main__":

    root = Tk()
    obj = ResultClass(root)
    root.mainloop()