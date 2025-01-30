# HNG Stage 0 API

This is a public API developed as part of the HNG Stage 0 task. It returns basic information, including:
- Your registered GitHub email.
- The current datetime in ISO 8601 format.
- The GitHub URL of the project's codebase.

The API is built using **Python** and **Flask**, and it handles Cross-Origin Resource Sharing (CORS) appropriately.

---

## Features
- **CORS Handling**: The API supports cross-origin requests.
- **Dynamic Datetime**: The `datetime` field is generated dynamically in ISO 8601 format (UTC).
- **Pretty-Printed JSON**: The API response is formatted with each key-value pair on a separate line for readability.

---

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites
- Python 3.x
- Git

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hng-stage0-api.git
   cd hng-stage0-api

2. ** Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install dependencies:

    ```bash
    pip install -r requirements.txt

4. ** Run the server:
    ```bash
    python app.py


5. ** Access the API:
    Open your browser or use a tool like Postman to access:

    ```bash
    http://localhost:5000/api
