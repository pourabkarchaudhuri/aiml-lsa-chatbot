# TechGig Code Gladiators 2019
### AIML and LSA powered chatbot : 

This is an a chatbot project powered by powerful open source frameworks and algorithms to stay independent from existing and expensive third-party platforms
## Features

  ##### The following functionalities are to be considered in this project

  * AIML - Artificial Intelligence Markup Language for Basic conversations
  * Spellcorrect - To do minimal spell rectification before text modelling
  * LSA - Latent Semantic Analysis - To answer FAQs
  * Sentimental Analysis - To understand positivity or negativity of conversations


### Technology

This python server uses uses open source packages to work. The following packages were used:

## Prerequisites

* [Python] - awesome language we love

## Installation

##### For Running in Console (Local)

The Chatbot requires [Python](https://www.python.org/) 3.6.1 to run.
```sh
$ git clone https://github.com/pourabkarchaudhuri/aiml-lsa-chatbot.git
$ cd aiml-lsa-chatbot
$ pip install -r requirements.txt
$ python get_corpora.py
```

##### For Running as a web server (Local)

```sh
$ python app.py
```
The default PORT is set to `5000`

Send a `POST` method HTTP call with some API client like `Postman` to `http://localhost:5000/query`

Set `Content-Type` as `application/json` in HEADERS
Put text in following payload to the body of thre request.

{
    "query": "YOUR SENTENCE"
}

### AIML utilizes a preprocessing step called Normalization.

This AIML set is designed to work with a AIML preprocessor

    The preprocessor

    Corrects some spelling errors and colloquialisms (e.g. "wanna" --> "want to")
    Substitutes words for common emoticons (e.g. ":-)" --> "SMILE")
    Expands contractions (e.g. "isn't" --> "is not")
    Removes intra-sentence punctuation (e.g. "Dr. Wallace lives on St. John St. --> "Dr Wallace lives on St John St.")

We refer to the above substitution steps as Normalization.

The last preprocessing step

    Splits sentences based on predefined punctuation characters ".", "!", ";" and "?"

All of these preprocessing steps are defined in the configuration file. In addition the configuration file

    Defines substitutions for <gender>, <person> and <person2>

The preprocessor normalizes the inputs to the bot by running through a series of substitutions, then splits the input into sentences and feeds these one at a time to the bot.

### LSA takeover on AIML Fallback

When AIML fails it switches to LSA. 
Latent semantic analysis (LSA) is a technique in natural language processing, in particular distributional semantics, of analyzing relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms. LSA assumes that words that are close in meaning will occur in similar pieces of text (the distributional hypothesis). A matrix containing word counts per paragraph (rows represent unique words and columns represent each paragraph) is constructed from a large piece of text and a mathematical technique called singular value decomposition (SVD) is used to reduce the number of rows while preserving the similarity structure among columns. Paragraphs are then compared by taking the cosine of the angle between the two vectors (or the dot product between the normalizations of the two vectors) formed by any two columns. Values close to 1 represent very similar paragraphs while values close to 0 represent very dissimilar paragraphs.


### Hope we disrupted. Thanks TechGig!

   [Python]: <https://www.python.org/>
