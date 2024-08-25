from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get("data", [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else ""

        response = {
            "is_success": True,
            "user_id": "your_full_name_ddmmyyyy",  # Replace with actual values
            "email": "your_email@example.com",
            "roll_number": "your_roll_number",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)
    
    elif request.method == 'GET':
        return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
