def describe_port(port, service, status):
    if status == "Open":
        if service == "SSH":
            risk = "medium"
            assessment = "Review SSH exposure"
        elif service == "HTTP":
            risk = "Medium"
            assessment = "Review HTTP exposure"
        elif service == "HTTPS":
            risk = "Low"
            assessment = "Review HTTPS exposure"
        
        else:
            risk = "High"
            assessment = "Unknown service exposure"
    else:
        risk = "None"
        assessment = "No immediate exposure detected"
    return risk, assessment
port = int(input("Enter port number:")) 
service = input("Enter the name of service (e.g. SSH, HTTP, HTTPS):").upper()
status = input("Enter the status of the port (open/closed):").capitalize()

risk, assessment = describe_port(port, service, status)

print("\n--- Security Assessment Report ---")
print(f"Port: {port}")
print(f"Service: {service}")
print(f"Status: {status}")
print(f"Risk: {risk}")
print(f"Assessment: {assessment}")