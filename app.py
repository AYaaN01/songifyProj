from flask import Flask, render_template, request
import chatbot_backend as cb

#flask index page initialisation
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get",  methods=['GET','POST'])
def chatbot_response():
    if request.method == 'GET':
        msg = request.args.get('usermsg')
        response_msg = cb.getResponse(msg)      
        return response_msg
    elif request.method == 'POST':
        return render_template("index.html")

#run server
if __name__ == "__main__":
    app.run(debug=True)