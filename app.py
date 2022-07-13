import sys
sys.path.append(r"C:\Users\nhan.pham\Desktop\Projects\Robust_video_matting\pytorch_inference")
import os
import shutil
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import torch
from pytorch_inference.model import MattingNetwork
from pytorch_inference.inference import convert_video

# Load the model
model = MattingNetwork('mobilenetv3')
model.load_state_dict(torch.load(os.getcwd() + r'\pytorch_inference\rvm_mobilenetv3.pth'))
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
            output_composition='com.mp4',
            output_alpha='pha.mp4',
            output_foreground='fgr.mp4',
            output_video_mbps=4,
            downsample_ratio=None,
            seq_chunk=12,
        )
    return {"file_name": file.filename}

#Download the converted video
@app.get("/")
async def download_file():
    file_path = "com.mp4"
    return FileResponse(path = file_path, filename = file_path)