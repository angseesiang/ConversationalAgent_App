from flask import Flask, request, jsonify, render_template
from model.conversational_model import ConversationalModel
from utils.data_preprocessor import DataPreprocessor
from utils.evaluator import Evaluator

# Initialize the Flask application
app = Flask(__name__)
model = ConversationalModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = model.generate_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
