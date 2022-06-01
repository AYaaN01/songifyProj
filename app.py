from flask import Flask, render_template, request
from chatbot_backend import getResponse
import emotion_resp as er
import spotify_api as sa

app = Flask(__name__)

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(getResponse(userText))

@app.route("/get/track")
#function to get the track ID
def trackSong():
    userText = request.args.get('msg')
    tone=er.getEmotion(userText)
    get_track = sa.send_trackURI(tone)
    return get_track
    
if __name__ == "__main__":
    app.run(debug=True)