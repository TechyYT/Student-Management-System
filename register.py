from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration | Welcome...")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        self.root.state("zoomed")
        # ======Images====== #
        self.phone_image = ImageTk.PhotoImage(file="images/phone1.png")
        self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0)
        self.lbl_Phone_image.config(bg="white")
        self.lbl_Phone_image.place(x=130, y=95)

        # ==== Header Image ==== #
        self.header_img = ImageTk.PhotoImage(file="images/header.png")
        self.lbl_header_img = Label(self.root, image=self.header_img, bg="white").place(
            x=70, y=0, height=70, relwidth=1)

        # ====Animation===== #
        self.im1 = ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image = Label(self.root, bg="gray")
        self.lbl_change_image.place(x=297, y=198, width=240, height=428)

        self.animate()

        # === Registration Frame ====#
        frame1 = Frame(self.root, bg="white", bd=2,
                       relief=SOLID, width=700, height=550)
        frame1.place(x=650, y=140)

        title = Label(frame1, text="Register Here", font=(
            "rog fonts", 35), bg="white", fg="#00ABE4").place(x=105, y=20)

        # --------------------ROW-1-----------------
        f_name = Label(frame1, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=120)
        self.txt_fname = Entry(frame1, font=(
            "times new roman", 15), bg="#ECECEC")
        self.txt_fname.place(x=50, y=160, width=250)

        l_name = Label(frame1, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=390, y=120)
        self.txt_lname = Entry(frame1, font=(
            "times new roman", 15), bg="#ECECEC")
        self.txt_lname.place(x=390, y=160, width=250)

        # ---------------------ROW-2----------------
        contact = Label(frame1, text="Contact No.", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=200)
        self.txt_contact = Entry(frame1, font=(
            "times new roman", 15), bg="#ECECEC")
        self.txt_contact.place(x=50, y=240, width=250)

        email = Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=390, y=200)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="#ECECEC")
        self.txt_email.place(x=390, y=240, width=250)

        # ----------------------ROW-3---------------
        question = Label(frame1, text="Security Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=280)
        self.cmb_quest = ttk.Combobox(frame1, font=(
            "times new roman", 14), state="readonly", justify=CENTER)
        self.cmb_quest['values'] = (
            "Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=320, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=390, y=280)
        self.txt_answer = Entry(frame1, font=(
            "times new roman", 15), bg="#ECECEC")
        self.txt_answer.place(x=390, y=320, width=250)

        # -------------------ROW-4-----------------
        password = Label(frame1, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=360)
        self.txt_password = Entry(frame1, font=(
            "times new roman", 15), bg="#ECECEC", show="*")
        self.txt_password.place(x=50, y=400, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=390, y=360)
        self.txt_cpassword = Entry(frame1, font=(
            "times new roman", 15), bg="#ECECEC", show="*")
        self.txt_cpassword.place(x=390, y=400, width=250)

        # -----------Terms-----------
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms and Conditions.", onvalue=1, offvalue=0, variable=self.var_chk, font=(
            "times new roman", 12,), bg="white", activebackground="white").place(x=50, y=440)
        btn_register = Button(frame1, text="Register Now", command=self.register_data, font=("times new roman", 18, "bold"), bg="#00B0F0",
                              activebackground="#00B0F0", fg="white", activeforeground="white", cursor="hand2", justify=CENTER).place(x=50, y=480, width=250, height=40)

        # -----------Login-----------
        f_login = Label(self.root, text="If Already Registered", font=(
            "times new roman", 15), bg="white").place(x=1100, y=710)
        btn_login = Button(self.root, text="Sign In", font=("times new roman", 15, "bold"), activebackground="white",
                           command=self.login, bg="white", bd=0, fg="#00759E", activeforeground="#00759E", cursor="hand2", justify=CENTER).place(x=1280, y=706)

    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im

        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(1500, self.animate)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    def register_data(self):
        if (self.txt_fname.get() == "" or
                self.txt_contact.get() == "" or
                self.txt_email.get() == "" or
                self.cmb_quest.get() == "Select" or
                self.txt_answer.get() == "" or
                self.txt_password.get() == "" or
                self.txt_cpassword.get() == ""):
            messagebox.showerror(
                "Error", "All Fields Are Required !!", parent=self.root)

        elif (self.txt_password.get() != self.txt_cpassword.get()):
            messagebox.showerror(
                "Error", "Password and Confirm Password should be same.", parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror(
                "Error", "Please Agree to our Terms and Conditions.")
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="techy", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee where email = %s",self.txt_email.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                            "Error", "User Already Exist, Please try with another email.")
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                )
                                )
                    con.commit()
                    con.close()
                    self.clear()
                    self.login()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def login(self):
        self.root.destroy()
        os.system("python login.py")


root = Tk()
obj = Login_System(root)
root.mainloop()