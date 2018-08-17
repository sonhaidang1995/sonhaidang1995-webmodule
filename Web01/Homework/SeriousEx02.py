from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def background(username):
    users = {
	"hai" :{
			"name" : "Dang Son Hai",
			"age" : 23
            },
    "son" :{
			"name" : "Dang Hai Son",
			"age" : 23
            },
    "dang" :{
            "name" : "Hai Son Dang",
            "age" : 23
            }
    }
    if username in users:
        return render_template('serious02.html',username = users[username])
    else:
        return 'User not found'
        
if __name__ == '__main__':
  app.run(debug=True)
 