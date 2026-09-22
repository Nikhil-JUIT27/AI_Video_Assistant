from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source = "https://youtu.be/lHBiso1Nw2E"

chunks=process_input(source)
print(transcribe_all(chunks))