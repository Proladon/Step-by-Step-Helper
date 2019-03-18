from tkinter import*


class Top1:
	def __init__(self, master):
		self.master = master
		master.geometry("400x200+700+400")
		master.title("Classes Tkinter GUI")
		
		self.quit_btn = Button(text="Close", command=master.quit)
		self.quit_btn.pack()

		self.quit_btn = Button(text="bruh", command=self.wee)
		self.quit_btn.pack()

	def wee(self):
		class Top2:
			def __init__(self, master2):
				self.master = master2
				master2.geometry("400x200+700+400")
				master2.title("Classes Tkinter GUI")
				
				self.quit_btn = Button(master2, text="Close", command=self.close)
				self.quit_btn.pack()
			def close(self):
				root2.destroy()

		root2 = Tk()
		win = Top2(root2)
		root2.mainloop()


root = Tk()
win = Top1(root)
root.mainloop()