from flask import Flask,render_template,request
import re
app = Flask(__name__)

@ app.route("/")
def home_page():
    return render_template("index.html")

@ app.route("/results",methods=["GET", "POST"])
def regex_match():
    matches = []
    if request.method == 'POST':
        input_str = request.form.get("test_string")
        regexp = request.form.get("regex")
        test_strings = input_str.splitlines()
        for string in test_strings:
            if re.match(regexp,string):
                matches.append(string)
            else:
                matches.append(f"{string} does not match the pattern.")
    return render_template('index.html', matches=matches)

@app.route("/validate-email", methods=["GET","POST"])
def validate_email():
    email_result = ""
    if request.method == "POST":
        inp_email = request.form.get("email")
        regex_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(regex_pattern, inp_email):
            email_result = f"Email '{inp_email}' is valid."
        else:
            email_result = f"Email '{inp_email}' is not valid."
    return render_template('index.html', email_result=email_result)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5000)
