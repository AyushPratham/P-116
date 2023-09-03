from flask import Flask, render_template
app = Flask(__name__)
@app.route("/student_info")
def student_webpage():
    name = "Ayush"
    return render_template('index.html', student_name = name)
app.run(debug = True)
