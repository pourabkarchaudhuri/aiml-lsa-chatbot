from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import chatbot

app = Flask(__name__)

#Example for Root Route
@app.route('/getresult', methods=['POST'])
def post_example():
    print(request.get_json())
    if not request.json:
        return jsonify({
            "status": 400,
            "message": "request has no body"
        })
    else:
        print(request.get_json())
        response = chatbot.get_lsa_response(request.get_json()['query'])
        return jsonify({
            "status": 200,
            "response": response
        })
        # print(request.data.query)
        # chatbot.run()

if __name__ == "__main__":
    app.run(debug=True, port=5000)