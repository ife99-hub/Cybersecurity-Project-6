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
port = 22
service = "SSH"
status = "open"


assessment = describe_port(port, service, status)

print(f"port: {port}")
print(f"service: {service}")
print(f"status: {status}")
print(f"Assessment: {assessment}")

