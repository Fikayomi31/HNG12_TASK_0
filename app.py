from flask import Flask, jsonify, Response
from datetime import datetime
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the data to be returned
def get_data():
    return {
        "email": "fikayoogundijo@gmail.com",
        "datetime": datetime.utcnow().isoformat(),
        "github_repo_url": "https://github.com/Fikayomi31/HNG12_TASK_0",
    }

# Define the API endpoint
@app.route('/api', methods=['GET'])
def api():
    data = get_data()
    # Print JSON with indentation and ensure email is first
    response = json.dumps(data, indent=4, sort_keys=False)
    return Response(response, mimetype='application/json')


# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)