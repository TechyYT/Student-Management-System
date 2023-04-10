from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk
import pymysql
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window | Welcome...")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        self.root.state("zoomed")
        # ======Images====== #
        self.phone_image = ImageTk.PhotoImage(file="images/phone1.png")
        self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0)
        self.lbl_Phone_image.config(bg="white")
        self.lbl_Phone_image.place(x=290, y=95)

        # ==== Header Image ==== #
        self.header_img = ImageTk.PhotoImage(file="images/header.png")
        self.lbl_header_img = Label(self.root, image=self.header_img, bg="white").place(
            x=70, y=0, height=70, relwidth=1)
        # =====Login_Frame===== #
        login_frame = Frame(self.root, bd=2, relief=SOLID, bg="white")
        login_frame.place(x=780, y=125, width=400, height=470)

        title = Label(login_frame, text="Login", font=(
            "rog fonts", 30), bg="white", fg="#00ABE4").place(x=0, y=0, relwidth=1)

        lbl_user = Label(login_frame, text="Username", font=(
            "Book Antiqua", 18), bg="white", fg="#767171").place(x=50, y=100)
        self.txt_user = Entry(login_frame, font=(
            "times new roman", 18), bg="#ECECEC")
        self.txt_user.place(x=50, y=140, width=300)

        lbl_pass = Label(login_frame, text="Password", font=(
            "Book Antiqua", 18), bg="white", fg="#767171").place(x=50, y=210)
        self.txt_pass = Entry(login_frame, font=(
            "times new roman", 18), show="*", bg="#ECECEC")
        self.txt_pass.place(x=50, y=250, width=300)

        btn_login = Button(login_frame, text="Log In", font=("times new roman", 18, "bold"), bg="#00B0F0", activebackground="#00B0F0",
                           fg="white", activeforeground="white", cursor="hand2", command=self.login).place(x=50, y=310, width=300, height=40)

        hr = Label(login_frame, bg="lightgrey").place(
            x=50, y=380, width=300, height=2)
        or_lbl = Label(login_frame, text="OR", font=(
            "times new roman", 15, "bold"), fg="lightgrey", bg="White").place(x=175, y=370)

        btn_forget = Button(login_frame, command=self.forget_password_window, text="Forget Password?", font=("times new roman", 13),
                            bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E", cursor="hand2").place(x=130, y=410)

        # ==== register frame === #
        register_frame = Frame(self.root, bd=2, relief=SOLID, bg="white")
        register_frame.place(x=780, y=610, width=400, height=60)

        lbl_reg = Label(register_frame, text="Don't have an account ?", font=(
            "times new roman", 13), bg="white").place(x=80, y=15)
        btn_reg = Button(register_frame, text="Sign Up", font=("times new roman", 13, "bold"), command=self.reg, bg="white",
                         fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E", cursor="hand2").place(x=250, y=13)

        # ====Animation===== #
        self.im1 = ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image = Label(self.root, bg="gray")
        self.lbl_change_image.place(x=457, y=198, width=240, height=428)

        self.animate()
    
    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im

        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(1500, self.animate)

    def login(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Your Email or Password.", parent=self.root)

        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="techy", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",
                            (self.txt_user.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Email or Password is Incorrect !!")

                else:
                    self.sms()
                con.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)

    def reg(self):
        self.root.destroy()
        os.system("python register.py")

    def forget_password(self):
        if self.txt_user.get() == "" or self.cmb_quest.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror("Error","All fields are required!!", parent = self.root2)

        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="techy", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",
                            (self.txt_user.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please Fill Correct Security Details.", parent=self.root2)
                else:
                    cur.execute("update employee set password = %s where email=%s",
                            (self.txt_new_pass.get(),self.txt_user.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password Changed Successfully, Please Login with New Password.", parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)




    def forget_password_window(self):
        if self.txt_user.get() == "":
            messagebox.showerror(
                "Error", "Email required to reset your password !!", parent=self.root)

        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="techy", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s",
                            self.txt_user.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please enter a valid email to reset your password.", parent=self.root)
                else:
                    
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+550+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")

                    t = Label(self.root2, text="Forget Password", font=(
                        "rog fonts", 20), bg="white", fg="#00ABE4").place(x=0, y=10, relwidth=1)

                    # ----------------------Forget Password---------------

                    question = Label(self.root2, text="Security Question", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=120, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=(
                        "times new roman", 14), state="readonly", justify=CENTER)
                    self.cmb_quest['values'] = (
                        "Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quest.place(x=75, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=160, y=180)
                    self.txt_answer = Entry(self.root2, font=(
                        "times new roman", 15), bg="#ECECEC")
                    self.txt_answer.place(x=75, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=135, y=260)
                    self.txt_new_pass = Entry(self.root2, font=(
                        "times new roman", 15), bg="#ECECEC", show="*")
                    self.txt_new_pass.place(x=75, y=290, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password", font=(
                        "times new roman", 12, "bold"),command=self.forget_password , bg="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white")
                    btn_change_password.place(x=100, y=340, width=200)
                    

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_user.delete(0,END)
    
    def sms(self):
        self.root.destroy()
        os.system("python dashboard.py")


root = Tk()
obj = Login_System(root)
root.mainloop()