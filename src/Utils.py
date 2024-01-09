import os

# Set the XAUTHORITY environment variable to the correct path
os.environ['XAUTHORITY'] = '/home/pi/.Xauthority'

import pyautogui

class Widget_Window:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

UI_instance = Widget_Window()


def Scale_Width_Height():
    scale = 1
    size_screen = pyautogui.size()
    width = ((size_screen.width / scale) / 683)
    height = ((size_screen.height / scale) / 400)
    return width, height

def show_widget_fullscreen(widget):
    widget.showFullScreen()
    # widget.showNormal()

class drug_List_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_list_instance = drug_List_Data()
        
class drug_Name_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_name_instance = drug_Name_Data()

class drug_ID:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_ID_instance = drug_ID()

class each_drug_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

each_drug_instance = each_drug_Data()

class each_drug_2_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

each_drug_2_instance = each_drug_2_Data()

class drug_Update_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_Update_instance = drug_Update_Data()

class drug_Update_2_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_Update_2_instance = drug_Update_2_Data()

class day_start_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

day_start_instance = day_start_Data()

class select_meal_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

select_meal_instance = select_meal_Data()

class data_checkui1_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

data_checkui1_instance = data_checkui1_Data()

class data_checkui2_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

data_checkui2_instance = data_checkui2_Data()

class data_checkui3_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

data_checkui3_instance = data_checkui3_Data()

class meal_label_text:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

meal_label_instance = meal_label_text()

class wifi_name_Data:
    def __init__(self):
        self.value = None
        
    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

wifi_name_instance = wifi_name_Data()