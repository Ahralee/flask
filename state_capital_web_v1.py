import pymysql
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

"""
Run this from your shell
and then visit http://localhost:4000/ from your browser
"""

home_html = """
<html>
<body background='http://flightattendanttraininghq.com/wp-content/uploads/2017/09/Quiz-Time.png'>
<center>
<h1>Welcome to Quiz World</h1>
<hr>
<li><a href='/state_capital'>State Capital</li>
</center>
</html>
"""

question_answer_html_header = """
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
}
td:nth-child(even){
    color: red;
}
</style>
</head>

<body>
    <center>
    <h1>State Capital Questions</h1> 
    <table> 
"""
question_answer_html_footer = """    
    </table>
    </center>
</body>
</html>
"""


def get_state_capital():
    sc = []
    conn = pymysql.connect(
        host='ahralee.cjnizbfe3nuo.us-west-1.rds.amazonaws.com',
        user='ahralee',
        password='arluv5226',
        db='test',
        charset='utf8'
    )
    curs = conn.cursor()
    sql = "select state, capital from state_capital"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        sc.append({'state': row[0], 'capital': row[1]})
    conn.close()
    return sc


@app.route("/")
def index():
    return home_html


@app.route("/state_capital", methods=['GET'])
def state_capital():
    sc_list = get_state_capital()
    html = question_answer_html_header
    for sc in sc_list:
        qa_pair = "<tr><td>Capital of " + sc['state'] + "</td>" +"<td>" + sc['capital'] + "</td></tr>"
        html += qa_pair
    html += question_answer_html_footer
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)