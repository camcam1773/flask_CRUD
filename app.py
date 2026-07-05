from flask import Flask, render_template, request, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()
main_bp = Blueprint("main", __name__)


class Todo(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return "<Task %r>" % self.id


@main_bp.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "Commit error"
    else:
        tasks = db.session.scalars(db.select(Todo).order_by(Todo.date_created)).all()
        return render_template("index.html", tasks=tasks)


@main_bp.route("/delete/<int:id>")
def delete(id):
    task_to_delete = db.get_or_404(Todo, id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting that task"


@main_bp.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = db.get_or_404(Todo, id)

    if request.method == "POST":
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue updating your task"
    else:
        return render_template("update.html", task=task)


def create_app(config_overrides=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if config_overrides:
        app.config.update(config_overrides)

    db.init_app(app)
    app.register_blueprint(main_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=8080)
