# Forensic Email Analysis & Data Extraction Project

This project outlines a forensic workflow for capturing, analyzing, and extracting data from a simulated email incident within a Kali Linux environment.

## Phase 1: Environment Setup

### 1. The Receiver (Modern Email Server)
* Install the library: `pip install aiosmtpd`.
* Start the server: `python3 -m aiosmtpd -n -l localhost:1025`.
* Keep this terminal open and visible throughout the exercise.

### 2. The Incident (Email Sender Script)
Create a Python script named `send_email.py` containing the forensic payload.
* **Sender:** `insider@company.local`.
* **Receiver:** `external@hacker.net`.
* **Subject:** `PROJECT Z BLUEPRINTS`.
* **Attachment:** An obfuscated file containing secret coordinates.

---

## Phase 2: The Forensic Workflow

### Step 1: Capture
* Open Wireshark and double-click the `Loopback: lo` interface, as we are routing traffic through `127.0.0.1`.
* Apply the display filter at the top: `tcp.port == 1025`.
* Run the sender script using `python3 send_email.py` and click the red square to stop the capture once the packets appear.

### Step 2: Identify IPs and Domains
* Navigate to **Statistics > Endpoints** and click the **IPv4** tab.
* You will see `127.0.0.1`, which provides evidence that the "Insider" sent data to the "Hacker Server" on the same internal network.

### Step 3: Content Analysis & Manual Carving
* Right-click an SMTP packet and select **Follow > TCP Stream** to analyze the `MAIL FROM`, `RCPT TO`, and email body text.
* Locate the stolen file by finding the block of text immediately following `Content-Transfer-Encoding: base64`.
* Copy the Base64 string and decode it manually in the Kali terminal using the command: `echo "PASTE_STRING_HERE" | base64 -d`.
* This extraction will reveal the "TOP SECRET" coordinates.

### Step 4: Detecting Phishing & Suspicious Patterns
* **Keyword Match:** Search for keywords like "CONFIDENTIAL" in the packet details.
* **Unusual Port:** Note the use of port `1025` instead of the standard port `25` to evade standard firewalls.
* **Obfuscation:** Observe the use of Base64 encoding to hide the contents of the attached file.
