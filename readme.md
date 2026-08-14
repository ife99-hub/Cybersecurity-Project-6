Port & Service Risk Analyzer

A beginner-friendly Python cybersecurity project that analyzes network port information, identifies services, validates input, and assigns basic security risk levels based on port status and service exposure.

📌 Project Overview

The Port & Service Risk Analyzer is a Python-based security automation project created as part of my journey into Red Teaming and Purple Teaming.

The project demonstrates how Python can be used to process security-related information and automatically produce a basic risk assessment.

The analyzer accepts:

Port number
Service name
Port status

It then evaluates the information and returns:

Risk level
Security assessment
Exposure recommendation
🎯 Objectives

The main objectives of this project are to:

Practice Python programming fundamentals.
Understand functions and return values.
Work with user input.
Apply conditional logic to cybersecurity scenarios.
Learn input validation and normalization.
Understand basic port and service assessment.
Begin developing cybersecurity automation skills.
Build a practical project for a cybersecurity portfolio.
🛠️ Technologies Used
Python 3
VS Code
Git/GitHub
🔐 Security Concepts Demonstrated

This project introduces several cybersecurity concepts:

Network ports
Common network services
Open and closed ports
Service exposure
Risk classification
Basic security assessment
Input validation
Security automation
🧠 Python Concepts Used

The project currently uses:

Variables
Strings
Integers
input()
print()
Functions
Parameters
Return values
if / elif / else
String methods
.strip()
.upper()
.capitalize()
try / except
ValueError
Basic counters
📂 Project Structure
port-service-risk-analyzer/
│
├── port_risk_analyzer.py
│
└── README.md
⚙️ How It Works

The program follows this process:

User Input
    ↓
Port Validation
    ↓
Input Normalization
    ↓
Service & Status Analysis
    ↓
Risk Classification
    ↓
Security Assessment
    ↓
Result

For example:

Port: 23
Service: TELNET
Status: Open
Risk: HIGH
Assessment: Review TELNET exposure; plaintext protocol
🚀 Example

The user enters:

Enter port number: 22
Enter service name: SSH
Enter status (Open/Closed): Open

The program returns:

Port: 22
Service: SSH
Status: Open
Risk: MEDIUM
Assessment: Review SSH exposure

Another example:

Enter port number: 23
Enter service name: Telnet
Enter status (Open/Closed): Open

Result:

Port: 23
Service: TELNET
Status: Open
Risk: HIGH
Assessment: Review TELNET exposure; plaintext protocol
📊 Current Risk Logic

The current version uses basic predefined rules:

Service	Status	Risk
SSH	Open	MEDIUM
HTTP	Open	MEDIUM
HTTPS	Open	LOW
TELNET	Open	HIGH
Unknown	Open	HIGH
Any supported service	Closed	NONE

Note: These risk levels are simplified educational rules and should not be treated as a real-world vulnerability rating system. Actual risk depends on configuration, exposure, authentication, vulnerabilities, network segmentation, and other factors.

🧪 Input Validation

The program validates the port number:

if port < 0 or port > 65535:

This prevents invalid port numbers outside the valid TCP/UDP port range.

It also handles invalid numerical input using:

try:
    ...
except ValueError:

The program normalizes user input using:

service = service.strip().upper()
status = status.strip().capitalize()

This allows inputs such as:

ssh
SSH
Ssh

to be handled consistently.

🔮 Planned Improvements

This project is being developed progressively.

Planned upgrades include:

 Analyze multiple ports automatically.
 Add risk counters.
 Add open/closed port counters.
 Generate an overall security status.
 Generate a security summary.
 Store scan results.
 Read simulated Nmap results.
 Process real Nmap output in an authorized lab.
 Export assessment results to a file.
 Improve the risk classification system.
 Add logging.
 Create a more professional security report.
🎓 Learning Progression

This project is part of my Python-for-Cybersecurity learning path.

The progression is:

Python Fundamentals
       ↓
Functions
       ↓
Conditional Logic
       ↓
Security Assessment
       ↓
Input Validation
       ↓
Port & Service Analysis
       ↓
Counters & State
       ↓
Security Automation
       ↓
Nmap Data Processing
       ↓
Red Team / Purple Team Applications
⚠️ Disclaimer

This project is intended for educational and authorized cybersecurity testing purposes only.

Do not use security scanning or assessment techniques against systems, networks, or devices without proper authorization.

👨‍💻 Author

Ifeoluwa Onabowale

Cybersecurity Student | Aspiring Red Team / Purple Team Professional

GitHub description

You can use this as your repository description:

A Python cybersecurity project that analyzes network ports and services, validates input, classifies security risks, and generates basic security assessments. Built as part of my Red Team and Purple Team learning journey.

