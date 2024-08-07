import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import configparser
from tkcalendar import DateEntry
from datetime import datetime
def add_columns_to_table():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    
    # Check if user_name column exists
    cursor.execute("PRAGMA table_info(project_info)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'user_name' not in columns:
        cursor.execute("ALTER TABLE project_info ADD COLUMN user_name TEXT")
        print("Added user_name column to project_info table")
    
    if 'password' not in columns:
        cursor.execute("ALTER TABLE project_info ADD COLUMN password TEXT")
        print("Added password column to project_info table")
    
    conn.commit()
    conn.close()
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
            project_engineer TEXT,
            user_name TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()
    #add_columns_to_table()
def print_db_structure():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        print(f"\nTable: {table_name}")
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        for column in columns:
            print(f"Column: {column[1]}, Type: {column[2]}")
    conn.close()

# Call this function at the start of your application
print_db_structure()


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
        INSERT INTO project_info (date, project_no, invoice_no, serial_no, msoffice_license, project_engineer, user_name, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data['date'], data['project_no'], data['invoice_no'], data['serial_no'], data['msoffice_license'], data['project_engineer'], data['user_name'], data['password']))
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
    try:
        conn = sqlite3.connect('projects.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM project_info WHERE project_no = ?', (project_no,))
        data = cursor.fetchone()
        conn.close()
        print(f"Fetched data for project {project_no}: {data}")  # Debug print
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")  # Debug print
        return None

