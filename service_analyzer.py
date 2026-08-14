def describe_port(port, service, status):
    if status == "open":
        if service == "SSH":
            assessment = "Review SSH exposure"
        elif service == "HTTP":
            assessment = "Review HTTP exposure"
        elif service == "HTTPS":
            assessment = "Review HTTPS exposure"
        else:
            assessment = "Unknown service exposure"
    else:
        assessment = "No immediate exposure detected"
    return assessment
port = int(input("Enter port number:"))
service = input("Enter the name of service (e.g. SSH, HTTP, HTTPS):").upper()
status = input("Enter the status of the port (open/closed):").capitalize()

assessment = describe_port(port, service, status)

print("\n--- Security Assessment Report ---")
print(f"Port: {port}")
print(f"Service: {service}")
print(f"Status: {status}")
print(f"Assessment: {assessment}")