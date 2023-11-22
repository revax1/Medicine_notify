import tkinter as tk
from tkinter import PhotoImage
from datetime import datetime
import sqlite3
import pygame

con = sqlite3.connect('drug_detail')
cur = con.cursor()

pygame.init()
clock = pygame.time.Clock()

class PageManager:
    def __init__(self):
        self.selected_options = []
        self.selected_options_temp = []

    def set_selected_options(self, options):
        self.selected_options = options

    def get_selected_options(self):
        return self.selected_options
    
    def next_selected_option(self):
        temp = self.selected_options.pop(0)
        self.selected_options_temp.insert(0, temp)

    def back_selected_option(self):
        if self.selected_options_temp :
            temp = self.selected_options_temp.pop(0)
            self.selected_options.insert(0, temp)
            return True
        else :
            return False


class HomePage(tk.Frame):
    def __init__(self, parent, controller, page_manager):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_manager = page_manager
        self.configure(bg="#E5F9FE")  # Set background color

        main_frame = tk.Frame(self, bg="#E5F9FE")
        main_frame.pack(pady=20)

        label_frame = tk.Frame(main_frame, bg="#FFFFFF")
        label_frame.pack(side='left', padx=5)

        self.top_image = PhotoImage(file='image/Home_icon.png')
        label_image = tk.Label(label_frame, image=self.top_image, background="#FFFFFF")
        label_image.pack(side='left', padx=5)

        label = tk.Label(label_frame, text="หน้าแรก", font=('Arial', 36, 'bold'), background="#FFFFFF")
        label.pack(side='left', padx=5)

        setting_button = tk.Button(self, text="ตั้งค่าเวลาจ่ายยา", width=20,
                                        command=lambda: controller.show_frame(SettingPage),
                                        font=('Arial', 20, 'bold'), bg="#C0C0C0")
        setting_button.pack(side='left')

        # show_button = tk.Button(self, text="show", width=20,
        #                                 command=lambda: print(self.page_manager.get_selected_options()),
        #                                 font=('Arial', 20, 'bold'), bg="#C0C0C0")
        # show_button.pack(side='left')

        # Create the time and date frame
        time_date_frame = tk.Frame(self, bg="#FFFFFF")
        time_date_frame.place(x=590, y=20)

        # Create the time label
        self.time_label = tk.Label(time_date_frame, text='', font=('Arial', 16), background="#FFFFFF")
        self.time_label.pack(side='top', padx=10)

        # Create the date label
        self.date_label = tk.Label(time_date_frame, text='', font=('Arial', 16), background="#FFFFFF")
        self.date_label.pack(side='top', padx=10)

        self.update_time_and_date()
       
    def update_time_and_date(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.config(text=current_time)

        # Get the current Thai date
        thai_date = self.get_thai_date()
        self.date_label.config(text=thai_date)

        self.after(1000, self.update_time_and_date)
        
        if current_time == "00:00:00":
                print("Play Sound!!")
                pygame.mixer.init()
                pygame.mixer.music.load("onepiece.mp3")
                pygame.mixer.music.play()

    def get_thai_date(self):
        thai_months = [
            '', 'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน',
            'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม'
        ]

        today = datetime.now()
        day = today.day
        month = today.month
        year = today.year + 543  # Convert to Thai year

        thai_date = f'{day} {thai_months[month]} {year}'
        return thai_date

class SettingPage(tk.Frame):
    def __init__(self, parent, controller, page_manager):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_manager = page_manager
        self.configure(bg="#E5F9FE")

        main_frame = tk.Frame(self, bg="#E5F9FE")
        main_frame.pack(pady=20)

        label_frame = tk.Frame(main_frame, bg="#FFFFFF")
        label_frame.pack(side='left', padx=5)

        self.top_image = PhotoImage(file='image/Setting_icon.png')
        label_image = tk.Label(label_frame, image=self.top_image, background="#FFFFFF")
        label_image.pack(side='left', padx=5)

        label = tk.Label(label_frame, text="เลือกมื้อของยา", font=('Arial', 36, 'bold'), background="#FFFFFF")
        label.pack(side='top', padx=5)

        back_button = tk.Button(self, text="ย้อนกลับ", command=lambda: controller.show_frame(HomePage), font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        back_button.place(x=40, y=40)

        self.selected_options = []

        checkboxes_frame = tk.Frame(self, bg="#C0C0C0")
        checkboxes_frame.pack(anchor='nw', padx=230, pady=30)

        options = [
            "มื้อเช้า ก่อนอาหาร",
            "มื้อเช้า หลังอาหาร",
            "มื้อเที่ยง ก่อนอาหาร",
            "มื้อเที่ยง หลังอาหาร",
            "มื้อเย็น ก่อนอาหาร",
            "มื้อเย็น หลังอาหาร",
            "มื้อก่อนนอน"
        ]
        self.checkboxes = []
        self.checkbox_vars = []
        for option in options:
            checkbox_var = tk.IntVar()
            self.checkbox_vars.append(checkbox_var)
            checkbox = tk.Checkbutton(checkboxes_frame, text=option, variable=checkbox_var, onvalue=1, offvalue=0,
                                   font=('Arial', 24), padx=30, pady=3, compound='left', bg='#C0C0C0')
            checkbox.pack(anchor='w')
            self.checkboxes.append(checkbox)

        next_button = tk.Button(self, text="ถัดไป", command=self.on_next_button_click,
                                font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        next_button.place(x=680, y=500)

    def on_next_button_click(self):
        selected_options = []
        for idx, checkbox in enumerate(self.checkboxes):
            if self.checkbox_vars[idx].get() == 1:
                selected_options.append(checkbox.cget("text"))
        self.page_manager.set_selected_options(selected_options)
        check_next(self, self.controller, selected_options).check_next_page()
        

class MealPage(tk.Frame):
    def __init__(self, parent, controller, title, page_manager): 
        tk.Frame.__init__(self, parent)
        self.configure(bg="#E5F9FE")
        self.parent = parent
        self.controller = controller
        self.page_manager = page_manager
        self.meal_title = title
        
        # Create the top frame (800x100)
        top_frame = tk.Frame(self, bg="#E5F9FE", width=800, height=100)
        top_frame.pack(side='top', pady=20)

        # Create the left frame (550x500)
        left_frame = tk.Frame(self, bg="#FFFFE4", width=550, height=500, relief='groove', borderwidth=5)
        left_frame.pack(side='left', fill='both')

        # Create the right top frame (230x233)
        right_frame = tk.Frame(self, bg="#FFFFFF", width=230, height=233, relief='groove', borderwidth=5)
        right_frame.place(x=560, y=110)

        # Create the "ลบรายการ" button
        delete_button = tk.Button(self, text="ลบรายการ", command=self.delete_drug, font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        delete_button.place(x=620, y=350)
        
        # Create the right buttom frame (230x233)
        left_bottom_frame = tk.Frame(left_frame, bg="#FFFFFF", width=345, height=185, relief='groove', borderwidth=5)
        left_bottom_frame.place(x=30, y=265)
        
        # สร้างรายการแสดงชื่อยาที่ได้ถูกบันทึก
        self.drug_list = tk.Listbox(right_frame, font=('Arial', 15), width=19, height=9)
        self.drug_list.place(x=0.1)
        
        # สร้างรายการแสดงรายละเอียดของแต่ละยา
        self.drug_detail_list = tk.Listbox(left_bottom_frame, font=('Arial', 15), width=30, height=7)
        self.drug_detail_list.place(x=0.1)

        label_frame = tk.Frame(top_frame, bg="#FFFFFF")
        label_frame.pack(side='left', padx=5)
        
        ####################################### top frame ######################################### 
        self.top_image = PhotoImage(file='image/Setting_icon.png')
        label_image = tk.Label(label_frame, image=self.top_image, background="#FFFFFF")
        label_image.pack(side='left', padx=5)

        label = tk.Label(label_frame, text=title, font=('Arial', 36, 'bold'), background="#FFFFFF")
        label.pack(side='top', padx=5)
        
        back_button = tk.Button(self, text="ย้อนกลับ", command=self.go_back, font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        back_button.place(x=40, y=40)
        
        ####################################### left frame ######################################### 
        # Entry and Label
        # drug name
        self.label_drugname = tk.Label(left_frame, text='ชื่อยา:', font=('Arial', 20, 'bold'), background="#FFFFE4")
        self.label_drugname.place(x=70, y=50)
        self.entry_drugname = tk.Entry(left_frame, width=22, bd=4, font=('Arial', 20, 'bold'))
        self.entry_drugname.place(x=160, y=50)
        # drug describe
        self.label_describe = tk.Label(left_frame, text='คำอธิบาย:', font=('Arial', 20, 'bold'), background="#FFFFE4")
        self.label_describe.place(x=30, y=120)
        self.entry_describe = tk.Entry(left_frame, width=22, bd=4, font=('Arial', 20, 'bold'))
        self.entry_describe.place(x=160, y=120)
        # เพิ่มชื่อยา
        add_button = tk.Button(left_frame, text='บันทึกชื่อยา', command=self.add_drug, font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        add_button.place(x=250, y=200)

        next_button = tk.Button(left_frame, text="ถัดไป", command=self.go_next, font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        next_button.place(x=430, y=400)
        
        ####################################### right frame ########################################
        self.displayDrug()

    def displayDrug(self):
        drug_status = self.meal_title
        drugs = cur.execute("SELECT * FROM drug WHERE drug_status=?", (drug_status,)).fetchall()
        count = 1
        
        self.drug_list.delete(0, tk.END)      # ลบข้อมูลที่อยู่ในตัวอักษรทั้งหมดในเวิร์ดี้

        for drug in drugs:
            drug_info = f" {count}. {drug[1]}"
            self.drug_list.insert(tk.END, drug_info)
            count += 1
            
        def on_drug_selected(event):
            # ฟังก์ชันนี้จะถูกเรียกเมื่อมีการเลือกรายการใน Listbox
            selected_index = self.drug_list.curselection()
            if selected_index:
                selected_index = selected_index[0]
                drug_name, drug_describe = drugs[selected_index][1], drugs[selected_index][2]
                # แสดงข้อมูลยาใน drug_detail_list
                self.show_drug_detail(drug_name, drug_describe)
                
        # เพิ่ม event handler ในการตรวจจับการคลิกแต่ละรายการใน Listbox
        self.drug_list.bind("<<ListboxSelect>>", on_drug_selected)

    def show_drug_detail(self, drug_name, drug_describe):
        # ล้างรายการที่แสดงใน drug_detail_list ก่อนแสดงใหม่
        self.drug_detail_list.delete(0, tk.END)

        # เพิ่มข้อมูลยาใน drug_detail_list
        self.drug_detail_list.insert(0, f"      ชื่อยา: {drug_name}")
        self.drug_detail_list.insert(1, f" คำอธิบาย: {drug_describe}")

            
    ########################################### fucntion ###########################################
    def add_drug(self):
        drug_name = self.entry_drugname.get()
        drug_describe = self.entry_describe.get()
        drug_status = self.meal_title

        if drug_name != "" and (drug_describe != "" or drug_describe == ""):
            print(f"ยา{drug_status} ได้ถูกบันทึก")
            try:
                query = "INSERT INTO 'drug' (drug_name, drug_describe, drug_status) VALUES (?,?,?)"
                cur.execute(query, (drug_name, drug_describe, drug_status))
                con.commit()
                print("บันทึกสำเร็จ")

                self.entry_drugname.delete(0, tk.END)
                self.entry_describe.delete(0, tk.END)

                # Update and display the drug list immediately
                self.displayDrug()

            except:
                print("บันทึกไม่สำเร็จ")
        else:
            print("โปรดใส่ชื่อยา")
            
    def delete_drug(self):
        selected_index = self.drug_list.curselection()
        if selected_index:
            selected_index = selected_index[0]
            drug_name = self.drug_list.get(selected_index).split(". ")[1]

            # ลบรายการยาที่ผู้ใช้เลือกออกจากฐานข้อมูล
            query = "DELETE FROM drug WHERE drug_name=?"
            cur.execute(query, (drug_name,))
            con.commit()

            # ลบรายการยาที่เลือกออกจาก drug_list และแสดงรายการยาใหม่ที่เหลือ
            self.drug_list.delete(selected_index)
            self.displayDrug()

    def go_back(self):
        check = self.page_manager.back_selected_option()
        if check:
            selected_options = self.page_manager.get_selected_options()
            check_next(self, self.controller, selected_options).check_next_page()
            self.displayDrug()  # แสดงรายการยาที่ถูกบันทึกในหน้าย่อยก่อนหน้านี้
        else:
            self.controller.show_frame(SettingPage)
            

    def go_next(self):
        selected_options = self.page_manager.get_selected_options()
        self.page_manager.next_selected_option()
        check_next(self, self.controller, selected_options).check_next_page()
        self.displayDrug()  # แสดงรายการยาที่ถูกบันทึกในหน้าย่อยถัดไป

class bbPage(MealPage):
    def __init__(self, parent, controller, page_manager): 
        super().__init__(parent, controller, "มื้อเช้า ก่อนอาหาร", page_manager) 
        
class abPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อเช้า หลังอาหาร", page_manager)  

class blPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อเที่ยง ก่อนอาหาร", page_manager)  

class alPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อเที่ยง หลังอาหาร", page_manager)

class bdPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อเย็น ก่อนอาหาร", page_manager)

class adPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อเย็น หลังอาหาร", page_manager)


class bbedPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อก่อนนอน", page_manager)


class check_next():
    def __init__(self, parent, controller, selected_options):
        self.parent = parent
        self.controller = controller
        self.selected_options = selected_options

    def check_next_page(self):
        if 'มื้อเช้า ก่อนอาหาร' in self.selected_options:
            self.go_next_page(bbPage)

        elif 'มื้อเช้า หลังอาหาร' in self.selected_options:
            self.go_next_page(abPage)
            
        elif 'มื้อเที่ยง ก่อนอาหาร' in self.selected_options:
            self.go_next_page(blPage)

        elif 'มื้อเที่ยง หลังอาหาร' in self.selected_options:
            self.go_next_page(alPage)

        elif 'มื้อเย็น ก่อนอาหาร' in self.selected_options:
            self.go_next_page(bdPage)

        elif 'มื้อเย็น หลังอาหาร' in self.selected_options:
            self.go_next_page(adPage)

        elif 'มื้อก่อนนอน' in self.selected_options:
            self.go_next_page(bbedPage)

    def go_next_page(self, next_page):
        self.controller.show_frame(next_page)

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.page_manager = PageManager()  # สร้างตัวจัดการหน้าต่าง
        self.geometry('800x600')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, SettingPage, bbPage, abPage, blPage, alPage, bdPage, adPage, bbedPage):
            frame = F(container, self, self.page_manager)  # ส่ง page_manager เข้าไปให้ทุกคลาส
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
