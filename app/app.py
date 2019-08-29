from flask import Flask, session, request, render_template, redirect, url_for
from .config import Config

from .data import questions, answers, extraquestion, rec_text, rec_jobs

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=['GET', 'POST'])
def yrkestest():
    if request.method == 'POST':
        return redirect(url_for('fraga'))
    else:
        session.clear()
        return render_template("start.html")


def rakna_poang(extra=None):
    resultat = {'d': 0, 'i': 0, 's': 0, 'c': 0}
    
    for index, answer in enumerate(session['svar']):
        value = answers[index][answer]
        if index == 12 or index == 13:
            resultat[value] += 2
        else:
            resultat[value] += 1

    if extra:
        resultat[extra] += 1

    session['resultat'] = resultat

    return None


def testa_mest_svar():
    maximum = max(session['resultat'].values())
    antal = [k for k, v in session['resultat'].items() if v == maximum]
    if len(antal) > 1:
        session['utslagsfraga'] = antal
        return True
    else:
        return False


@app.route("/fraga/", methods=['GET', 'POST'])
def fraga():
    if request.method == 'POST':
        session['svar'].append(request.form.get('svar', type=int))
        session['fid'] = request.form.get('fid', type=int) + 1
    else:
        session['fid'] = 0
        session['svar'] = []

    if session['fid'] == 20:
        rakna_poang()
        flera_max = testa_mest_svar()

        if flera_max:
            return redirect(url_for('utslagsfraga'))
        else:
            return redirect(url_for('resultat'))
    else:
        fid = session['fid']
        content = questions[session['fid']]
        return render_template("fraga.html", fid=fid, content=content)


@app.route("/extrafraga/", methods=['GET', 'POST'])
def utslagsfraga():
    if request.method == 'POST':
        rakna_poang(extra=request.form.get('svar'))
        return redirect(url_for('resultat'))
    else:
        return render_template('extrafraga.html', fraga=extraquestion, val=session['utslagsfraga'])


@app.route("/resultat")
def resultat():
    primary = max(session['resultat'], key=session['resultat'].get)

    temp = session['resultat']
    temp.pop(primary, None)

    secondary = max(temp, key=temp.get)

    secondary_jobs = []

    for job in rec_jobs[secondary]:
        if job not in rec_jobs[primary]:
            secondary_jobs.append(job)

    content = {'description': rec_text[primary], 'primary': rec_jobs[primary], 'secondary': secondary_jobs}
    return render_template("resultat.html", content=content)
