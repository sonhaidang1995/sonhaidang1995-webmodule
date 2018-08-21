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

#Cách của Nguyên:
# Tạo ra 1 list các list có các thông tin lần lượt là danh sách username
# danh sách họ tên, tuổi, sở thích v..v. trong đó thứ tự lần lượt trong các list con sẽ tương ứng với 
# thứ tự username => câu lệnh => lấy ra index, vị trí của trường username trong list con đầu tiên
# Các list các lấy ra các phần tử có index giống với user name và in ra
 