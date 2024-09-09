import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.state('zoomed')  # Maximize the window
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.auto_test_button = tk.Button(self, text="Auto Test", command=self.auto_test)
        self.setting_mode_button = tk.Button(self, text="Setting Mode", command=self.setting_mode)
        self.sensor_calibration_button = tk.Button(self, text="Sensor Calibration", command=self.sensor_calibration)
        self.parameters_button = tk.Button(self, text="Parameters", command=self.parameters)
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_application)

        self.auto_test_button.grid(row=0, column=0, padx=20, pady=20)
        self.setting_mode_button.grid(row=0, column=1, padx=20, pady=20)
        self.sensor_calibration_button.grid(row=1, column=0, padx=20, pady=20)
        self.parameters_button.grid(row=1, column=1, padx=20, pady=20)
        self.exit_button.grid(row=2, columnspan=2, pady=20)

    def auto_test(self):
        self.clear_window()
        self.auto_test_screen()

    def auto_test_screen(self):
        self.auto_test_label = tk.Label(self, text="Auto Test Module")
        self.auto_test_label.pack(pady=20)

        self.previous_button = tk.Button(self, text="Previous", command=self.close)
        self.previous_button.pack(pady=20)

    def setting_mode(self):
        messagebox.showinfo("Info", "Setting Mode Module")

    def sensor_calibration(self):
        messagebox.showinfo("Info", "Sensor Calibration Module")

    def parameters(self):
        messagebox.showinfo("Info", "Parameters Module")

    def exit_application(self):
        self.quit()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
    def close(self):
        self.destroy()        

if __name__ == "__main__":
    app = Application()
    app.mainloop()
