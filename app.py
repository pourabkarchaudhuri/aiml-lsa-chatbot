import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import chatbot


app = Flask(__name__)

#Example for Root Route
@app.route('/query', methods=['POST'])
def post_example():
    print(request.get_json())
    if not request.json:
        return jsonify({
            "status": 400,
            "message": "Bar request. Request has no body"
        })
    else:
        print(request.get_json())
        response = chatbot.get_lsa_response(request.get_json()['query'])
        return jsonify({
            "result" : {
                "fulfillment":{
                    "messages": [{
                        "type": 0,
                        "platform": "facebook",
                        "speech": response
                        }
                    ]
                }        
            }
        })
        # return jsonify({
        #     "status": 200,
        #     "response": response
        # })
        # print(request.data.query)
        # chatbot.run()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)