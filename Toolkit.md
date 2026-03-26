# Prompt-Powered Kickstart: Building a Beginner’s Toolkit for Flask with JavaScript

## 1. Title & Objective

**Title:** Getting Started with Flask and JavaScript – A Beginner’s Toolkit

**Technology Chosen:** Flask (a lightweight Python web framework) combined with vanilla JavaScript for the frontend.

**Why I Chose This Technology:** Flask is simple and powerful for building web APIs and small applications. Combining it with JavaScript allows for full-stack development without heavy frameworks, making it ideal for beginners to understand client-server interactions.

**End Goal:** Create a simple web application where the frontend fetches and displays a random joke from a Flask backend API.

## 2. Quick Summary of the Technology

**What is Flask?** Flask is a micro web framework written in Python. It's designed to be lightweight and easy to use, allowing developers to build web applications quickly.

**Where is it Used?** Flask is commonly used for building RESTful APIs, web services, and small to medium-sized web applications. It's popular in data science projects, prototyping, and backend services.

**One Real-World Example:** Many machine learning models are deployed as web APIs using Flask, where the frontend (built with JS) sends data to the Flask server for prediction.

**JavaScript Role:** Vanilla JavaScript handles the frontend interactions, making asynchronous requests to the Flask API using the Fetch API.

## 3. System Requirements

- **OS:** Linux, macOS, or Windows
- **Tools/Editors:** Python 3.x, VS Code or any text editor, a web browser
- **Packages:** pip (Python package installer)

## 4. Installation & Setup Instructions

### Step 1: Install Python
Ensure Python 3 is installed. Download from [python.org](https://www.python.org/downloads/) if needed.

### Step 2: Clone or Download the Repository
Download the codebase from the provided GitHub repo or ZIP file.

### Step 3: Set Up the Backend
1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac; use `venv\Scripts\activate` on Windows
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

### Step 4: Run the Application
1. Start the Flask server:
   ```
   python app.py
   ```
   You should see output like: `* Running on http://127.0.0.1:5001/`

2. Open your browser and navigate to `http://127.0.0.1:5001` to view the live application.

## 5. Minimal Working Example

**Description:** This example demonstrates a basic full-stack app. The Flask backend fetches a random joke from an external API and returns it as JSON. The JavaScript frontend fetches this joke and displays it on the page when the button is clicked.

**Code Overview:**

- **Backend (app.py):**
  ```python
  from flask import Flask, jsonify, send_from_directory
  from flask_cors import CORS
  import requests

  app = Flask(__name__)
  CORS(app)

  @app.route('/')
  def index():
      return send_from_directory('../frontend', 'index.html')

  @app.route('/<path:path>')
  def static_files(path):
      return send_from_directory('../frontend', path)

  @app.route('/api/message')
  def message():
      try:
          response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
          joke = response.json()['joke']
          return jsonify({"message": joke})
      except:
          return jsonify({"message": "Why don't scientists trust atoms? Because they make up everything!"})

  if __name__ == '__main__':
      app.run(debug=True)
  ```

- **Frontend (index.html):**
  ```html
  <!DOCTYPE html>
  <html>
  <head>
    <title>Flask + JS Toolkit</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Joke Generator</h1>
    <button onclick="getMessage()">Get a Joke</button>
    <p id="output"></p>
    <script src="script.js"></script>
  </body>
  </html>
  ```

- **JavaScript (script.js):**
  ```javascript
  function getMessage() {
    fetch("/api/message")
      .then(response => response.json())
      .then(data => {
        document.getElementById("output").innerText = data.message;
      })
      .catch(error => console.error("Error:", error));
  }
  ```

- **CSS (style.css):**
  ```css
  body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 50px;
  }

  button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }

  #output {
    margin-top: 20px;
    font-size: 18px;
    color: blue;
  }
  ```

**Expected Output:** When you click the "Get a Joke" button, a random dad joke appears below the button (e.g., "Why don't scientists trust atoms? Because they make up everything!").

## 6. AI Prompt Journal

**Prompt 1:** "Give me a step-by-step guide to set up a basic Flask application with CORS enabled for API calls."

**Link to Curriculum:** (Assuming from ai.moringaschool.com Flask module)

**AI’s Response Summary:** The AI provided a complete setup including installing Flask and flask-cors, creating the app structure, and enabling CORS.

**My Evaluation:** Very helpful; it saved time on boilerplate code and explained CORS importance for frontend-backend communication.

**Prompt 2:** "How to create a simple JavaScript function to fetch data from a Flask API and display it on an HTML page?"

**Link to Curriculum:** JavaScript Fetch API section.

**AI’s Response Summary:** Explained using fetch() with promises, handling JSON response, and updating DOM.

**My Evaluation:** Clear and concise; helped me understand asynchronous operations.

**Prompt 3:** "Basic CSS styling for a centered button and text display."

**Link to Curriculum:** CSS basics.

**AI’s Response Summary:** Provided simple CSS rules for body, button, and output elements.

**My Evaluation:** Straightforward; improved the UI without complexity.

**Prompt 4:** "How to integrate a public API like icanhazdadjoke.com into a Flask app to fetch random jokes?"

**Link to Curriculum:** API integration in Python.

**AI’s Response Summary:** Explained using requests library to make GET requests with headers, handle JSON responses, and error handling.

**My Evaluation:** Helped add a fun, dynamic feature; demonstrated real API usage.

## 7. Common Issues & Fixes

- **Issue:** CORS error when fetching from frontend.
  **Fix:** Install and use flask-cors. Add `CORS(app)` after creating the Flask app. Reference: [Flask-CORS docs](https://flask-cors.readthedocs.io/)

- **Issue:** ModuleNotFoundError for flask_cors.
  **Fix:** Ensure `pip install flask-cors` is run. If using virtual env, activate it first.

- **Issue:** API not responding.
  **Fix:** Check if Flask server is running on port 5000. Ensure the URL in fetch matches the server address.

- **Issue:** Button click does nothing.
  **Fix:** Check browser console for errors. Ensure script.js is loaded and functions are defined.

## 8. References

- **Official Flask Docs:** [flask.palletsprojects.com](https://flask.palletsprojects.com/)
- **Flask-CORS:** [pypi.org/project/Flask-Cors/](https://pypi.org/project/Flask-Cors/)
- **JavaScript Fetch API:** [developer.mozilla.org/en-US/docs/Web/API/Fetch_API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- **icanhazdadjoke API:** [icanhazdadjoke.com/api](https://icanhazdadjoke.com/api)
- **Tutorial:** [Flask Quickstart](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- **Video:** [Building a Simple Flask App](https://www.youtube.com/watch?v=Z1RJmh_OqeA) (example link)

**Themed Hello World - Joke API Integration:** Enhanced the basic message app into a joke generator that fetches random dad jokes from the icanhazdadjoke.com API. This demonstrates integrating external APIs, error handling, and making the app more engaging for users.

- **Official Flask Docs:** [flask.palletsprojects.com](https://flask.palletsprojects.com/)
- **Flask-CORS:** [pypi.org/project/Flask-Cors/](https://pypi.org/project/Flask-Cors/)
- **JavaScript Fetch API:** [developer.mozilla.org/en-US/docs/Web/API/Fetch_API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- **Tutorial:** [Flask Quickstart](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- **Video:** [Building a Simple Flask App](https://www.youtube.com/watch?v=Z1RJmh_OqeA) (example link)