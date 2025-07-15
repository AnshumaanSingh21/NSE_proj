from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import tempfile
import os

app = FastAPI()
model = whisper.load_model("base")

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <head><title>Mic Whisper</title></head>
        <body>
            <h2>Run Whisper Mic Transcription</h2>
            <form action="/run" method="post">
                <button type="submit">Start Recording & Transcribe</button>
            </form>
        </body>
    </html>
    """

@app.post("/run")
async def run_transcription():
    fs = 16000  # Sampling rate
    seconds = 5  # Duration of recording

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        tmp_filename = tmpfile.name

    print("Recording...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write(tmp_filename, fs, recording)
    print("Recording complete.")

    result = model.transcribe(tmp_filename)
    os.remove(tmp_filename)

    return {"transcription": result["text"]}
