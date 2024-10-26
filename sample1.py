import tkinter as tk
from tkinter import messagebox
def validate_login():
  username=entry_username.get()
  password=entry_password.get()
  if username=="achuth"and password=="password":
    messagebox.showinfo("login sucess","welcome!")
  else:
      messagebox.showinfo("login failed","invalid credential.please try again....")
root=tk.Tk()
root.title("login page")
root.geometry("300x200")
label_username=tk.Label(root,text="username:")
label_username.pack(pady=10)
entry_username=tk.entry(root)
entry_username.pack(pady=5)
label_password=tk.Label(root,text="password:")
label_password.pack(pady=10)
entry_password=tk.Entry(root,show='*')
entry_password.pack(pady=5)
button_login=tk.Button(root,text="login",command=validate_login)
button_login.pack(pady=20)
root.mainloop()