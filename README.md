# Robust Video Matting
## ![gif](https://user-images.githubusercontent.com/107867709/178918313-e523be3f-a281-413d-8f23-09f7e7378e6f.gif)
## Description
####
We are going to build a robust, real-time, high-resolution human video matting tool that achieves new state-of-the-art performance. This tool can process 4K at 76 FPS and HD at 104 FPS on an Nvidia GTX 1080Ti GPU.
####
## Instruction
### Run the service with FastAPI
####
1. Mount to the project location
2. Install libraries
```
pip install -r requirements.txt
```
3. Start FastAPI
```
uvicorn app:app --reload
```
- Check the Swagger: http://127.0.0.1:8000/docs
- Here, you can upload the video from your computer and wait for it to process. Then, you can download the converted video to your computer 
####
