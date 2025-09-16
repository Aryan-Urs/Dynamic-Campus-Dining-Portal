from flask import Flask,jsonify
from db_config import get_db_connection

app=Flask(__name__)

@app.route("/test_db")
def test_db():
    conn=get_db_connection()
    if conn:
        return jsonify({"message":"Successully connected to the Database"})
    else:
        return jsonify({"message":"Could not Connect to the Database"}),500
@app.route("/")
def home():
    return "Hello to the Backend"
if __name__=="__main__":
    app.run(debug=True)


          