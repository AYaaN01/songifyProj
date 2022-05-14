
from flask import Flask, redirect, render_template, request
import requests
import json

#flask index page initialisation

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get', methods=['POST','GET'])
def chatbot_user_response():
    if request.method == 'POST':
        msg = request.form.get("usermsg")
        print(msg)
        
#run server
if __name__ == "__main__":
    app.run(debug=True)