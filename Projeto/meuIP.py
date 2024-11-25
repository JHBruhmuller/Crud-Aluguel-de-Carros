import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(("8.8.8.8", 80))
    ipLocal = s.getsockname()[0]

print(f"Seu IP local é: {ipLocal}")