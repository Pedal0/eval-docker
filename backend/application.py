from flaskr import create_app
from flaskr.routes import bp

app = create_app()
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
