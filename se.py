from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route('/')
def home():
    return "hello!!!!!!!!!!"

@app.route('/home/cube/<int:nu>')
def cube(nu):
    return {"data":nu**3}

if __name__ == "__main__":
    app.run(debug = True)
    