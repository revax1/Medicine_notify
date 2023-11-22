import tkinter as tk
from tkinter import PhotoImage
from datetime import datetime

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

        main_frame = tk.Frame(self, bg="#E5F9FE")
        main_frame.pack(pady=20)

        label_frame = tk.Frame(main_frame, bg="#FFFFFF")
        label_frame.pack(side='left', padx=5)

        self.top_image = PhotoImage(file='image/Setting_icon.png')
        label_image = tk.Label(label_frame, image=self.top_image, background="#FFFFFF")
        label_image.pack(side='left', padx=5)

        label = tk.Label(label_frame, text=title, font=('Arial', 36, 'bold'), background="#FFFFFF")
        label.pack(side='top', padx=5)

        # Add the Next and Back buttons
        back_button = tk.Button(self, text="ย้อนกลับ", command=self.go_back, font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        back_button.place(x=40, y=40)

        next_button = tk.Button(self, text="ถัดไป", command=self.go_next, font=('Arial', 16, 'bold'), bg="#C0C0C0", fg="black")
        next_button.place(x=680, y=500)

    def go_back(self):
        check = self.page_manager.back_selected_option()
        if check :
            selected_options = self.page_manager.get_selected_options()
            check_next(self.parent, self.controller, selected_options).check_next_page()
        else :
            self.controller.show_frame(SettingPage)    

    def go_next(self):
        selected_options = self.page_manager.get_selected_options()
        self.page_manager.next_selected_option()
        check_next(self.parent, self.controller, selected_options).check_next_page()

class bbPage(MealPage):
    def __init__(self, parent, controller, page_manager): 
        super().__init__(parent, controller, "มื้อเช้า ก่อนอาหาร", page_manager) 
class abPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อเช้า หลังอาหาร", page_manager)  

class blPage(MealPage):
    def __init__(self, parent, controller, page_manager):  
        super().__init__(parent, controller, "มื้อเที่ยง ก่อนอาหาร", page_manager)  

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
