from tkinter import*


class Mainwin:
	def __init__(self, master):
		self.master = master
		master.attributes("-topmost",1)
		master.geometry("400x250+700+400")
		master.config(bg="#252A33")
		master.title("Classes Tkinter GUI")
		
		self.doc_list = Listbox(relief=FLAT, bg="#252A33", fg="white")
		self.doc_list.place(x=10, y=0, width=120)

		self.quit_btn = Button(text="New", relief=FLAT, bg="#FD6BAD", fg="#323232", command=self.call_diaolog)
		self.quit_btn.place(x=10, y=200)
		self.quit_btn = Button(text="Modify", relief=FLAT, bg="#27F8D3", fg="#323232", command=self.modify)
		self.quit_btn.place(x=65, y=200)

#///////////////////////////////////////////////////////////////#
# Functions

	def call_diaolog(self):
		class step_creater:
			def __init__(self, master2):
				self.master = master2
				master2.geometry("400x600+400+400")
				master2.title("Classes Tkinter GUI")
				
				self.quit_btn = Button(master2, text="Done", command=self.close)
				self.quit_btn.pack()

			def close(self):
				win.doc_list.insert(1, "New_1")
				root2.destroy()
		root2 = Tk()
		win2 = step_creater(root2)
		root2.mainloop()

	def modify(self):
		pass



root = Tk()
win = Mainwin(root)
root.mainloop()