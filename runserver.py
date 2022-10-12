import uvicorn


# ● main：main.py 文件（一个 Python「模块」）。
# ● app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
# ● host：启动服务的ip，0.0.0.0代表任何都可以访问
# ● port：服务的端口
# ● reload：让服务器在更新代码后重新启动。仅在开发时使用该选

if __name__ == '__main__':
    uvicorn.run(app='main:fun', host="0.0.0.0", port=8100, reload=True)