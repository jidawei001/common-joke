from flask import Flask,render_template,request
import google.generativeai as palm
import os

api = os.getenv("MAKERSUITE_API_TOKEN")
model = {"model":"models/chat-bison-001"}
palm.configure(api_key=api)

app = Flask(__name__)
user_name = ""
flag = 1

@app.route("/",methods=["GET","POST"])
def index():
    global flag
    flag = 1
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global flag,user_name
    if flag==1:
        user_name = request.form.get("q")
        flag = 0
    return(render_template("main.html",r=user_name))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/DBS",methods=["GET","POST"])
def DBS():
    return(render_template("DBS.html"))

@app.route("/DBS_prediction",methods=["GET","POST"])
def DBS_prediction():
    q = float(request.form.get("q"))
    return(render_template("DBS_prediction.html",r=90.2 + (-50.6*q)))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    return(render_template("makersuite.html"))

@app.route("/makersuite_1",methods=["GET","POST"])
def makersuite_1():
    q = "Can you help me prepare my tax return?"
    r = palm.chat(**model, messages=q)
    return(render_template("makersuite_1_reply.html",r=r.last))

@app.route("/makersuite_gen",methods=["GET","POST"])
def makersuite_gen():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("makersuite_gen_reply.html",r=r.last))

if __name__ == "__main__":
    app.run()
