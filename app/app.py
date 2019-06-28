from flask import Flask, render_template

from data import questions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route("/")
def yrkestest():
    return render_template("start.html", questions=questions)


@app.route("/fraga/<int:fraga_id>")
def fraga(fraga_id):
    content = [fraga_id + 1, questions[fraga_id]]
    return render_template("fraga.html", content_data=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
