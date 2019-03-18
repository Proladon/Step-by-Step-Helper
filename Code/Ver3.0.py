from tkinter import*


class Mainwin:
	def __init__(self, master):
		self.master = master
		master.attributes("-topmost",1)
		master.geometry("400x200+700+400")
		master.title("Classes Tkinter GUI")
		

		self.quit_btn = Button(text="bruh", command=self.call_diaolog)
		self.quit_btn.pack()

	def call_diaolog(self):
		class step_creater:
			def __init__(self, master2):
				self.master = master2
				master2.geometry("400x600+400+400")
				master2.title("Classes Tkinter GUI")
				
				self.quit_btn = Button(master2, text="Close", command=self.close)
				self.quit_btn.pack()
			def close(self):
				root2.destroy()
		root2 = Tk()
		win = step_creater(root2)
		root2.mainloop()


root = Tk()
win = Mainwin(root)
root.mainloop()