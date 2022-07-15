# Robust Video Matting
## ![gif](https://user-images.githubusercontent.com/107867709/178918313-e523be3f-a281-413d-8f23-09f7e7378e6f.gif)
## Description
####
We are going to build a robust, real-time, high-resolution human video matting tool that achieves new state-of-the-art performance. This tool can process 4K at 76 FPS and HD at 104 FPS on an Nvidia GTX 1080Ti GPU. The method we use in this tool does not require any auxiliary inputs such as a trimap or a pre-captured background image, so it can be widely applied to existing human matting applications.
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
- Here, you can upload the video from your computer and wait for it to be processed. Then, you can download the converted video to your computer 
####
## Reference
####
If you want to know more about the structure of the model, how to train, inference and how to export the model between frameworks (they are similar to pytorch) more detail, try the links below:
- https://github.com/PeterL1n/RobustVideoMatting
- https://arxiv.org/abs/2108.11515
####
