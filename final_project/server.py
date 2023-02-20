from machinetranslation import englishToFrench, frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench_route():
    english_text = request.args.get('textToTranslate')
    # Write your code here
    french_text = englishToFrench(english_text)['translations'][0]['translation']
    return french_text 

@app.route("/frenchToEnglish")
def frenchToEnglish_route():
    french_text = request.args.get('textToTranslate')
    # Write your code here
    english_text = frenchToEnglish(french_text)['translations'][0]['translation']
    return english_text 

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return  render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
