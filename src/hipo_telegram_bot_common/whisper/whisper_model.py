# env: deeplearning
import opencc
import whisper

converter = opencc.OpenCC("t2s.json")
model_checkpoint = r"c:\users\hipo\Downloads\small.pt"
model = whisper.load_model(model_checkpoint)
# input_video_file = r"c:\users\weiwe\Downloads\[960x540] Financial Results Highlights.mp4"
# input_audio_file = r"c:\users\weiwe\Downloads\[960x540] Financial Results Highlights.mp3"
# ffmpeg_out = subprocess.run(f'ffmpeg -i "{input_video_file}" "{input_audio_file}"',shell=True,capture_output=True)
fn = r"c:\users\hipo\downloads\zxy.m4a"
result = model.transcribe(fn)
with open(rf"{fn}.txt", mode="w", encoding="utf-8") as f:
    f.write("，".join([converter.convert(segment["text"]) for segment in result["segments"]]))
