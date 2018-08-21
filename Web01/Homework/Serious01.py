from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = weight/((height/100)**2)
    print(bmi)
    # Way 01
    # posts = {
    #     'weight': weight,
    #     'height': height,
    #     'BMI': BMI
    # }
    # return render_template('serious01.html', posts = posts)

    # Way 02    
    condition = 0
    if bmi < 16:
        condition = 'Severly underweight'
    elif bmi < 18.5:
        condition = 'Underweight'
    elif bmi < 25:
        condition = 'Normal'
    elif bmi < 30:
        condition = 'Overweight'
    else:
        condition = 'Obese'
    return condition
if __name__ == '__main__':
  app.run(debug = True)
 