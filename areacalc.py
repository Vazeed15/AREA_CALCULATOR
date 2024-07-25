from flask import Flask, render_template, request

app = Flask(__name__)

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    import math
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def square_area(side):
    return side ** 2

def parallelogram_area(base, height):
    return base * height

@app.route('/', methods=['GET', 'POST'])
def calculate():
    area = None
    dimensions = []

    if request.method == 'POST':
        shape = request.form['shape']
        if shape == 'rectangle':
            length = request.form['length']
            width = request.form['width']
            if length and width:
                length = float(length)
                width = float(width)
                area = rectangle_area(length, width)
                dimensions = [('Length', length), ('Width', width)]
        elif shape == 'circle':
            radius = request.form['radius']
            if radius:
                radius = float(radius)
                area = circle_area(radius)
                dimensions = [('Radius', radius)]
        elif shape == 'triangle':
            base = request.form['base']
            height = request.form['height']
            if base and height:
                base = float(base)
                height = float(height)
                area = triangle_area(base, height)
                dimensions = [('Base', base), ('Height', height)]
        elif shape == 'square':
            side = request.form['side']
            if side:
                side = float(side)
                area = square_area(side)
                dimensions = [('Side', side)]
        elif shape == 'parallelogram':
            base = request.form['parallelogram_base']
            height = request.form['parallelogram_height']
            if base and height:
                base = float(base)
                height = float(height)
                area = parallelogram_area(base, height)
                dimensions = [('Base', base), ('Height', height)]
    
    return render_template('areacalc.html', area=area, dimensions=dimensions)

if __name__ == '__main__':
    app.run(debug=True)
