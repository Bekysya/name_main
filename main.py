from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    uq = {'nick':'Bek'}
    posts = [
        {
            'author': {'username':'Ivan'},
            'body': 'Привет, всем. Кто тут есть'
        },
        {
            'author': {'username': 'Sasha'},
            'body': 'Все тут, ты задержался'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Медвед'
        }
    ]
    return render_template('index.html', title = 'Главная страница', name = 'Фруктик', uq = uq, posts = posts)

@app.route('/index')
def main():
    return render_template('hell.html')

if __name__=='__main__':
    app.run()