import whisperx
import torch
import gc
import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    # Abre una ventana de diálogo para seleccionar el archivo
    file_path = filedialog.askopenfilename()
    return file_path

# Seleccionar archivo de audio
audio_file_path = select_file()

if not audio_file_path:
    print("No se seleccionó ningún archivo.")
    exit()

device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 16
compute_type = "float16"

# Transcripción
model = whisperx.load_model("large-v2", device, compute_type=compute_type)
audio = whisperx.load_audio(audio_file_path)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"])

# Alineación
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
print(result["segments"])

# Concatenar los segmentos transcritos
transcription_text = "\n".join([segment['text'] for segment in result["segments"]])

# Guardar la transcripción en un archivo de texto
output_file_path = 'transcription.txt'
with open(output_file_path, 'w') as file:
    file.write(transcription_text)

print(f"Transcripción guardada en {output_file_path}")

# Abre el explorador de archivos en la ubicación del archivo guardado
os.startfile(output_file_path)  # En Windows

# Para otros sistemas operativos, podrías usar:
# import subprocess
# subprocess.run(['open', output_file_path])  # En macOS
# subprocess.run(['xdg-open', output_file_path])  # En Linux
