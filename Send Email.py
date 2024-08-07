import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

def send_email(self):
    try:
        sender_email = "rameshbabu.d@brakesindia.co.in"
        receiver_email = "mail2drb@gmail.com"
        password = "RameshP@ssword#14"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Project Information"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = f"""\
        Project Information:
        Date: {self.date_picker.get_date()}
        Project No: {self.project_no_var.get()}
        Invoice No: {self.invoice_no_entry.get()}
        Serial No: {self.serial_no_entry.get()}
        MS Office License: {self.msoffice_license_entry.get()}
        Project Engineer: {self.project_engineer_entry.get()}
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        message.attach(part1)

        # Create secure connection with server and send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")