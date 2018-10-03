
#標題 、大小、ICON、顏色、透明度

from tkinter import*
#from tkinter.ttk import*

current_step1 = 0
current_step2 = 0
current_step3 = 0
hints = {
        "STEP  0": "Ver 1.0 By Proladon",
        "STEP  1": "總務 " " → " "系統採購 " " → " "許言 ",
        "STEP  2": "支付證明採購 " " → " "支付證明申請 " " → " "新增",
        "STEP  3": "預算來源 " " → " "國科會 " " → " "工作計畫",
        "STEP  4": "整筆儲存 " " → " "明細檔資料 ",
        "STEP  5": "品名 " " → " "數量:1 " " → " "預估單價" " → " "期限:今天",
        "STEP  6": "用途:研究用 " " → " "交貨地點:研究室 " " → " "其他:無",
        "STEP  7": "預算科目:業務 " " → " "新增儲存 " " → " "(複製所有)送出",
        "STEP  8": "直接採購登入 " " → " "新增 " " → " "查詢",
        "STEP  9": "√一個 " " → " "廠商:自行採購 " " → " "整筆儲存",
        "STEP  10": "採購數量:1 " " → " "儲存"  " → " "整筆儲存",
        "STEP  11": "確定 " " → " "新增 " " → " "....",
        "STEP  12": "各單位憑證資料輸入 " " → " "新增 ",
        "STEP  13": "經費來源 " " → " "國科會 " " → " "查詢",
        "STEP  14": "√一個 " " → " "下一步 " " → " "發票or收據(no key)",
        "STEP  15": "日期:今天 " " → " "編號 " " → " "金額" " → " "未付款",
        "STEP  16": "新增 " " → " "..... " " → " "支付證明書列印",
        "STEP  17": "釘上發票影本 " " → " "桌面 " " → " "會計文件表單",
        "STEP  18": "填寫憑證黏存單" " → " "發票影印2份 ",
        "STEP  19": "1份留存" " → " "1份給會計" " → " "填寫預控表 ",
        "STEP  20": "##待補##",       
        }

# Dialog Tk win
dialog = Tk()
dialog.title("Step Helper Ver2.0 (By Proladon)")
dialog.geometry("500x150")
dialog.resizable(0,0)
dialog.attributes("-topmost", 1)
#//////////////Left Pannel//////////////#
left_pannel = Frame(dialog, width=100, height=150, bg="skyblue")
left_pannel.place(x=0, y=0)
#//////////////Right Pannel//////////////#
right_pannel = Frame(dialog, width=400, height=150, bg="#575e68")
right_pannel.place(x=100, y=0)

read_me = Label(text=
"使用說明\n"+"#欲切換申報類別請先按Re按鍵重置")
read_me.config(font="微軟正黑體 12 bold")
read_me.place(x=170, y=10)
#/////////////////////////////////////#

#//////////////////Right Pannel//////////////////#
def test_1 ():
    read_me.destroy()
    #//////////////////////////////////////////////#
    def next_step():
            global current_step1
            if current_step1 < 20:
                current_step1 += 1 
                step = "STEP  " + str(current_step1)
                step2 = "STEP  " + str(current_step1)
                var.set(step)
                var2.set(hints[step2]) 

    def back_step():
            global current_step1
            if current_step1 > 0:
                current_step1 -= 1    
                step = "STEP  " + str(current_step1)
                step2 = "STEP  " + str(current_step1)
                var.set(step)
                var2.set(hints[step2])
            if current_step1 == 0:
                var.set("人事費")
                var2.set("")
    
    def reset():
            global current_step1
            current_step1 = 0
            var.set("")
            var2.set("")

    #///////////////Right Pannel Widgets///////////////#
    var = StringVar()
    var.set("人事費")
    step_lb = Label(text="", bg="#575e68", fg="white", textvariable= var)
    step_lb.place(x=280, y=10)

    var2 = StringVar()
    var2.set("")
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2)
    show_lb.place(x=150, y=50)

    next_btn = Button(text="Next", font="微軟正黑體 12")
    next_btn.config(command=next_step)
    next_btn.place(width=150, height=30, x=330, y=110)
    back_btn = Button(text="Back", font="微軟正黑體 12")
    back_btn.config(command=back_step)
    back_btn.place(width=150, height=30, x=120, y=110)
    reset_btn = Button(text="Re", font="微軟正黑體 12")
    reset_btn.config(command=reset)
    reset_btn.place(width=30, height=30, x=285, y=110)

    #//////////////////////////////////////////////#

