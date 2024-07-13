from flask import Flask, jsonify, request
from agent import *

app = Flask(__name__)

agent_executor = initialize_agent()

@app.route("/")
def introduction():
    user_input = "Hello, introduce yourself to someone opening this program for the first time. Be concise."

    output = agent_executor.invoke({"input": user_input})

    return jsonify(output["output"])

@app.route("/chat", methods=['POST'])
def chat():
    user_input = request.get_json()["user_input"]
    
    output = agent_executor.invoke({"input": user_input})
    
    return jsonify(output["output"])

if __name__ == "__main__":
    app.run()