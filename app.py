import sys
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import torch

sys.path.append(os.getcwd() + r"\pytorch_inference")

# Load the model
from pytorch_inference.model import MattingNetwork
from pytorch_inference.inference import convert_video
model = MattingNetwork('mobilenetv3')
model.load_state_dict(torch.load(r'pytorch_inference\rvm_mobilenetv3.pth'))
app=FastAPI()

#Convert the video
@app.post("/")
async def create_file(file: UploadFile = File(...)):
    with open("video.mp4", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        convert_video(
            model,
            input_source="video.mp4",
            output_type='video',
            output_composition=r'converted_video\com.mp4',
            output_alpha=r'converted_video\pha.mp4',
            output_foreground=r'converted_video\fgr.mp4',
            output_video_mbps=4,
            downsample_ratio=None,
            seq_chunk=12,
        )
    return {"file_name": file.filename}

#Download the converted video
@app.get("/")
async def download_file():
    file_path = r"converted_video\com.mp4"
    return FileResponse(path = file_path, filename = file_path)