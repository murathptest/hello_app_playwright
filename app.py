from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        agree = request.form.get('agree')
        message = f'Hello {name}, Agree checkbox is {"checked" if agree else "not checked"}'
    return f'''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Agree: <input type="checkbox" name="agree" value="yes"><br>
            <input type="submit">
        </form>
        <p>{message}</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
