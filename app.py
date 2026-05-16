from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    expression = ""
    
    if request.method == 'POST':
        # Get the math expression typed by the user from the hidden form field
        expression = request.form.get('expression', '')
        
        # If the 'C' (Clear) button was clicked
        if 'clear' in request.form:
            expression = ""
            result = ""
        # If the '=' (Equal) button was clicked
        elif 'equal' in request.form:
            try:
                if expression:
                    # eval() calculates the string expression (e.g., "5*2+3")
                    # We block standard built-ins for an added layer of safety
                    result = str(eval(expression, {"__builtins__": None}, {}))
            except Exception:
                result = "Error"
                
    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)