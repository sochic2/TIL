from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕하세요!!!'

# @app.route('/html')
# def html():
#     return render_template('chicken.html')    
# #chicken.html 페이지를 띄워주세요.



# @app.route('/html_name/<string:name>')
# def html_name(name):
#     return render_template('chicken.html', your_name = name)


@app.route('/dictionary/<string:word>')
def html_word(word):
    word_dict = {"grape" : "포도", "apple": "사과" }
    return render_template('workshop.html', word = word, word_dict = word_dict)