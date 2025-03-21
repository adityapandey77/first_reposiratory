from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Aditya Sagar Pandey" 
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    
   
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    time_str = ist_time.strftime("%d %B %Y, %I:%M %p IST")


    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time in IST:</b> {time_str}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
