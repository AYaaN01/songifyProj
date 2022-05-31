from flask import Flask, render_template, request
import chatbot_backend as cb

# flask app initialisation
app = Flask(__name__)

# <html> index page initialisation 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def chatbot_response():
    msg = request.args.get('usermsg', type=str)
    print(msg)
    #response_msg = cb.getResponse(msg)      
    return msg
    
#run server
if __name__ == "__main__":
    app.run(debug=True)