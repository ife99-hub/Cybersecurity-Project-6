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
ports = [{"port": 22, "service": "SSH", "status": "Open"},
         {"port": 80, "service": "HTTP", "status": "Open"},
         {"port": 443, "service": "HTTPS", "status": "Open"},
         {"port": 23, "service": "Telnet", "status": "Open"},
         {"port": 25, "service": "SMTP", "status": "Closed"}]
for port_info in ports:
    port = port_info["port"]
    service = port_info["service"]
    status = port_info["status"]


    risk, assessment = describe_port(port, service, status)
    print("\nPort:", port)
    print("Service:", service)
    print("Status:", status)
    print("Risk:", risk)
    print("Assessment:", assessment)
