from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route("/")
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
    <ul>
      <a href="/animals/dogs"><li>Dogs</li></a>
      <a href="/animals/cats"><li>Cats</li></a>
      <a href="/animals/rabbits"><li>Rabbits</li></a>
    </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"""<h1>
               List of {pet_type}
             </h1>"""
  for i, pet in enumerate(pets[pet_type]):
    html += f'''<ul>
                  <a href = "/animals/{pet_type}/{i}">
                    <li>{pet['name']}</li>
                  </a>
                </ul>
              '''
  return html


@app.route("/animals/<pet_type>/<int:i>")
def pet(pet_type, i):
  indice = pets[pet_type]
  info = indice[i]
  return f"""
              <h1>{info['name']}</h1>
              <img src = '{info['url']}'/>
              <p>{info['description']}</p>
            """
