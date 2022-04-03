import app

if __name__ == "__main__":
    app.db.create_all()
    app.app.run()
