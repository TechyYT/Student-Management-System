from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import pymysql

class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1300x500+107+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.grab_set()
        self.root.resizable(False, False)

        # ====Variables =======#
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # =====Title =========#
        title = Label(self.root, text="Manage Student Details", font=(
            "goudy old style", 20, "bold"), bg="#5e7cd2", fg="white")
        title.place(x=10, y=10, width=1340, height=40)

        # ========Labels======== #
            
            #==Column-1==#
        lbl_roll = Label(self.root, text="Roll No.", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_Name = Label(self.root, text="Name", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=110)
        lbl_Email = Label(self.root, text="Email", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=160)
        lbl_gender = Label(self.root, text="Gender", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=210)
        lbl_address = Label(self.root, text="Address", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=310)
        lbl_state = Label(self.root, text="State", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=260)
            
            #==Column-2==#
        lbl_dob = Label(self.root, text="D.O.B", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        lbl_admission = Label(self.root, text="Admission", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=360, y=160)
        lbl_contact = Label(self.root, text="Contact", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=360, y=110)
        lbl_city = Label(self.root, text="City", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=320, y=260)
        lbl_pin = Label(self.root, text="PIN", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=500, y=260)
        
        # ====Entry Fields===========#
            
            #===Column-1===#
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=(
            "goudy old style", 15), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 15), bg="lightyellow").place(x=150, y=110, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=(
            "goudy old style", 15), bg="lightyellow").place(x=150, y=160, width=200)
        self.txt_gender = ttk.Combobox(self.root, values=("Select","Male","Female","Other"), textvariable=self.var_gender, font=(
            "goudy old style", 15), state='readonly', justify=CENTER)
        self.txt_gender.place(x=150, y=210, width=200)
        self.txt_gender.current(0)
        txt_state = Entry(self.root, textvariable=self.var_state, font=(
            "goudy old style", 15), bg="lightyellow").place(x=150, y=260, width=150)
        self.txt_address = Text(self.root, font=(
            "goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=310, width=500, height=110)

            #===Column-2===#
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=(
            "goudy old style", 15), bg="lightyellow")
        self.txt_dob.place(x=480, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=(
            "goudy old style", 15), bg="lightyellow").place(x=480, y=110, width=200)
        txt_admission = Entry(self.root, textvariable=self.var_a_date, font=(
            "goudy old style", 15), bg="lightyellow").place(x=480, y=160, width=200)
        txt_city = Entry(self.root, textvariable=self.var_city, font=(
            "goudy old style", 15), bg="lightyellow").place(x=380, y=260, width=110)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=(
            "goudy old style", 15), bg="lightyellow").place(x=550, y=260, width=127)
        
        # =====Buttons==========#
        self.btn_add = Button(self.root, command=self.add, text="Save", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2")
        self.btn_add.place(x=150, y=440, width=110, height=40)

        self.btn_update = Button(self.root, command=self.update, text="Update", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2")
        self.btn_update.place(x=270, y=440, width=110, height=40)

        self.btn_delete = Button(self.root, command=self.delete,text="Delete", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2")
        self.btn_delete.place(x=390, y=440, width=110, height=40)

        self.btn_clear = Button(self.root, command=self.clear, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2")
        self.btn_clear.place(x=510, y=440, width=110, height=40)

        # =====Search Panel ========#
        self.var_search = StringVar()
        lbl_search_roll = Label(text="Roll No.", font=(
            "times new roman", 15), bg="white").place(x=750, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=(
            "goudy old style", 15), bg="lightyellow")
        txt_search_roll.place(x=900, y=60, width=220)

        btn_search = Button(self.root, command=self.search,text="Search", font=(
            "goudy old style", 15, "bold"), bg="#5e7cd2", fg="white", cursor="hand2")
        btn_search.place(x=1150, y=60, width=130, height=29)

        # =====Content======#
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=750, y=100, width=540, height=370)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.StudentTable = ttk.Treeview(self.C_Frame, columns=(
            "roll", "name", "email", "gender", "dob", "contact", "admission", "state", "city", "pin", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        self.StudentTable.heading("roll", text="Roll No.")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("dob", text="D.O.B")
        self.StudentTable.heading("contact", text="Contact")
        self.StudentTable.heading("admission", text="Admission")
        self.StudentTable.heading("state", text="State")
        self.StudentTable.heading("city", text="City")
        self.StudentTable.heading("pin", text="PIN")
        self.StudentTable.heading("address", text="Address")
        
        self.StudentTable["show"] = 'headings'
        self.StudentTable.pack(fill=BOTH, expand=1)

        self.StudentTable.column("roll", width=100)
        self.StudentTable.column("name", width=100)
        self.StudentTable.column("email", width=100)
        self.StudentTable.column("gender", width=100)
        self.StudentTable.column("dob", width=100)
        self.StudentTable.column("contact", width=100)
        self.StudentTable.column("admission", width=100)
        self.StudentTable.column("state", width=100)
        self.StudentTable.column("city", width=100)
        self.StudentTable.column("address", width=200)
        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. is Required!!", parent=self.root)
            else:
                cur.execute("select * from student where roll = %s",
                            self.var_roll.get())
                row = cur.fetchone()

                if (row == None):
                    messagebox.showerror("Error", "Select a Student from the list.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete this Student's Detail?", parent = self.root)
                    if op == True:
                        cur.execute("delete from student where roll = %s",self.var_roll.get())
                        con.commit()
                        messagebox.showinfo("Delete","Student's Details deleted successfully.", parent=self.root)
                        self.clear()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")

    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        r = self.StudentTable.focus()
        content = self.StudentTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_state.set(row[7])
        self.var_city.set(row[8])
        self.var_pin.set(row[9])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[10])

    def add(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. is Required!!", parent=self.root)
            else:
                cur.execute("select * from student where roll = %s",
                            self.var_roll.get())
                row = cur.fetchone()

                if (row != None):
                    messagebox.showerror("Error", "Student already exist.")
                else:
                    cur.execute("insert into student (roll, name, email, gender, dob, contact, admission, state, city, pin, address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Added Successfully.", parent=self.root)
                    self.show()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")

    def update(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. is Required!!", parent=self.root)
            else:
                cur.execute("select * from student where roll = %s",
                            self.var_roll.get())
                row = cur.fetchone()

                if (row == None):
                    messagebox.showerror("Error", "Select Student From List")
                else:
                    cur.execute("update student set name=%s, email=%s, gender=%s, dob=%s, contact=%s, admission=%s, state=%s, city=%s, pin=%s, address=%s where roll=%s", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Details Updated Successfully.")
                    self.show()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")

    def show(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()

            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert("", END, values=row)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")

    def search(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll = %s",self.var_search.get())
            rows = cur.fetchall()
            if rows != None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for row in rows:
                    self.StudentTable.insert("", END, values=row)
        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")


if __name__ == "__main__":

    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
