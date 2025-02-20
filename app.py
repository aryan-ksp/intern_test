from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    try:
        result = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return "<h1>Flask App is Running!</h1><p>Go to <a href='/htop'>/htop</a> to see the required output.</p>"

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content response for favicon

@app.route('/htop')
def htop():
    name = "Aryan Kashyap"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = get_top_output()

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
