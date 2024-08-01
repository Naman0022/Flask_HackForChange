from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger():
    # Extract data from the request
    data = request.json
    user_id = data.get('user_id')
    content_type = data.get('content_type')  # 'image' or 'chat'
    content = data.get('content')  # URL or chat text

    # Log the received data (optional)
    print(f"Received data: User ID: {user_id}, Type: {content_type}, Content: {content}")

    try:
        # Run your Python script with the extracted data
        # Here we pass the data as environment variables or arguments
        # Adjust the command based on how your script needs to receive data
        result = subprocess.run([
            'python3', 'model.py',
            f'--user_id={user_id}',
            f'--content_type={content_type}',
            f'--content={content}'
        ], capture_output=True, text=True)

        output = result.stdout
        return jsonify({"status": "success", "output": output}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
