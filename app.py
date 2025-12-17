import streamlit as st
from flask import Flask, render_template_string, request

app = Flask(BVCF__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Grade Calculator</title>
</head>
<body>
    <h1>Student Grade Calculator</h1>
    <form method="post" action="/calculate">
        <label for="subjects">Enter the number of subjects:</label>
        <input type="number" id="subjects" name="subjects" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

marks_form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Enter Marks</title>
</head>
<body>
    <h1>Enter Marks for Each Subject</h1>
    <form method="post" action="/result">
        {% for i in range(1, subjects + 1) %}
            <label for="subject{{ i }}">Marks for Subject {{ i }}:</label>
            <input type="number" id="subject{{ i }}" name="subject{{ i }}" required><br>
        {% endfor %}
        <button type="submit">Calculate</button>
    </form>
</body>
</html>
"""

result_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
</head>
<body>
    <h1>Result</h1>
    <p>Total Marks: {{ total }}</p>
    <p>Percentage: {{ percentage }}%</p>
    <p>Grade: {{ grade }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(html)

@app.route("/calculate", methods=["POST"])
def calculate():
    subjects = int(request.form["subjects"])
    return render_template_string(marks_form_html, subjects=subjects)

@app.route("/result", methods=["POST"])
def result():
    total = 0
    marks = []
    for key, value in request.form.items():
        marks.append(int(value))
        total += int(value)
    percentage = total / len(marks)
    grade = ""
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    return render_template_string(result_html, total=total, percentage=percentage, grade=grade)

if __name__ == "__main__":
    app.run(debug=True)