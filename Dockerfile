# 使用官方的 Python 3.10 镜像作为基础镜像
FROM python:3.10-slim-buster

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到容器的 /app 目录中
COPY . /app

# 安装必要的包
RUN pip install --no-cache-dir -U sentence-transformers flask

# 暴露端口 5000 供应用程序使用
EXPOSE 5000

# 定义环境变量
ENV NAME World

# 在容器启动时运行 app.py
CMD ["python", "app.py"]
