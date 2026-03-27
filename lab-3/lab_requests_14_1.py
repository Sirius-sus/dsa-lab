from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/number/', methods = ["GET"])
def get_number():
    try:
        param = float(request.args.get('param')) # Преобразование в float
    except:
        return jsonify({"error": "Параметр не задан или задан некорректно"}), 400
    
    # Умножение на случайное число
    random_number = random.randint(1, 100)
    result = random_number * param

    return jsonify({
        "param": param,
        "random_number": random_number,
        "result": result
    })

@app.route('/number/', methods = ["POST"])
def post_number():
    try:
        data = request.get_json() # Получение данных из запроса
        json_param = float(data['jsonParam']) # Чтение параметра jsonParam
    except:
        return jsonify({"error": "Параметр не задан или задан некорректно"}), 400
    
    # Умножение на случайное число, выбор операции
    random_number = random.randint(1, 100)
    result = random_number * json_param
    operation = random.choice(['sum', 'sub', 'mul', 'div'])

    return jsonify({
        "json_param": json_param,
        "random_number": random_number,
        "result": result,
        "operation": operation
    })

@app.route('/number/', methods = ["DELETE"])
def delete_number():
    # Выбор числа и операции
    random_number = random.randint(1, 100)
    operation = random.choice(['sum', 'sub', 'mul', 'div'])

    return jsonify({
        "result": random_number,
        "operation": operation
    })

if __name__ == "__main__":
    app.run(debug=True)
