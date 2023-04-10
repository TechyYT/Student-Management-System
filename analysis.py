from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class AnalysisClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1522x600+0+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.grab_set()
        self.root.resizable(False, False)
        
        # =====Title =========#
        title = Label(self.root, text="Results Analysis", font=(
            "goudy old style", 20, "bold"), bg="#5e7cd2", fg="white")
        title.place(x=10, y=10, width=1503, height=40)

        # ==== Search ======== #
        self.var_search = StringVar()
        lbl_search = Label(self.root, text="Search By Roll No.", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=70, y=70)
        
        txt_search = Entry(self.root, font=(
            "goudy old style", 18, "bold"), textvariable=self.var_search, bg="lightyellow").place(x=250, y=70, width=180)
        
        btn_search = Button(self.root, text="Search", font=(
            "goudy old style", 15, "bold"), command=self.search, bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white")
        btn_search.place(x=460, y=70, width=130, height=32)

        btn_clear = Button(self.root, text="Clear", font=(
            "goudy old style", 15, "bold"), command=self.clear, bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white")
        btn_clear.place(x=600, y=70, width=130, height=32)

        btn_delete = Button(self.root, text="Delete", font=(
            "goudy old style", 15, "bold"), command=self.delete, bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white")
        btn_delete.place(x=650, y=565, width=130, height=32)


        # =====Content====== #
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=30, y=330, width=750, height=230)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.ResultTable = ttk.Treeview(self.C_Frame, columns=(
            "roll", "name", "english", "hindi", "maths", "science", "computer"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ResultTable.xview)
        scrolly.config(command=self.ResultTable.yview)

        self.ResultTable.heading("roll", text="Roll No.")
        self.ResultTable.heading("name", text="Name")
        self.ResultTable.heading("english", text="English")
        self.ResultTable.heading("hindi", text="Hindi")
        self.ResultTable.heading("maths", text="Maths")
        self.ResultTable.heading("science", text="Science")
        self.ResultTable.heading("computer", text="Computer Science")
      
        self.ResultTable["show"] = 'headings'
        self.ResultTable.pack(fill=BOTH, expand=1)

        self.ResultTable.column("roll", width=50)
        self.ResultTable.column("name", width=100)
        self.ResultTable.column("english", width=100)
        self.ResultTable.column("hindi", width=100)
        self.ResultTable.column("maths", width=100)
        self.ResultTable.column("science", width=100)
        self.ResultTable.column("computer", width=100)

        # ============= Max Marks in a subject ================= #
        lbl_txt = Label(self.root, text="Student(s) Who Got Maximum Marks In a Subject.", font=(
            "times new roman", 15, "bold"), bg="#5e7cd2", fg="white").place(x=70, y=150)
        
        lbl_subject = Label(self.root, text="Subject", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=80, y=190)
        
        self.cmb_subject  = ttk.Combobox(self.root, font=(
            "times new roman", 13), state="readonly", justify=CENTER)
        self.cmb_subject['values'] = (
            "Select", "English", "Hindi", "Maths", "Science", "Computer")
        self.cmb_subject.place(x=180, y=190, width=200)
        self.cmb_subject.current(0)

        btn_search2 = Button(self.root, text="Search", font=(
            "goudy old style", 15, "bold"), command=self.max, bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white")
        btn_search2.place(x=400, y=185, width=130, height=32)

        # ============= Overall Highest Marks ===================== #
        self.var_percentage = StringVar()
        lbl_txt2 = Label(self.root, text="Student(s) Having Overall Highest Marks.", font=(
            "times new roman", 15, "bold"), bg="#5e7cd2", fg="white").place(x=70, y=255)
        
        btn_search3 = Button(self.root, text="Get It.", font=(
            "goudy old style", 15, "bold"), command=self.highest, bg="#5e7cd2", fg="white", cursor="hand2", activebackground="#5e7cd2", activeforeground="white")
        btn_search3.place(x=450, y=253, width=130, height=32)

        lbl_percentage = Label(self.root, text="Highest Percentage", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=80, y=290)
        txt_percentage = Entry(self.root, font=(
            "goudy old style", 18, "bold"), textvariable=self.var_percentage,bg="lightyellow", state='readonly').place(x=285, y=290, width=180)
        
        # ========== Average Marks ============ #


# =========== Vertical Line ================================================ #
        vertical_line = Label(self.root, bd=0, bg="black").place(x=790,y=60, height=530, width=2)

        # ======= Analysis Part =============== #
        lbl_txt2 = Label(self.root, text="Visualization of Students Total Marks", font=(
            "times new roman", 18, "bold"), bg="#5e7cd2", fg="white").place(x=980, y=60)
        
        # ===== Calling Plot Function ==== #
        self.plot()
    
    def plot(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        total = "english+hindi+maths+science+computer"
        cur.execute(f"select name,{total} from result")
        rows = cur.fetchall()
        
        names = []
        marks = []

        for i in rows:
            names.append(i[0])
            marks.append(i[1])

        # print("Names of student : ",names)
        # print("Marks of student : ",marks)

        fig = Figure(figsize = (5, 5), dpi = 100)

        plot1 = fig.add_subplot(111)
        plot1.bar(names, marks)
        plot1.set_ylabel("Total Marks of Students")
        plot1.set_xlabel("Name of Students")
        plot1.set_title("Name of Students V/S Total Marks")

        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=920, y=90)


# ============  Functions ============================================================= #
    def search(self):
        self.var_percentage.set("")
        self.cmb_subject.current(0)

        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Enter Roll No.", parent=self.root)
            
            else:
                cur.execute("select roll,name,english,hindi,maths,science,computer from result where roll = %s",self.var_search.get())
                rows = cur.fetchall()
                if rows != None:
                    self.ResultTable.delete(*self.ResultTable.get_children())
                    for row in rows:
                        self.ResultTable.insert("", END, values=row)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}", parent = self.root)

    def max(self):
        self.var_search.set("")
        self.var_percentage.set("")
        
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            if self.cmb_subject.get() == "Select":
                messagebox.showerror("Error", "Please Select a Subject.", parent = self.root)

            else:
                sub_name = self.cmb_subject.get().lower()
                cur.execute(f"select max({sub_name}) from result",)
                max_num = cur.fetchall()
                max_num = max_num[0][0]
                cur.execute(f"select * from result where {sub_name} = {max_num}")
                rows = cur.fetchall()
                if rows != None:
                    self.ResultTable.delete(*self.ResultTable.get_children())
                    for row in rows:
                        self.ResultTable.insert("", END, values=row)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}", parent = self.root)

    def delete(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            selected_item = self.ResultTable.focus()
            item_details = self.ResultTable.item(selected_item)
            row = item_details.get('values')[0]
            
            cur.execute(f"delete from result where roll = {row}")
            messagebox.showinfo("Success","Result Deleted SuccessFully.")
            con.commit()
            self.plot()
            self.clear()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}", parent = self.root)
        con.close()

    def highest(self):
        self.var_search.set("")
        self.cmb_subject.current(0)

        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            total = "english+hindi+maths+science+computer"
            cur.execute(f"select max({total}) from result")
            sum = cur.fetchall()
            sum = sum[0][0]
            per = (sum/500)*100
            cur.execute(f"select * from result where {total} = {sum}")
            rows = cur.fetchall()
            if rows != None:
                    self.ResultTable.delete(*self.ResultTable.get_children())
                    for row in rows:
                        self.ResultTable.insert("", END, values=row)
                    self.var_percentage.set(str(per)+"%")


        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")

    def clear(self):
        self.var_search.set("")
        self.var_percentage.set("")
        self.cmb_subject.current(0)
        
        # === Clear Tree View ==== #
        for item in self.ResultTable.get_children():
            self.ResultTable.delete(item)

if __name__ == "__main__":
    root = Tk()
    obj = AnalysisClass(root)
    root.mainloop()