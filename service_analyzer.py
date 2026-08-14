def describe_port(port, service, status):
    service = service.strip().upper()
    status = status.strip().capitalize()
    if status == "Open":
        if service == "SSH":
            risk = "MEDIUM"
            assessment = "Review SSH exposure"
        elif service == "HTTP":
            risk = "MEDIUM"
            assessment = "Review HTTP exposure"
        elif service == "HTTPS":
            risk = "LOW"
            assessment = "Review HTTPS exposure"
        elif service == "TELNET":
            risk = "HIGH"
            assessment = "Review TELNET exposure; plaintext protocol"
        else:
            risk = "HIGH"
            assessment = "Unknown service exposure"
    elif status == "Closed":
        risk = "NONE"
        assessment = "No immediate exposure detected"
    else:
        risk = "UNKNOWN"
        assessment = "Invalid status provided"

    return risk, assessment
try:
    port = int(input("Enter port number:"))
    if port < 0 or port > 65535:
        print("Invalid port number. Please enter a value between 0 and 65535.")
    else:
        service = input("Enter service name:")
        status = input("Enter status (Open/Closed):")
    risk, assessment = describe_port(port, service, status)
    print("\nPort:", port)
    print("Service:", service)
    print("Status:", status)
    print("Risk:", risk)
    print("Assessment:", assessment)
except ValueError:
    print("Invalid input. Please enter a valid port number.")

