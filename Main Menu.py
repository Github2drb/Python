# python
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.state('zoomed')  # Maximize the window
        self.create_widgets()

    def create_widgets(self):
        self.auto_test_button = tk.Button(self,text="Auto Test", command=self.open_auto_test)
        self.auto_test_button.pack(pady=20)

        self.setting_mode_button = tk.Button(self, text="Setting Mode", command=self.setting_mode)
        self.setting_mode_button.pack(pady=20)

        self.sensor_calibration_button = tk.Button(self, text="Sensor Calibration", command=self.sensor_calibration)
        self.sensor_calibration_button.pack(pady=20)
        self.sensor_calibration_button.place(x=100,y=250)

        self.parameters_button = tk.Button(self, text="Parameters", command=self.parameters)
        self.parameters_button.pack(pady=20)

    def open_auto_test(self):
        self.auto_test_window = AutoTestWindow(self)

    def setting_mode(self):
        self.setting_mode_window = SettingModeWindow(self)

    def sensor_calibration(self):
        self.sensor_calibration_window=SensorCalibrationWindow(self)

    def parameters(self):
        self.parameters_window=ParametersWindow(self)

class AutoTestWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Auto Test Module")
        self.state('zoomed')
        #self.geometry("800x600")  # Set size for the auto test window
        self.create_widgets()

    def create_widgets(self):
        self.previous_button = tk.Button(self, text="Previous", command=self.on_previous_button_click)
        self.previous_button.pack(pady=20)
        
    def on_previous_button_click(self):
        self.destroy()  # Close the auto test window

class SettingModeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Setting Mode")
        self.state('zoomed')
        self.create_widgets()
        
    def create_widgets(self):
        self.previous_button = tk.Button(self, text="Previous", command=self.on_previous_button_click_set)
        self.previous_button.pack(pady=20)
        
       
    def on_previous_button_click_set(self):
        self.destroy()  # Close the setting mode window
        
class SensorCalibrationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sensor Calibration")
        self.state('zoomed')  # Set size for the auto test window
        self.create_widgets()

    def create_widgets(self):
        self.previous_button = tk.Button(self, text="Previous", command=self.on_previous_button_click_SC)
        self.previous_button.pack(pady=20)
        
    def on_previous_button_click_SC(self):
        self.destroy()  # Close the auto test window   
        
class ParametersWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Parameters")
        self.state('zoomed')  # Set size for the auto test window
        self.create_widgets()

    def create_widgets(self):
        self.previous_button = tk.Button(self, text="Previous", command=self.on_previous_button_click_param)
        self.previous_button.pack(pady=20)
        
    def on_previous_button_click_param(self):
        self.destroy()  # Close the auto test window                    

if __name__ == "__main__":
    app = Application()
    app.mainloop()

