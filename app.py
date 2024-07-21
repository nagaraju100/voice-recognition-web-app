from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

def recognize_speech(audio_data):
    recognizer = sr.Recognizer()
    try:
        transcription = recognizer.recognize_google(audio_data)
        return transcription
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError:
        return "Sorry, there was an issue with the recognition service."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    transcription = recognize_speech(audio_data)
    return jsonify({"transcription": transcription})

if __name__ == "__main__":
    app.run(debug=True)
