# Voice Recognition Web Application

This is a web application that takes voice input from the user, uses speech recognition to transcribe it, and then responds back using text-to-speech. The application is built with Flask, JavaScript, and uses the Web Speech API for audio processing.

## Features

- Record audio from the user's microphone
- Transcribe the recorded audio to text
- Respond with the transcribed text using text-to-speech
- Clear previous transcriptions before starting a new recording

## Prerequisites

- Python 3.6+
- Flask
- SpeechRecognition library
- PyAudio library
- Web browser with Web Speech API support (e.g., Chrome)

## Getting Started

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/nagaraju100/voice-recognition-web-app.git
    cd voice-recognition-web-app
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```sh
    pip install Flask SpeechRecognition pyaudio
    ```

4. **Ensure you have `pyaudio` installed:**

    If you encounter issues, you may need to download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and then install it using:

    ```sh
    pip install path/to/downloaded/pyaudio.whl
    ```

### Running the Application

1. **Start the Flask server:**

    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to:**

    ```arduino
    http://127.0.0.1:5000/
    ```

    ![Voice Recognition Web Application](/images/application_start_page.JPG)

## Project Structure

```plaintext
voice-recognition-web-app/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── script.js
