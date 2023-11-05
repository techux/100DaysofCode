from flask import Flask, request

app = Flask(__name__) 

# Test the method - GET and POST
@app.route("/", methods=["GET","POST"])
def homepage():
    return f"Hello World! Method is {request.method} "

# Understand the Query passing in url
@app.route("/helo/<name>")
def greet(name="World"):
    return f"Hello {name}"

# Learn about parameters passing from URL
@app.route("/get", methods=["GET"])
def display():
    return f"Parameters are : {dict(request.args)}"

if __name__ == "__main__":
    app.run()