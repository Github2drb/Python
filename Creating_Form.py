import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import configparser
from tkcalendar import DateEntry

# Database setup
def setup_database():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS project_info (
            id INTEGER PRIMARY KEY,
            date TEXT,
            project_no TEXT,
            invoice_no TEXT,
            serial_no TEXT,
            msoffice_license TEXT,
            project_engineer TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Save data to config file
def save_to_ini(data):
    config = configparser.ConfigParser()
    config['ProjectInfo'] = data
    with open('info.ini', 'w') as configfile:
        config.write(configfile)

# Insert data into database
def insert_data(data):
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO project_info (date, project_no, invoice_no, serial_no, msoffice_license, project_engineer)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data['date'], data['project_no'], data['invoice_no'], data['serial_no'], data['msoffice_license'], data['project_engineer']))
    conn.commit()
    conn.close()

# Fetch project numbers from the database
def fetch_project_numbers():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT project_no FROM project_info')
    project_numbers = [row[0] for row in cursor.fetchall()]
    conn.close()
    return project_numbers

# Fetch data based on project_no
def fetch_data(project_no):
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM project_info WHERE project_no = ?', (project_no,))
    return cursor.fetchone()

# GUI Application Class
class ProjectForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Information Form")

        # Form Fields
        #self.date_entry = tk.Entry(root,width=20,font=("Arial", 12))
        self.date_picker = DateEntry(root, width=19, background='darkblue', foreground='white', borderwidth=2, font=("Arial", 12),date_patern ='dd-mm-yyyy')
        self.date_picker.grid(row=0, column=1)
        tk.Label(root, text="Date:").grid(row=0, column=0)

        self.project_no_var = tk.StringVar()
        self.project_no_combobox = ttk.Combobox(root,font=("Arial", 12),width=24,justify='center', textvariable=self.project_no_var)
        self.project_no_combobox.place(x=250,y=60,anchor='center')
        self.project_no_combobox.bind("<<ComboboxSelected>>", self.load_project_data)
        tk.Label(root,font=('Arial',12), text="Project No:").place(x=75,y=60,anchor='center')

        self.invoice_no_entry = tk.Entry(root,font=("Arial", 12),width=24,justify='center')
        self.invoice_no_entry.place(x=250,y=100,anchor='center')
        tk.Label(root,font=('Arial',12), text="Invoice No:").place(x=75,y=100,anchor='center')

        self.serial_no_entry = tk.Entry(root,font=("Arial", 12),width=24,justify='center')
        self.serial_no_entry.place(x=250,y=140,anchor='center')
        tk.Label(root,font=('Arial',12), text="Serial No:").place(x=75,y=140,anchor='center')

        self.msoffice_license_entry = tk.Entry(root,font=("Arial", 12),width=24,justify='center')
        self.msoffice_license_entry.place(x=250,y=180,anchor='center')
        tk.Label(root,font=("Arial", 12), text="MS Office License:").place(x=75,y=180,anchor='center')

        self.project_engineer_entry = tk.Entry(root,font=("Arial", 12),justify='center')
        self.project_engineer_entry.place(x=250,y=220,anchor='center')
        #self.project_engineer_entry.grid(row=5, column=1)
        tk.Label(root,font=("Arial", 12), text="Project Engineer:").place(x=75,y=220,anchor='center')

        # Buttons
        self.save_button = tk.Button(root, text="Save",width=8,height=1,bg="green",font=("Arial", 12),fg="white", command=self.save_data)
        self.save_button.grid(row=18, column=0)
        self.save_button.place(x=45,y=273,anchor='center')

        self.send_email_button = tk.Button(root, text="Send Email",width=12,height=1,bg="green",font=("Arial", 12),fg="white", command=self.send_email)
        #self.send_email_button.grid(row=18, column=1)
        self.send_email_button.place(x=202,y=273,anchor='center')

        self.close_button = tk.Button(root, text="Close",width=8,height=1,bg="green",font=("Arial", 12),fg="white", command=root.quit)
        self.close_button.place(x=352,y=273,anchor='center')
        #self.close_button.grid(row=18, column=2)

        # Load Database
        setup_database()
        self.load_project_numbers()

    def load_project_numbers(self):
        project_numbers = fetch_project_numbers()
        self.project_no_combobox['values'] = project_numbers

    def load_project_data(self, event):
        project_no = self.project_no_var.get()
        data = fetch_data(project_no)
        if data:
            #self.date_entry.delete(0, tk.END)
            #self.date_entry.insert(0, data[1])
            self.date_picker.set_date(data[1])
            self.invoice_no_entry.delete(0, tk.END)
            self.invoice_no_entry.insert(0, data[3])
            self.serial_no_entry.delete(0, tk.END)
            self.serial_no_entry.insert(0, data[4])
            self.msoffice_license_entry.delete(0, tk.END)
            self.msoffice_license_entry.insert(0, data[5])
            self.project_engineer_entry.delete(0, tk.END)
            self.project_engineer_entry.insert(0, data[6])

    def save_data(self):
        data = {
            'date': self.date_picker.get_date().strftime('%Y-%m-%d'),
            #'date': self.date_entry.get(),
            'project_no': self.project_no_var.get(),
            'invoice_no': self.invoice_no_entry.get(),
            'serial_no': self.serial_no_entry.get(),
            'msoffice_license': self.msoffice_license_entry.get(),
            'project_engineer': self.project_engineer_entry.get()
        }

        save_to_ini(data)
        insert_data(data)
        messagebox.showinfo("Info", "Data saved successfully!")

    def send_email(self):
        # Here you would implement email sending logic
        messagebox.showinfo("Info", "Send email functionality not implemented.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Window With a Title Bar")
    root.geometry("400x300+300+120")
    app = ProjectForm(root)
    root.mainloop()
