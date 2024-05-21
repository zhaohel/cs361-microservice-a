import requests

BASE_URL = 'http://localhost:5000'

def test_log_usage(date):
    response = requests.post(f'{BASE_URL}/log', json={'date': date})
    print('Log Response:', response.json())

def test_count_usage():
    response = requests.get(f'{BASE_URL}/count')
    print('Count Response:', response.json())

def test_update_last_entry(date):
    response = requests.put(f'{BASE_URL}/update', json={'date': date})
    print('Update Response:', response.json())

if __name__ == '__main__':
    print("Testing log usage:")
    test_log_usage('2024-05-20')
    print("\nTesting count usage:")
    test_count_usage()
    print("\nTesting update last entry:")
    test_update_last_entry('2024-05-21')
    print("\nTesting count usage post update:")
    test_count_usage()
