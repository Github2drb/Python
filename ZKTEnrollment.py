from zk import ZK, const
import tkinter as tk
from tkinter import messagebox

# Configuration
ip = '192.168.1.201'  # Replace with your device's IP address
port = 4370  # Default port for ZKTeco devices

class EnrollmentApp:
    def __init__(self, master):
        self.master = master
        master.title("ZKTeco User Enrollment")
        master.geometry("300x150")

        tk.Label(master, text="User ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(master, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(master, text="Password:").grid(row=2, column=0, sticky="e", padx=5, pady=5)

        self.user_id_entry = tk.Entry(master)
        self.name_entry = tk.Entry(master)
        self.password_entry = tk.Entry(master, show="*")

        self.user_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(master, text="Enroll", command=self.enroll_user).grid(row=3, column=0, columnspan=2, pady=10)

    def enroll_user(self):
        user_id = self.user_id_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()

        if not user_id or not name:
            messagebox.showerror("Error", "User ID and Name are required!")
            return

        zk = ZK(ip, port=port, timeout=5)
        
        try:
            conn = zk.connect()
            print(f"Connection to {ip} successful")

            conn.disable_device()

            user = conn.set_user(uid=user_id, name=name, password=password, user_id=user_id)
            
            if user:
                messagebox.showinfo("Success", f"User enrolled successfully:\nID={user.user_id}\nName={user.name}")
            else:
                messagebox.showerror("Error", "Failed to enroll user")

            # Verify enrollment
            users = conn.get_users()
            for user in users:
                if user.user_id == user_id:
                    print(f"Verified: User {user.user_id} ({user.name}) is in the device")
                    break
            else:
                print("Warning: User not found in device after enrollment")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        finally:
            if conn:
                conn.enable_device()
                conn.disconnect()
                print("Disconnected from device")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnrollmentApp(root)
    root.mainloop()