# program language -> web framework -> web
# flask
# fapp => câu lệnh tắt tạo flask
from flask import Flask, render_template
app = Flask(__name__)
# tạo ra 1 sever Flask(__name__)

@app.route('/')
def index():
    return 'Bùm'

@app.route('/hello')
def say_hello():
    # return '<h1>Hello from the other side</h1>'
    return render_template('index.html')
# Tất cả các render_template đều phải đặt trong folder tên "templates"
# Return string giống như html => có thể định dạng kiểu chữ



# @app.route('/hello/say-hi')
# def say_hi():
#     return 'Hi Hai'
@app.route('/hello/say-hi/<name>/<age>')
def say_hi(name,age):
    return 'Hi {}, you are {} years old'.format(name,age)

@app.route('/sum/<numb1>/<numb2>')
def sum(numb1,numb2):
    #Return '{} + {} = {}'.format(numb1,numb2,numb1+numb2) => numb1, numb2 là string 44,55 => 4455
    result= int(numb1) + int(numb2)
    return '{} + {} = {}'.format(numb1,numb2,result)
    #Return result => lỗi do chỉ có thể return string, int không thể return ra được
    # Return str(result) => correct hoặc return str(int(numb1) + int(numb2))
    # => có thể quy định kiểu dữ liệu của parameter
@app.route('/test/<int:a>/<int:b>')
def sum1(a,b):
    return str(a + b)

if __name__ == '__main__':
# Kiểm tra có phải file app được chạy trực tiếp hay không
# Ví dụ khi import turtle, random => thì turtle, random đang được chạy gián tiếp
# Chạy trực tiếp => chạy thẳng file
  app.run(debug = True)
# debug = True => mỗi khi thông tin code thay đổi => server sẽ tự cập nhật lại thông tin tục
# debug = False => muốn cập nhật lại thông tin => phải chạy lại file code
 