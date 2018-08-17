from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bùm'

@app.route('/hello')
def say_hello():
    # title = "Musical Instrument"
    # content = "Ukulele"
    # author = "Guitar"
    posts = [
        {
        "title": "Musical Instrument",
        "content": "Ukulele",
        "author": "Guitar",
        "author_sex": 1
        },
        {
        "title": "Thơ con ếch",
        "content": "Từ từ",
        "author": "Tuấn Anh",
        "author_sex": 0
        },
        {
        "title": "Đen vãi",
        "content": "Gục gã trước cổng thiên đường",
        "author": "Đen",
        "author_sex": 1
        }
        ]
    return render_template('test.html',
                            posts = posts)
    # return render_template('test.html',
    #                         post_title = "xxx",
    #                         post_content = "yyy",
    #                         post_author = "zzz"
    #                         )                        
    # => Nếu khai báo từng biến sẽ rất dài => nhét toàn bộ biến vào 1 dictionary
if __name__ == '__main__':
  app.run(debug = True)
  

# Data + template => call "render_template"
 