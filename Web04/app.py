from flask import *
from mongoengine import *
from models.video import Video
from youtube_dl import YoutubeDL
from models.account import Account

import mlab

app = Flask(__name__)
app.secret_key = "a super super secret key" 
# Phải có secret_key thì section mới có hiệu lực

mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html',videos = videos)

@app.route('/admin',methods = ["GET","POST"])
def admin():
    if "loggedin" in session:
        if session['loggedin'] == True:
            if request.method == "GET":
                videos = Video.objects()
                return render_template('admin.html',videos=videos)
            elif request.method == "POST":
                form = request.form
                link = form['link']

                ydl = YoutubeDL()
                data = ydl.extract_info(link, download = False)
                
                title = data['title']
                views = data['view_count']
                thumbnail = data['thumbnail']
                youtube_id = data ['id']

                video = Video(
                    title = title,
                    views = views,
                    thumbnail = thumbnail,
                    youtube_id = youtube_id,
                    link = link
                )
                video.save()
                return redirect(url_for('admin'))
        else:
            return "Yêu cầu đăng nhập"
    else:
        return "Yêu cầu đăng nhập"
@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    if youtube_id is not None:
        youtube_id = youtube_id
        return render_template('detail.html',youtube_id = youtube_id)
    else:
        return "Not found"

@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for("admin"))
        else:
            return "Đi chỗ khác chơi"

# found_user = User.objects(username = username, password = password)

@app.route('/logout')
def logout():
    session['loggedin'] = False
    return redirect(url_for('login'))


@app.route('/sign-up', methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('sign-up.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']

        account = Account(
            name = name,
            email = email,
            username = username,
            password = password
        )
        account.save()
        return "Sign up succesfull!!"

if __name__ == '__main__':
  app.run(debug=True)
 

# Token
# secret key
# session : dictionary + tên cố định