def test_2 ():
    read_me.destroy()
    #//////////////////////////////////////////////#
    def next_step():
            global current_step2
            if current_step2 < 20:
                current_step2 += 1    
                step = "STEP  " + str(current_step2)
                step2 = "STEP  " + str(current_step2)
                var.set(step)
                var2.set(hints[step2]) 

    def back_step():
            global current_step2
            if current_step2 > 0:
                current_step2 -= 1
                step = "STEP  " + str(current_step2)
                step2 = "STEP  " + str(current_step2)
                var.set(step)
                var2.set(hints[step2])
            if current_step2 == 0:
                var.set("總務費")
                var2.set("使用說明\n"+"#欲切換申報類別請先按Re按鍵重置")
    def reset():
            global current_step2
            current_step2 = 0
            var.set("")
            var2.set("")        

    #///////////////Right Pannel Widgets///////////////#
    var = StringVar()
    var.set("總務費")
    step_lb = Label(text="", bg="#575e68", fg="white", textvariable= var)
    step_lb.place(x=280, y=10)

    var2 = StringVar()
    var2.set("#欲切換申報類別請先按Re按鍵重置")
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2)
    show_lb.place(x=150, y=50)


    next_btn = Button(text="Next", font="微軟正黑體 12")
    next_btn.config(command=next_step)
    next_btn.place(width=150, height=30, x=330, y=110)
    back_btn = Button(text="Back", font="微軟正黑體 12")
    back_btn.config(command=back_step)
    back_btn.place(width=150, height=30, x=120, y=110)
    reset_btn = Button(text="Re", font="微軟正黑體 12")
    reset_btn.config(command=reset)
    reset_btn.place(width=30, height=30, x=285, y=110)
    #//////////////////////////////////////////////#

def test_3 ():
    read_me.destroy()
    #//////////////////////////////////////////////#
    def next_step():
            global current_step3
            if current_step3 < 20:
                current_step3 += 1    
                step = "STEP  " + str(current_step3)
                step2 = "STEP  " + str(current_step3)
                var.set(step)
                var2.set(hints[step2]) 

    def back_step():
            global current_step3
            if current_step3 > 0:
                current_step3 -= 1    
                step = "STEP  " + str(current_step3)
                step2 = "STEP  " + str(current_step3)
                var.set(step)
                var2.set(hints[step2])
            if current_step3 == 0:
                var.set("待更新")
                var2.set("")

    def reset():
            global current_step3
            current_step3 = 0
            var.set("")
            var2.set("")        

    #///////////////Right Pannel Widgets///////////////#
    var = StringVar()
    var.set("待更新")
    step_lb = Label(text="", bg="#575e68", fg="white", textvariable= var)
    step_lb.place(x=280, y=10)

    var2 = StringVar()
    var2.set("")
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2)
    show_lb.place(x=150, y=50)


    next_btn = Button(text="Next", font="微軟正黑體 12")
    next_btn.config(command=next_step)
    next_btn.place(width=150, height=30, x=330, y=110)
    back_btn = Button(text="Back", font="微軟正黑體 12")
    back_btn.config(command=back_step)
    back_btn.place(width=150, height=30, x=120, y=110)
    reset_btn = Button(text="Re", font="微軟正黑體 12")
    reset_btn.config(command=reset)
    reset_btn.place(width=30, height=30, x=285, y=110)
    #//////////////////////////////////////////////#

#///////////////Left Pannel Buttons///////////////#
btn_1 = Button(left_pannel,text="人事費", font="微軟正黑體 12")
btn_1.config(command=test_1)
btn_1.place(width=80, height=30, x=10, y=10)

btn_2 = Button(left_pannel,text="總務費", font="微軟正黑體 12")
btn_2.config(command=test_2)
btn_2.place(width=80, height=30, x=10, y=60)

btn_3 = Button(left_pannel,text="多張統一", font="微軟正黑體 12")
btn_3.config(command=test_3)
btn_3.place(width=80, height=30, x=10, y=110)

