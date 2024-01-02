from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello world'

@app.route('/calculator',methods=['GET'])
def math_operations():
    operation = request.json['operation']
    num1 = request.json['num1']
    num2 = request.json['num2']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        print('Choose Operator')

    return result


if __name__ = '__main__'
    app.run(debug=True)