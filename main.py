from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "When will this eye emoji end and you will use your words?"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)  # Replace 8080 with your desired port
