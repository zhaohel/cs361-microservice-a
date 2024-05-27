# cs361-microservice-a
Below are instructions for requesting and receiving data.
## Prerequisites
- Python

### Installation

Clone this repository to your local machine:

```bash
git clone <your repo url>
cd <your-repository>
```
Running Microservice
```
cd <directory where your file is>
```
or
```
python3 usageSocket.py
```

## Requesting Data
### 1. Log Usage
To log a new usage date:
```
python3 test.py log <insert date yyyy-mm-dd>
```
### 2. Count Entries
To get the count of total usages:
```
python3 test.py count
```
### 3. Update Last Entry
To update the last logged date:
```
python3 test.py update <new date yyyy-mm-dd>
```
## Receiving Data
How to interpret the responses from the microservice after making HTTP requests to its endpoints.
### 1. Log Usage
When you send a POST request to the /log endpoint:
```
Response from server: {"status": "Success", "message": "Usage logged"}

```
### 2. Count Entries
When you send a GET request to the /count endpoint:
```
Response from server: {"count": 1}

```
This response indicates the total number of usage logs recorded.
### 3. Update Last Entry
When you send a PUT request to the /update endpoint:
```
Response from server: {"status": "Success", "message": "Last entry updated"}

```
## UML Sequence Diagram
<img width="678" alt="image" src="https://github.com/zhaohel/cs361-microservice-a/assets/103477958/07fba9fa-39b6-4e34-a11b-ab860f722fba">


