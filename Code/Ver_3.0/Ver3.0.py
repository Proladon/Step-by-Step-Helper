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
	def modify(self):
		select = self.doc_list.curselection()
		if select != ():
			self.call_diaolog()
			# get step vaule from select doc
			counte = self.widgets
			for i in range(counte):
				pass
		else:
			war = Tk()
			war.geometry("200x50+500+450")
			lb = Label(war, text="Please select a file!")
			lb.pack()
			war.mainloop()

	def call_diaolog(self):
		class step_creater:
			def __init__(self, master2):
				self.master2 = master2
				master2.geometry("400x600+400+400")
				master2.title("Classes Tkinter GUI")
				
				self.lb_1 = Label(master2, text="How many step")
				self.lb_1.pack()
				self.ask_how_many = Spinbox(master2, from_=1, to=100)
				self.ask_how_many.pack()
				self.confirm_btn = Button(master2, text="Confirm", command=self.confirm)
				self.confirm_btn.pack()

				self.widgets = [] # Storage dynamic widgets
				self.data = {} # Storage dynamic data

			def confirm(self):
				num = self.ask_how_many.get()
				for c in range(int(num)):
					i = "entry_" + str(c)
					self.widgets.append(i)
					self.widgets[c] = Entry(self.master2)
					self.widgets[c].pack()
					
				self.btn = Button(self.master2, text="Done", command=self.close)
				self.btn.pack()

				self.confirm_btn.config(text="Reset", command=self.reset)

			def reset(self):
				counte = int(len(self.widgets))
				for i in range(counte):
					self.widgets[i].destroy()
					self.btn.destroy()
				self.data.clear()
				self.widgets.clear()
				self.confirm_btn.config(text="Confirm", command=self.confirm)

			def prt_get(self):
				counte = int(len(self.widgets))
				for i in range(counte):
					print(self.widgets[int(i)].get())

			def close(self):
				mainWin.doc_list.insert(1, "New_1")
				root2.destroy()

		root2 = Tk()
		win2 = step_creater(root2)
		root2.mainloop()




root = Tk()
mainWin = Mainwin(root)
root.mainloop()