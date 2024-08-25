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
            "user_id": "abhinavchaitanya_30012004", 
            "email": "abhinavchaitanya.r2021@vitstudent.ac.in",
            "roll_number": "21BEC1500",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)
    
    elif request.method == 'GET':
        return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
