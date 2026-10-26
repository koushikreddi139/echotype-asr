from flask import Flask, render_template, request, jsonify, send_file
import os, tempfile

app = Flask(__name__)
UPLOAD_DIR = os.path.join(tempfile.gettempdir(), 'whisper_asr_uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

try:
    import whisper
    MODEL = whisper.load_model('base')
except Exception:
    MODEL = None

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/transcribe')
def transcribe():
    if MODEL is None:
        return jsonify(error='Whisper is not installed or the model could not be loaded. Run: pip install openai-whisper'), 500
    audio = request.files.get('audio')
    if not audio or not audio.filename:
        return jsonify(error='Please select an audio file.'), 400
    ext = os.path.splitext(audio.filename)[1].lower() or '.wav'
    path = os.path.join(UPLOAD_DIR, 'audio' + ext)
    audio.save(path)
    try:
        result = MODEL.transcribe(path, fp16=False)
        return jsonify(text=result.get('text', '').strip(), language=result.get('language', 'unknown'))
    except Exception as e:
        return jsonify(error=f'Transcription failed: {e}'), 500
    finally:
        try: os.remove(path)
        except OSError: pass

if __name__ == '__main__':
    app.run(debug=True)
