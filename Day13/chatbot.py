from flask import Flask, request, jsonify, session
from flask_cors import CORS
from langchain_mistralai import ChatMistralAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from uuid import uuid4
import os


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY","novan")
CORS(app, supports_crendials=True)

os.environ["MISTRAL_API_KEY"] = "xHaefEmVuA516MvfCGYQSQ1GqeI2rBAH"

chat_sessions = {}

def create_chain():
    memory = ConversationBufferMemory(return_messages=True)
    llm = ChatMistralAI(model="mistral-large-latest", temperature=0.7)
    return ConversationChain(llm=llm, memory=memory)

@app.before_request
def ensure_session():
    if "user_id" not in session:
        session["user_id"] = str(uuid4())

@app.route('/api/chat', methods=['POST'])
def chat():
    user_id = session["user_id"]
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided"}), 400
    if user_id not in chat_sessions:
        chat_sessions[user_id] = create_chain()

    chain = chat_sessions[user_id]

    try:
        response = chain.run(input=message)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)