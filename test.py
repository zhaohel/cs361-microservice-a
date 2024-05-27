import socket
import json
import sys

def send_request(data):
    """Sends a request to the server and prints the response."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5500))
        s.sendall(json.dumps(data).encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        return response

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test.py <command> <date>")
        sys.exit(1)

    command = sys.argv[1]
    date = sys.argv[2] if len(sys.argv) > 2 else None
    data = {"command": command}
    if date:
        data["date"] = date

    response = send_request(data)
    print("Response from server:", response)
