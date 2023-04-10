from tkinter import *
from PIL import ImageTk, Image
from student import StudentClass
from result import ResultClass
from analysis import AnalysisClass
from tkinter import messagebox
import os
import pymysql

class SMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.state("zoomed")
        self.root.config(bg="white")

        # ==== Header Image ==== #
        self.header_img = ImageTk.PhotoImage(file="images/header.png")
        self.lbl_header_img = Label(self.root, image=self.header_img, bg="white").place(
            x=70, y=0, height=60, relwidth=1)
        
        # =====Menu Frame============== #
        M_frame = LabelFrame(self.root, text="Menu", font=("times new roman",15), bg="white")
        M_frame.place(x=110,y=70, width=1310, height=80)
        
        # ===== Buttons ====== #
        btn_student = Button(M_frame, command=self.add_student, text="Student", cursor="hand2",font=("goudy old style",15,"bold"), bg="#5e7cd2", fg="white")
        btn_student.place(x=50,y=5, width=200, height=40)
        
        btn_result = Button(M_frame, command=self.add_result, text="Result", cursor="hand2",font=("goudy old style",15,"bold"), bg="#5e7cd2", fg="white")
        btn_result.place(x=300,y=5, width=200, height=40)
        
        btn_view = Button(M_frame, command=self.add_analysis, text="Results Analysis", cursor="hand2",font=("goudy old style",15,"bold"), bg="#5e7cd2", fg="white")
        btn_view.place(x=550,y=5, width=200, height=40)
        
        btn_logout = Button(M_frame, command=self.logout, text="Logout", cursor="hand2",font=("goudy old style",15,"bold"), bg="#5e7cd2", fg="white")
        btn_logout.place(x=800,y=5, width=200, height=40)
        
        btn_exit = Button(M_frame, command=self.exit, text="Exit", cursor="hand2",font=("goudy old style",15,"bold"), bg="#5e7cd2", fg="white")
        btn_exit.place(x=1050,y=5, width=200, height=40)
        
        # ====== Footer ====== #
        footer = Label(self.root, text="Student Management System\nContact Us For Technical Issue : 9193661024",font=("times new roman",12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        
        # -----Image------ #
        self.bg_img = Image.open("images/bg_sms.jpg")
        self.bg_img = self.bg_img.resize((1550,550),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg_img = Label(self.root, image=self.bg_img).place(x=0, y=180, width=1550, height=550)
        
        # === Details ===== #
        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", bd=10, relief=RIDGE, bg="#5e7cd2", fg="white", font = ("times new roman",20))
        self.lbl_student.place(x=1200, y=400, width=300, height=100)
        
        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", bd=10, relief=RIDGE, bg="#5e7cd2", fg="white", font = ("times new roman",20))
        self.lbl_result.place(x=1200, y=560, width=300, height=100)

        self.update_details()

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_analysis(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = AnalysisClass(self.new_win)

    def update_details(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="techy", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(rows))}]")
            self.lbl_student.after(200,self.update_details)

            cur.execute("select * from result")
            rows = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(rows))}]")
            
        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")


    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?")
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?")
        if op == True:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = SMS(root)
    root.mainloop()