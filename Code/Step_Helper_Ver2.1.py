
#標題 、大小、ICON、顏色、透明度

from tkinter import*
#from tkinter.ttk import*

current_step1 = 0
current_step2 = 0
current_step3 = 0
hints_1 = {
        "STEP  0": "Ver 2.1 By Proladon",
        "STEP  1": "## 人事費步驟待更新 ##",          
        }

hints_2 = {
        "STEP  0": "Ver 2.1 By Proladon",
        "STEP  1": "總務" " → " "請採購系統" " → " "許言",
        "STEP  2": "總務請採購系統 " " → " "支付證明採購 ",
        "STEP  3": "支付證明申請" " → " "新增",
        "STEP  4": "預算來源 & 工作計劃(根據專案選擇)",
        "STEP  5": "整筆儲存" " → " "明細檔案資料",
        "STEP  6": "預算科目" " → " "業務" " → " "規格 & 廠牌 & 單位" " → "  "無",
        "STEP  7": "預估單價(發票總金額)" " → " "履約期限" " → " "今天",
        "STEP  8": "品名(發票購物項目)" " → " "數量" " → " "1",
        "STEP  9": "用途" " → " "研究用" " → " "交貨地點" " → " "研究室",
        "STEP  10": "如有多張發票，直接此頁面重複 STEP6 ~ STEP9",
        "STEP  11": "新增儲存" " → " "送出(重要)",
        "STEP  12": "直接採購登入" " → " "新增" " → " "查詢(下方)",
        "STEP  13": "√一個" " → " "下一步" " → " "廠商" " → " "使用者自行採購",
        "STEP  14": "整筆儲存(跳出錯誤訊息)" " → " "確定",
        "STEP  15": "採購數量(下方明細資料)" " → " "1" " → " "儲存" " → " "整筆儲存",
        "STEP  16": "各單位憑證資料輸入" " → " "新增",
        "STEP  17": "經費來源(根據專案選擇)" " → " "查詢(下方)",
        "STEP  18": "√一個" " → " "下一步" " → " "發票or收據",
        "STEP  19": "憑證編號(發票上的編碼)" " → " "憑證日期" " → " "今天",
        "STEP  20": "金額(發票總金額)" " → " "未付款:付款對象" " → " "許言",
        "STEP  21": "新增" " → " "完成憑證製單(重要)",
        "STEP  22": "如有多張發票重複 STEP16 ~ STEP21",
        "STEP  23": "支付證明書列印" " → " "新增" " → " "列印支付證明書(只會彈出一次)",
        "STEP  24": "回到電腦桌面" " → " "會計文件表單資料夾" " → " "支出憑證黏存單",
        "STEP  25": "發票影印(印兩份一份留存)、填寫預控表、蓋章",       
        }

# Dialog Tk win
dialog = Tk()
dialog.title("Step Helper Ver2.1 (By Proladon)")
dialog.geometry("550x150")
dialog.resizable(0,0)
dialog.attributes("-topmost", 1)
#//////////////Left Pannel//////////////#
left_pannel = Frame(dialog, width=100, height=150, bg="skyblue")
left_pannel.place(x=0, y=0)
#//////////////Right Pannel//////////////#
right_pannel = Frame(dialog, width=450, height=150, bg="#575e68")
right_pannel.place(x=100, y=0)

read_me = Label(text=
"使用說明\n"+"#欲切換申報類別請先按Re按鍵重置")
read_me.config(font="微軟正黑體 12 bold")
read_me.place(x=190, y=10)
#/////////////////////////////////////#


#//////////////////Right Pannel//////////////////#
def test_1 ():
    read_me.destroy()
    #//////////////////////////////////////////////#
    def next_step():
            global current_step1
            if current_step1 < 25:
                current_step1 += 1 
                step = "STEP  " + str(current_step1)
                step2 = "STEP  " + str(current_step1)
                var.set(step)
                var2.set(hints_1[step2]) 

    def back_step():
            global current_step1
            if current_step1 > 0:
                current_step1 -= 1    
                step = "STEP  " + str(current_step1)
                step2 = "STEP  " + str(current_step1)
                var.set(step)
                var2.set(hints_1[step2])
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
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2, font="微軟正黑體 12 bold")
    show_lb.place(x=120, y=50)

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
            if current_step2 < 25:
                current_step2 += 1    
                step = "STEP  " + str(current_step2)
                step2 = "STEP  " + str(current_step2)
                var.set(step)
                var2.set(hints_2[step2]) 

    def back_step():
            global current_step2
            if current_step2 > 0:
                current_step2 -= 1
                step = "STEP  " + str(current_step2)
                step2 = "STEP  " + str(current_step2)
                var.set(step)
                var2.set(hints_2[step2])
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
    show_lb = Label(text="", bg="#575e68", fg="white", textvariable= var2, font="微軟正黑體 12 bold")
    show_lb.place(x=120, y=50)


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

#/////////////////////////////////////////////#
dialog.mainloop()
