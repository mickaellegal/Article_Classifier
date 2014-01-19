from flask import Flask, request, render_template, jsonify
from yhat import Yhat
import os


app = Flask(__name__)
yh = Yhat(os.environ.get("YHAT_USERNAME"), os.environ.get("YHAT_APIKEY"))


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method=="GET":
            return render_template("home.html")
    else:
            
        data = request.form.get('entry')
    
        data = {
             "content": [data]
             }    

    results = yh.predict("NYTimesClassifier", 1, data)
    
    return jsonify({"results": results})
    

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)))    