
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def home():
    return "CI CD Pipeline has been created"

if __name__=="__main__":
    app.run(debug=True)