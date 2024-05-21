# cs361-microservice-a

## Prerequisites
- Python 
- Flask

Install Flask:
```
pip install flask
```
or 
```
pip3 install flask
```
Running Microservice
```
python ireneMicroservice.py
```
or
```
python3 ireneMicroservice.py
```
The service will start on http://localhost:5000.

## Requesting Data
### 1. Log Usage
To log a new usage date:

Endpoint: `POST /log`
```
{
  "date": "YYYY-MM-DD"
}
```
Example Call:
```
import requests
response = requests.post('http://localhost:5000/log', json={"date": "2024-05-20"})
print(response.json())
```
### 2. Count Entries
To get the count of total usages:

Endpoint: `GET /count`
Example Call:
```
import requests
response = requests.get('http://localhost:5000/count')
print(response.json())
```
### 3. Update Last Entry
To update the last logged date:

Endpoint: `PUT /update`
```
{
  "date": "YYYY-MM-DD"
}
```
Example Call:
```
import requests
response = requests.put('http://localhost:5000/update', json={"date": "2024-05-21"})
print(response.json())
```
## Receiving Data

## UML Sequence Diagram


