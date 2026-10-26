# EchoType — Whisper ASR

A simple web-based Automatic Speech Recognition (ASR) tool that converts uploaded audio into editable text using OpenAI Whisper.

## Run locally

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

> Whisper also requires FFmpeg. Install FFmpeg and ensure `ffmpeg` is available on PATH.
