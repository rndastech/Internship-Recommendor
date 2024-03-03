from flask import Flask, render_template, request ,url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Extracting data from the form
    first_name = request.form['q1']
   # last_name = request.form['q2']
    email = request.form['q3']
    black=request.form['q4']
    print(f'email,"hehe"')
    # Writing data to a file
    with open('input1.txt', 'w') as file:
        file.write(f'{first_name}')
    
    #with open('input2.txt', 'w') as file:
       # file.write(f'{last_name}')
    with open('input3.txt', 'w') as file:
        file.write(f'{email}')
    with open('input4.txt', 'w') as file:
        file.write(f'{black}')
    # Starting other_program.py as a subprocess
    subprocess.Popen(['python', 'nwe.py'])
    subprocess.Popen(['python', 'ss2.py'])
    subprocess.Popen(['python', 'plan.py'])
    
    
    #subprocess.Popen(['python', 'ape.py'])
    render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