#/////////////////////////////////////////////#
dialog.mainloop()

#標題 、大小、ICON、顏色、透明度

from tkinter import*
#from tkinter.ttk import*

current_step1 = 0
current_step2 = 0
current_step3 = 0
hints = {
        "STEP  0": "Ver 1.0 By Proladon",
        "STEP  1": "總務 " " → " "系統採購 " " → " "許言 ",
        "STEP  2": "支付證明採購 " " → " "支付證明申請 " " → " "新增",
        "STEP  3": "預算來源 " " → " "國科會 " " → " "工作計畫",
        "STEP  4": "整筆儲存 " " → " "明細檔資料 ",
        "STEP  5": "品名 " " → " "數量:1 " " → " "預估單價" " → " "期限:今天",
        "STEP  6": "用途:研究用 " " → " "交貨地點:研究室 " " → " "其他:無",
        "STEP  7": "預算科目:業務 " " → " "新增儲存 " " → " "(複製所有)送出",
        "STEP  8": "直接採購登入 " " → " "新增 " " → " "查詢",
        "STEP  9": "√一個 " " → " "廠商:自行採購 " " → " "整筆儲存",
        "STEP  10": "採購數量:1 " " → " "儲存"  " → " "整筆儲存",
        "STEP  11": "確定 " " → " "新增 " " → " "....",
        "STEP  12": "各單位憑證資料輸入 " " → " "新增 ",
        "STEP  13": "經費來源 " " → " "國科會 " " → " "查詢",
        "STEP  14": "√一個 " " → " "下一步 " " → " "發票or收據(no key)",
        "STEP  15": "日期:今天 " " → " "編號 " " → " "金額" " → " "未付款",
        "STEP  16": "新增 " " → " "..... " " → " "支付證明書列印",
        "STEP  17": "釘上發票影本 " " → " "桌面 " " → " "會計文件表單",
        "STEP  18": "填寫憑證黏存單" " → " "發票影印2份 ",
        "STEP  19": "1份留存" " → " "1份給會計" " → " "填寫預控表 ",
        "STEP  20": "##待補##",       
        }

# Dialog Tk win
dialog = Tk()
dialog.geometry("500x150")
dialog.resizable(0,0)
dialog.attributes("-topmost", 1)
#//////////////Left Pannel//////////////#
left_pannel = Frame(dialog, width=100, height=150, bg="skyblue")
left_pannel.place(x=0, y=0)
#//////////////Right Pannel//////////////#
right_pannel = Frame(dialog, width=400, height=150, bg="#575e68")
right_pannel.place(x=100, y=0)
#/////////////////////////////////////#

#//////////////////Right Pannel//////////////////#
def test_1 ():
    #right_pannel = Frame(dialog, width=400, height=150, bg="#575e68")
    #right_pannel.place(x=100, y=0)
    #//////////////////////////////////////////////#
    def next_step():
            global current_step1
            if current_step1 < 20:
                current_step1 += 1    
                step = "STEP  " + str(current_step1)
                step2 = "STEP  " + str(current_step1)
                var.set(step)
                var2.set(hints[step2]) 

    def back_step():
            global current_step1
            if current_step1 > 0:
                current_step1 -= 1    
                step = "STEP  " + str(current_step1)
                step2 = "STEP  " + str(current_step1)
                var.set(step)
                var2.set(hints[step2])
            if current_step1 == 0:
                var.set("人事費")
                var2.set("")
    
    def reset():
            global current_step1
            current_step1 = 0
            var.set("")
            var2.set("")

    #///////////////Right Pannel Widgets///////////////#
    var = StringVar()
    var.set("人事費")
    step_lb = Label(text="", bg="#575e68", fg="white", textvariable= var)
    step_lb.place(x=270, y=10)

    var2 = StringVar()
    var2.set("")
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2)
    show_lb.place(x=150, y=50)

    next_btn = Button(text="Next", font="微軟正黑體 12")
    next_btn.config(command=next_step)
    next_btn.place(width=150, height=30, x=330, y=110)
    back_btn = Button(text="Back", font="微軟正黑體 12")
    back_btn.config(command=back_step)
    back_btn.place(width=150, height=30, x=120, y=110)
    reset_btn = Button(text="Re", font="微軟正黑體 12")
    reset_btn.config(command=reset)
    reset_btn.place(width=30, height=30, x=285, y=110)

    #//////////////////////////////////////////////#

