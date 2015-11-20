from flask import Flask, request, url_for
app = Flask(__name__)
from parseRecpie import Recipe,requestRecipe
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/recipe/', methods=['POST'])
def recipe():
     
    toAdd =Recipe(request.form['recipe_url'])
    toAdd.parseObject.save()
    return "OK!"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5004)
