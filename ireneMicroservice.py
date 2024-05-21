from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
filename = 'usage_log.txt'

def read_log():
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def write_log(data):
    with open(filename, 'a') as file:
        file.write(data + "\n")

@app.route('/log', methods=['POST'])
def log_usage():
    data = request.get_json()
    try:
        date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
        write_log(str(date))
        return jsonify({'message': 'Usage logged', 'date': str(date)}), 200
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD'}), 400

@app.route('/count', methods=['GET'])
def count_usage():
    entries = read_log()
    return jsonify({'count': len(entries)}), 200

@app.route('/update', methods=['PUT'])
def update_last_entry():
    entries = read_log()
    data = request.get_json()
    if entries:
        try:
            new_date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
            entries[-1] = str(new_date)
            with open(filename, 'w') as file:
                file.writelines(line + '\n' for line in entries)
            return jsonify({'message': 'Last entry updated', 'new_date': str(new_date)}), 200
        except ValueError:
            return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD'}), 400
    else:
        return jsonify({'error': 'No entries to update'}), 404

if __name__ == '__main__':
    app.run(debug=True)
