
from flask import Flask
import sys
from housing.logger import logging
from housing.exception import housing_exception

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def home():
    try:
        raise Exception("error testing")
    except Exception as e:
        housing_exception(e,sys)
        logging.info(f"error {e} happened!!")
        logging.info(msg="Inside the home tab")
    return "CI CD Pipeline has been created"

if __name__=="__main__":
    app.run(debug=True)