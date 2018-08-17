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
    if bmi < 16:
        return 'Your BMI: {}. Severely underweight'.format(bmi)
    elif 16 <= bmi < 18.5:
        return "Your BMI: {}. Underweight".format(bmi)
    elif 18.5 <= bmi < 25:
        return "Your BMI: {}. Normal".format(bmi)
    elif 25 <= bmi < 30:
        return "Your BMI: {}. Overweight".format(bmi)
    else:
        return 'Your BMI: {}. Obese'.format(bmi)
if __name__ == '__main__':
  app.run(debug = True)
 