#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers='\n'.join(str(num)for num in range(parameter))
    return numbers + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation, num2):
    if operation in ('+', 'sum'):
        result=num1+num2
    elif operation in ('-', 'subtraction'):
        result= num1-num2
    elif operation in('/', 'div','division'):
        result= num1/num2
    elif operation in ('*','multiplication'):
        result= num1 *num2
    elif operation in('%', 'modulus'):
        result=num1%num2
    else:
        return "Invalid operation",400
    return str(result)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
