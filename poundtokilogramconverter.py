from flask import Flask
from flask import request

app = Flask(__name__)

html = """
<center>
<form action='/convert' method='POST'>
Pound to kilo:<input type='text' name='pound' value='{pound}'> lb = <span id='kilo'>{kilo}</span> kg <br>
<input type='submit' value='Submit'>
</form>
"""


@app.route("/")
def index():
    lb = 0
    kg = 0
    return html.format(pound=lb, kilo=kg)

@app.route("/convert", methods=['POST'])
def convert():
    # you can retrieve the pound value from request.form["pound"]
    # Now complete the logic here
    # 1 lb = 0.453592 kg
    html = "{pound}lb = {kilo}kg"
    lb = request.form["pound"]
    try:
        kg = float(lb) * 0.453592
        return html.format(pound=lb, kilo=kg)
    except ValueError:
        return 'Error!! Non-numeric value is found as a input.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)



