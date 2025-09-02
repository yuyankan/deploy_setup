from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import os

app = FastAPI()

# 定义图片服务器的根路径
# **请确保运行此脚本的服务器有权限访问这个网络共享路径**
#IMAGE_SERVER_PATH = Path("//147.121.160.30/data")
# change to docker address
IMAGE_SERVER_PATH = Path("/data_mount")

@app.get("/images/{image_path:path}")
async def get_image(image_path: str):
    # 将客户端请求的 URL 路径与图片服务器根路径拼接
    full_path = IMAGE_SERVER_PATH / image_path

    # 检查文件是否存在
    if not full_path.exists() or not full_path.is_file():
        raise HTTPException(status_code=404, detail="Image not found")

    # 返回图片文件
    return FileResponse(full_path, media_type="image/bmp")
~                                                           
