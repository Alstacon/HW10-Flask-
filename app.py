from utils import load_candidates
from flask import Flask
from person import Person

app = Flask(__name__)

candidates = load_candidates()


@app.route('/')
def page_index():
    list = []
    for n in range(0, len(candidates)):
        page = Person(candidates[n])
        example = page.index(candidates)
        list.append(example)
    return "_".join(list)


@app.route('/candidates/<int:id>')
def page_candidates(id):
    person = Person(candidates[id - 1])
    return f"<p><img src='{person.picture}'></p>" \
           f"<p>Кандидат - {person.name}</p>" \
           f"<p>Позиция - {person.position}</p>" \
           f"<p>Скиллы - {person.skills}</p>"


@app.route('/skills/<skill>')
def page_skills(skill):
    list = []
    for n in range(0, len(candidates)):
        picked = Person(candidates[n])
        if skill.lower() in picked.skills.lower().split(', '):
            picked = str(picked)
            list.append(picked)
    return '_'.join(list)


app.run()
