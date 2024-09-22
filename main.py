from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

# Utility functions
def extract_numbers(data):
    return [x for x in data if x.isdigit()]

def extract_alphabets(data):
    return [x for x in data if x.isalpha()]

def highest_lowercase(data):
    return [max([x for x in data if x.islower()], default="")]

def validate_file(file_b64):
    try:
        file_data = base64.b64decode(file_b64)
        # For demo, we're just writing it to a temp file
        temp_file = 'temp_file'
        with open(temp_file, 'wb') as f:
            f.write(file_data)

        file_size = os.path.getsize(temp_file) / 1024  # Size in KB
        mime_type = "application/octet-stream"  # Default mime type

        # Clean up temp file after processing
        os.remove(temp_file)

        return True, mime_type, file_size
    except Exception as e:
        return False, "", 0

# POST method for /bfhl route
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    file_b64 = request.json.get('file_b64', "")

    # Extract numbers and alphabets
    numbers = extract_numbers(data)
    alphabets = extract_alphabets(data)
    highest_lower = highest_lowercase(alphabets)

    # Validate file if provided
    file_valid, file_mime_type, file_size_kb = validate_file(file_b64) if file_b64 else (False, "", 0)

    response = {
        "is_success": True,
        "user_id": "your_name_01012000",  # Use your format here
        "email": "your_email@example.com",
        "roll_number": "ABCD1234",  # Replace with actual roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lower,
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return jsonify(response)

# GET method for /bfhl route
@app.route('/bfhl', methods=['GET'])
def operation_code():
    return jsonify({"operation_code": 1})

if __name__ == "__main__":
    app.run(debug=True)
