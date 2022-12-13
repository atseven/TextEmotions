from flask import Flask, request, send_file
# from flask_ngrok import run_with_ngrok
import text2emotion as te
import nltk
nltk.download('omw-1.4')

app = Flask(__name__)
# run_with_ngrok(app) 

@app.route('/')
def run():
  text = request.args.get('text')
  text = str(text)
  result = te.get_emotion(text)
  return {"text": text, "result": result}
if __name__ == "__main__":
  app.run()