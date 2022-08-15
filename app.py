from flask import Flask, render_template, request, redirect


command_txt = "ingenting"

number = 0

def number_checker(name_zero, name_one):
    global command_txt
    global number
    if number ==  0:
        number = 1
        print(number)
        command_txt = name_zero
    elif number == 1:
        number = 0
        print(number)
        command_txt = name_one

app = Flask(__name__)
app.debug = True

 
@app.route("/home")
def home():
    return render_template("index.html")
 
@app.route("/commander")
def commander():
    return render_template("command.html", command = command_txt)


@app.route('/middag')
def youtube():
    number_checker(name_one="middag1", name_zero="middag0")
    print(command_txt)
    return "nothing"


if __name__ == "__main__":
    app.run()