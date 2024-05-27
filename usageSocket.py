import socket
import json
import os

def log_usage(date):
    """Logs the provided date to a text file if not already logged."""
    try:
        with open("usage_log.txt", "r+") as file:
            existing_dates = file.read().splitlines()
            if date in existing_dates:
                return {"status": "Error", "message": "Date already logged"}
            else:
                file.write(f"{date}\n")
                return {"status": "Success", "message": "Usage logged"}
    except FileNotFoundError:
        with open("usage_log.txt", "w") as file:
            file.write(f"{date}\n")
        return {"status": "Success", "message": "Usage logged"}

def count_usage():
    """Counts the number of unique log entries."""
    try:
        with open("usage_log.txt", "r") as file:
            return {"count": len(set(file.read().splitlines()))}
    except FileNotFoundError:
        return {"count": 0}

def start_server():
    host = 'localhost'
    port = 5500
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on port {port}")

    try:
        while True:
            client, addr = server.accept()
            with client:
                print(f"Connected by {addr}")
                data = client.recv(1024).decode()
                request = json.loads(data)
                if request['command'] == 'log':
                    response = log_usage(request['date'])
                elif request['command'] == 'count':
                    response = count_usage()
                else:
                    response = {"status": "Error", "message": "Invalid command"}
                client.sendall(json.dumps(response).encode())
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