# GUI Application Class
class ProjectForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Information Form")

        # Date Picker
        self.date_picker = DateEntry(root, width=19, background='darkblue', foreground='white', borderwidth=2, font=("Arial", 12))
        self.date_picker.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(root, text="Date:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.project_no_var = tk.StringVar()
        self.project_no_combobox = ttk.Combobox(root, font=("Arial", 12), width=24, textvariable=self.project_no_var)
        self.project_no_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.project_no_combobox.bind("<<ComboboxSelected>>", self.load_project_data)
        tk.Label(root, font=('Arial', 12), text="Project No:").grid(row=1, column=0, padx=5, pady=5, sticky='e')

        self.invoice_no_entry = tk.Entry(root, font=("Arial", 12), width=24)
        self.invoice_no_entry.grid(row=2, column=1, padx=5, pady=5)
        tk.Label(root, font=('Arial', 12), text="Invoice No:").grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.serial_no_entry = tk.Entry(root, font=("Arial", 12), width=24)
        self.serial_no_entry.grid(row=3, column=1, padx=5, pady=5)
        tk.Label(root, font=('Arial', 12), text="Serial No:").grid(row=3, column=0, padx=5, pady=5, sticky='e')

        self.msoffice_license_entry = tk.Entry(root, font=("Arial", 12), width=24)
        self.msoffice_license_entry.grid(row=4, column=1, padx=5, pady=5)
        tk.Label(root, font=("Arial", 12), text="MS Office License:").grid(row=4, column=0, padx=5, pady=5, sticky='e')

        self.project_engineer_entry = tk.Entry(root, font=("Arial", 12), width=24)
        self.project_engineer_entry.grid(row=5, column=1, padx=5, pady=5)
        tk.Label(root, font=("Arial", 12), text="Project Engineer:").grid(row=5, column=0, padx=5, pady=5, sticky='e')

        self.user_name_entry = tk.Entry(root, font=("Arial", 12), width=24)
        self.user_name_entry.grid(row=6, column=1, padx=5, pady=5)
        tk.Label(root, font=("Arial", 12), text="User Name:").grid(row=6, column=0, padx=5, pady=5, sticky='e')

        self.password_entry = tk.Entry(root, font=("Arial", 12), width=24, show="")
        self.password_entry.grid(row=7, column=1, padx=5, pady=5)
        tk.Label(root, font=("Arial", 12), text="Password:").grid(row=7, column=0, padx=5, pady=5, sticky='e')

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.grid(row=8, column=0, columnspan=2, pady=10)

        self.save_button = tk.Button(button_frame, text="Save", width=8, height=1, bg="green", font=("Arial", 12), fg="white", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = tk.Button(button_frame, text="Delete", width=8, height=1, bg="green", font=("Arial", 12), fg="white", command=self.delete_data)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.send_email_button = tk.Button(button_frame, text="Send Email", width=12, height=1, bg="green", font=("Arial", 12), fg="white", command=self.send_email)
        self.send_email_button.pack(side=tk.LEFT, padx=5)

        self.close_button = tk.Button(button_frame, text="Close", width=8, height=1, bg="green", font=("Arial", 12), fg="white", command=root.quit)
        self.close_button.pack(side=tk.LEFT, padx=5)

        # Load Database
        setup_database()
        self.load_project_numbers()
    def send_email(self):
        messagebox.showinfo("Info", "Send email functionality not implemented soon.")    

    def load_project_numbers(self):
        project_numbers = fetch_project_numbers()
        self.project_no_combobox['values'] = project_numbers

    def load_project_data(self, event):
        project_no = self.project_no_var.get()
        data = fetch_data(project_no)
        print(f"Loaded data for project {project_no}: {data}")

        if data:
            try:
            # Date handling
                date_str = str(data[1]) if len(data) > 1 else ""
                if date_str:
                    for date_format in ['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y']:
                        try:
                            date_obj = datetime.strptime(date_str, date_format).date()
                            self.date_picker.set_date(date_obj)
                            break
                        except ValueError:
                            continue
                    else:
                        print(f"Invalid date format: {date_str}. Setting to today's date.")
                        self.date_picker.set_date(datetime.now().date())
                else:
                    print("No date data. Setting to today's date.")
                    self.date_picker.set_date(datetime.now().date())

                # Set other fields
                self.invoice_no_entry.delete(0, tk.END)
                self.invoice_no_entry.insert(0, str(data[3]) if len(data) > 3 else "")
                self.serial_no_entry.delete(0, tk.END)
                self.serial_no_entry.insert(0, str(data[4]) if len(data) > 4 else "")
                self.msoffice_license_entry.delete(0, tk.END)
                self.msoffice_license_entry.insert(0, str(data[5]) if len(data) > 5 else "")
                self.project_engineer_entry.delete(0, tk.END)
                self.project_engineer_entry.insert(0, str(data[6]) if len(data) > 6 else "")
                self.user_name_entry.delete(0, tk.END)
                self.user_name_entry.insert(0, str(data[7]) if len(data) > 7 else "")
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, str(data[8]) if len(data) > 8 else "")

                print("Data loaded successfully")
            except Exception as e:
                print(f"Error loading data: {e}")
                messagebox.showerror("Error", f"Failed to load project data: {str(e)}")
        else:
            print(f"No data found for project number: {project_no}")
            messagebox.showwarning("Warning", f"No data found for project number: {project_no}")

    def save_data(self):
        try:
            date_str = self.date_picker.get_date().strftime('%Y-%m-%d')
        except AttributeError:
            date_str = datetime.now().strftime('%Y-%m-%d')
            messagebox.showwarning("Warning", "Error getting date. Using today's date.")

        try:
            data = {
                'date': date_str,
                'project_no': self.project_no_var.get(),
                'invoice_no': self.invoice_no_entry.get(),
                'serial_no': self.serial_no_entry.get(),
                'msoffice_license': self.msoffice_license_entry.get(),
             'project_engineer': self.project_engineer_entry.get(),
             'user_name': self.user_name_entry.get(),
                'password': self.password_entry.get()
            }

            print(f"Saving data: {data}")  # Debug print
            save_to_ini(data)
            insert_data(data)
            messagebox.showinfo("Info", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
            print(f"Error details: {e}")
    
    def delete_data(self):        
        project_no = self.project_no_var.get()
        
        try:
            conn = sqlite3.connect('projects.db')
            cursor = conn.cursor()
            cursor.execute('delete FROM project_info WHERE project_no = ?', (project_no,))
            data = cursor.fetchone()
            conn.close()
            print(f"Deleted data for project {project_no}: {data}")  # Debug print 
            return data         
        except Exception as e:
            print(f"Sql_Query Failed.Error deleting data: {e}")  # Debug delete
            return None
        
# Run the application
if __name__ == "__main__":
    setup_database()
    root = tk.Tk()
    root.title("Project Information Form")
    app = ProjectForm(root)
    root.mainloop()