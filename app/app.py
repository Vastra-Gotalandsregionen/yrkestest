from flask import Flask, session, request, render_template, redirect, url_for

from data import questions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route("/", methods=['GET', 'POST'])
def yrkestest():
    if request.method == 'POST':
        return redirect(url_for('fraga'))
    else:
        return render_template("start.html")


@app.route("/fraga/", methods=['GET', 'POST'])
def fraga():
    if request.method == 'POST':
        session['svar'].append(int(request.form['svar']))
        session['fid'] = int(request.form['fid']) + 1
    else:
        session['fid'] = 0
        session['svar'] = []

    if session['fid'] == 20:
        return redirect(url_for('resultat'))
    else:
        content = [session['fid'], questions[session['fid']]]
        return render_template("fraga.html", content_data=content)


@app.route("/resultat")
def resultat():
    return render_template("resultat.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
