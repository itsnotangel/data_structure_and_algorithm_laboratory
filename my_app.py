from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Works page (same as index, optional separate page)
@app.route('/works')
def works():
    return render_template('works.html')

# Profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Uppercase converter
@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('uppercase.html', result=result)

# Circle area calculator
@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        radius = request.form.get('radius', type=float)
        if radius is not None:
            area = 3.14159 * radius * radius
    return render_template('circle.html', area=area)

# Triangle area calculator
@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        base = request.form.get('base', type=float)
        height = request.form.get('height', type=float)
        if base is not None and height is not None:
            area = 0.5 * base * height
    return render_template('triangle.html', area=area)

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)