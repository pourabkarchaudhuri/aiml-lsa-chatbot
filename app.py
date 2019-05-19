from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
# import chatbot

#!/usr/bin/python3
import os
import aiml
from preprocessor import spellcorrect
from CHATBOT_LSI import lsa

BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

# Endless loop which passes the input to the bot and prints
# its response
# while True:
#     input_text = input("User says > ")

   
def get_lsa_response(input_text):
    response = k.respond(input_text)

    if response=='grammar_fallback' :
        print("Grammar Engine fallback")
        spellcorrected_text = spellcorrect(input_text)
        lsa_response = lsa(spellcorrected_text)
        # print("Bot says > ", lsa_response)
        return lsa_response

        # file_path = "/path/to/yourfile.txt"
        file_path = os.getcwd() + '/fallback_sentences.txt'
        with open(file_path, 'a') as file:
            file.write(input_text + "\n")

    else :
        return response
        # print("Bot says > ", response)

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({
        "status":"active",
        "state":"running",
        "errors":None
    })

#Example for Root Route
@app.route('/query', methods=['POST'])
def lsa():
    # print(request.get_json())
    if not request.json:
        return jsonify({
            "status": 400,
            "message": "Bar request. Request has no body"
        })
    else:
        print(request.get_json())
        response = get_lsa_response(request.get_json()['query'])
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

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)