def test_2 ():
    right_pannel = Frame(dialog, width=400, height=150, bg="#575e68")
    right_pannel.place(x=100, y=0)
    #//////////////////////////////////////////////#
    def next_step():
            global current_step2
            if current_step2 < 20:
                current_step2 += 1    
                step = "STEP  " + str(current_step2)
                step2 = "STEP  " + str(current_step2)
                var.set(step)
                var2.set(hints[step2]) 

    def back_step():
            global current_step2
            if current_step2 > 0:
                current_step2 -= 1    
                step = "STEP  " + str(current_step2)
                step2 = "STEP  " + str(current_step2)
                var.set(step)
                var2.set(hints[step2])
            if current_step2 == 0:
                var.set("總務費")
                var2.set("")
    def reset():
            global current_step2
            current_step2 = 0
            var.set("")
            var2.set("")        

    #///////////////Right Pannel Widgets///////////////#
    var = StringVar()
    var.set("總務費")
    step_lb = Label(text="", bg="#575e68", fg="white", textvariable= var)
    step_lb.place(x=270, y=10)

    var2 = StringVar()
    var2.set("")
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2)
    show_lb.place(x=150, y=50)


    next_btn = Button(text="Next", font="微軟正黑體 12")
    next_btn.config(command=next_step)
    next_btn.place(width=150, height=30, x=330, y=110)
    back_btn = Button(text="Back", font="微軟正黑體 12")
    back_btn.config(command=back_step)
    back_btn.place(width=150, height=30, x=120, y=110)
    reset_btn = Button(text="Re", font="微軟正黑體 12")
    reset_btn.config(command=reset)
    reset_btn.place(width=30, height=30, x=285, y=110)
    #//////////////////////////////////////////////#

def test_3 ():
    right_pannel = Frame(dialog, width=400, height=150, bg="#575e68")
    right_pannel.place(x=100, y=0)
    #//////////////////////////////////////////////#
    def next_step():
            global current_step3
            if current_step3 < 20:
                current_step3 += 1    
                step = "STEP  " + str(current_step3)
                step2 = "STEP  " + str(current_step3)
                var.set(step)
                var2.set(hints[step2]) 

    def back_step():
            global current_step3
            if current_step3 > 0:
                current_step3 -= 1    
                step = "STEP  " + str(current_step3)
                step2 = "STEP  " + str(current_step3)
                var.set(step)
                var2.set(hints[step2])
            if current_step3 == 0:
                var.set("待更新")
                var2.set("")

    def reset():
            global current_step3
            current_step3 = 0
            var.set("")
            var2.set("")        

    #///////////////Right Pannel Widgets///////////////#
    var = StringVar()
    var.set("待更新")
    step_lb = Label(text="", bg="#575e68", fg="white", textvariable= var)
    step_lb.place(x=270, y=10)

    var2 = StringVar()
    var2.set("")
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2)
    show_lb.place(x=150, y=50)


    next_btn = Button(text="Next", font="微軟正黑體 12")
    next_btn.config(command=next_step)
    next_btn.place(width=150, height=30, x=330, y=110)
    back_btn = Button(text="Back", font="微軟正黑體 12")
    back_btn.config(command=back_step)
    back_btn.place(width=150, height=30, x=120, y=110)
    reset_btn = Button(text="Re", font="微軟正黑體 12")
    reset_btn.config(command=reset)
    reset_btn.place(width=30, height=30, x=285, y=110)
    #//////////////////////////////////////////////#

#///////////////Left Pannel Buttons///////////////#
btn_1 = Button(left_pannel,text="人事費", font="微軟正黑體 12")
btn_1.config(command=test_1)
btn_1.place(width=80, height=30, x=10, y=10)

btn_2 = Button(left_pannel,text="總務費", font="微軟正黑體 12")
btn_2.config(command=test_2)
btn_2.place(width=80, height=30, x=10, y=60)

btn_3 = Button(left_pannel,text="待更新", font="微軟正黑體 12")
btn_3.config(command=test_3)
btn_3.place(width=80, height=30, x=10, y=110)

#/////////////////////////////////////////////#
dialog.mainloop()

