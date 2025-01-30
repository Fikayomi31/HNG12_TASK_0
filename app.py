from flask import Flask, jsonify, Response
from datetime import datetime
import json

app = Flask(__name__)

# Define the data to be returned
def get_data():
    return {
        "email": "fikayoogundijo@gmail.com",
        "datetime": datetime.utcnow().isoformat() + "Z",
        "github_repo_url": "https://github.com/Fikayoogundijo/hng-stage0-api",
    }

# Define the API endpoint
@app.route('/api', methods=['GET'])
def api():
    data = get_data()
    # Pretty-print JSON with indentation and ensure email is first
    response = json.dumps(data, indent=4, sort_keys=False)
    return Response(response, mimetype='application/json')

    return jsonify(get_data())

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)