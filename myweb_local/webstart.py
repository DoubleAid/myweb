from app import create_app

app = create_app()

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # 服务器使用
    # app.run(host='0.0.0.0', debug=True)
    # 本地测试使用
    app.run(port=8000)
