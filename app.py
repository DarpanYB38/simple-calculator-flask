from flask import Flask, render_template, request

app = Flask(__name__)

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = Calculator.add(num1, num2)
            elif operation == "subtract":
                result = Calculator.subtract(num1, num2)
            elif operation == "multiply":
                result = Calculator.multiply(num1, num2)
            elif operation == "divide":
                result = Calculator.divide(num1, num2)

        except ValueError:
            error = "Invalid input. Please enter numeric values for both numbers."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
