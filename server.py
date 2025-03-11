from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("11 mar.html")
@app.route("/submit", methods=["post"])
def submit(): 
    name=request.form.get("name")
    email=request.form.get("email")
    return f"Received: Name={name} and Email={email}"
if __name__=="__main__":
    app.run(debug=True)
     