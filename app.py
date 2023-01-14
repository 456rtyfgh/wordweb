from flask import Flask, render_template, request, redirect

app = Flask(__name__)

words = [
    {'id':1, 'english':'tree', 'korean':'나무'},
    {'id':2, 'english':'apple', 'korean':'사과'},
    {'id':3, 'english':'antidisestablishmentarianism', 'korean':'반체제주의'},
    {'id':4, 'english':'bow', 'korean':'활'},
    {'id':5, 'english':' pneumonoultramicroscopicsilicovolcanoconiosis', 'korean':'폐,허파'}
]
nextId = len(words) + 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list/')
def list():
    return render_template('list.html', word_list=words)

@app.route('/word/<int:id>/')
def read(id):
    english = ''
    korean = ''
    for word in words:
        if id == word['id']:
            english = word['english']
            korean = word['korean']
            break

    return render_template('word.html', id=id, english=english, korean=korean)

@app.route('/new/')
def create():
    return render_template('create.html')

@app.route('/create/', methods=['POST'])
def post_create():
    global nextId
    english = request.form['english']
    korean = request.form['korean']
    newword = {'id': nextId, 'english': english, 'korean': korean}
    words.append(newword)
    nextId += 1
    return redirect('/word/{}/'.format(newword['id']))

@app.route('/modyfi/<int:id>/')
def update(id):
    english = ''
    korean = ''
    for word in words:
        if id == word['id']:
            english = word['english']
            korean = word['korean']
            break

    return render_template('update.html', id=id, english=english, korean=korean)        

app.run(debug=True)