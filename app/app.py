from flask import Flask, request, render_template, redirect, url_for

from data import questions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route("/")
def yrkestest():
    return render_template("start.html", questions=questions)


@app.route("/fraga/", methods=['GET', 'POST'])
def fraga():
    if request.method == 'POST':
        fraga_id = int(request.form['fraga']) + 1
    else:
        fraga_id = 0

    if fraga_id == 20:
        return redirect(url_for('resultat'))
    else:
        content = [fraga_id, questions[fraga_id]]
        return render_template("fraga.html", content_data=content)


@app.route("/resultat")
def resultat():
    return render_template("resultat.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
