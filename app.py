import os, sys

from flask import Flask, session, request, render_template, redirect, url_for
from flask_babel import Babel
from flask_babel import gettext, ngettext, refresh
from .config import Config


from .data import questions, answers, extraquestion, segmentQuestion, rec_text, rec_jobs, addextraquestions, addextraquestionsanswers, how_many_questions


def rakna_poang(extra=None):
    resultat = {'d': 0, 'i': 0, 's': 0, 'c': 0}

    for index, answer in enumerate(session['svar']):
        value = answers[index][answer]
        if index == 14 or index == 15:
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

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        if request.args.get('lang'):
            session['lang'] = request.args.get('lang')
        return session.get('lang', 'sv')

    @app.route("/", methods=['GET', 'POST'])
    def yrkestest():
        if request.method == 'POST':
            session['numberofquestions'] = 10

            session['fid'] = 0
            session['svar'] = []

            return redirect(url_for('fraga'))
        else:
            session.clear()
            return render_template("start.html")

    @app.route("/fraga/", methods=['GET', 'POST'])
    def fraga():
        if request.method == 'POST':
            session['svar'].append(request.form.get('svar', type=int))
            session['fid'] = request.form.get('fid', type=int) + 1
        else:
            fid = session['fid']
            content = questions[session['fid']]
            progress = session['numberofquestions']
            return render_template("fraga.html", fid=fid, content=content, progress=progress)

        if session['fid'] == session['numberofquestions']:
            rakna_poang()
            flera_max = testa_mest_svar()

            if flera_max:
                return redirect(url_for('utslagsfraga'))
            else:
                return redirect(url_for('education'))
        else:
            return redirect(url_for('fraga'))

    @app.route("/extrafraga/", methods=['GET', 'POST'])
    def utslagsfraga():
        if request.method == 'POST':
            rakna_poang(extra=request.form.get('svar'))
            return redirect(url_for('education'))
        else:
            return render_template('extrafraga.html', fraga=extraquestion, val=session['utslagsfraga'])

    @app.route("/utbildning", methods=['GET', 'POST'])
    def education():
        if request.method == 'POST':
            session['education'] = request.form.get('svar')
            return redirect(url_for('resultat'))
        else:
            return render_template('education.html', fraga=segmentQuestion)

    @app.route("/resultat")
    def resultat():
        primary = max(session['resultat'], key=session['resultat'].get)
        education = session['education']
        language = get_locale()

        temp = session['resultat']
        temp.pop(primary, None)

        secondary = max(temp, key=temp.get)

        secondary_jobs = []

        for job in rec_jobs[secondary][education]:
            if job not in rec_jobs[primary][education]:
                secondary_jobs.append(job)

        content = {'description': rec_text[primary], 'primary': rec_jobs[primary][education], 'secondary': secondary_jobs, 'language': language}
        return render_template("resultat.html", content=content)

    return app


app = create_app()
