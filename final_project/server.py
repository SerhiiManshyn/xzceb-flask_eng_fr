from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def englishToFrench():
    #textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = request.args.get('text_to_translate')
    return french_text  #"Translated text to French"

@app.route("/french_to_english")
def frenchToEnglish():
    #textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = request.args.get('text_to_translate')
    return english_text #"Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return  render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
