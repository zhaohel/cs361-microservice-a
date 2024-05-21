# cs361-microservice-a
Below are instructions for requesting and receiving data.
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
How to interpret the responses from the microservice after making HTTP requests to its endpoints.
### 1. Log Usage
When you send a POST request to the /log endpoint:
```
{
  "message": "Usage logged",
  "date": "2024-05-20"
}
```
### 2. Count Entries
When you send a GET request to the /count endpoint:
```
{
  "count": 1
}
```
This response indicates the total number of usage logs recorded.
### 3. Update Last Entry
When you send a PUT request to the /update endpoint:
```
{
  "message": "Last entry updated",
  "new_date": "2024-05-21"
}
```
## UML Sequence Diagram
<img width="678" alt="image" src="https://github.com/zhaohel/cs361-microservice-a/assets/103477958/07fba9fa-39b6-4e34-a11b-ab860f722fba">


