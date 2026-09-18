from flask import Flask, request, jsonify
from src.pipeline import RAGPipeline

app = Flask(__name__)
pipeline = RAGPipeline()

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    answer = pipeline.answer_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)