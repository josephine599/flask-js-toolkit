# Flask-JS Toolkit

A beginner's toolkit for building web applications with Flask (Python backend) and JavaScript (frontend).

## Overview

This toolkit demonstrates a simple full-stack web application where a Flask server serves both the frontend and provides an API that fetches random jokes.

## Setup Instructions

1. Ensure you have Python 3 installed.

2. Navigate to the backend directory:
   ```
   cd backend
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the Flask app:
   ```
   python app.py
   ```

6. Open your browser and go to `http://127.0.0.1:5001` to see the live application.

## Usage

- The Flask server serves the frontend at the root URL.
- Click the "Get a Joke" button to fetch a random joke from the API.

## Minimal Working Example

The example consists of:
- A Flask app that serves the HTML, CSS, JS files and provides an API.
- An HTML page with a button.
- JavaScript to fetch data from the API.
- Basic CSS for styling.

Expected output: Clicking the button displays a random dad joke.
## Live Code Repository
https://github.com/josephine599/flask-js-toolkit