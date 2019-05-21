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
while True:
    input_text = input("User says > ")

   
   
    response = k.respond(input_text)

    if (response=='grammar_fallback' or "grammar_fallback" in response) :
        print("Grammar Engine Incapable > Switch to LSA")
        spellcorrected_text = spellcorrect(input_text)
        print(spellcorrected_text)
        lsa_response = lsa(spellcorrected_text)
        print("Bot says > ", lsa_response)

        # file_path = "/path/to/yourfile.txt"
        file_path = os.getcwd() + '/fallback_sentences.txt'
        with open(file_path, 'a') as file:
            file.write(input_text + "\n")

    else :
        print("Bot says > ", response)