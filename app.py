from flask import Flask
import random
import requests

app = Flask(__name__)

def magic_ball():
    answer=random.choice(['It is certain.','Yes - definitely.','Without a doubt.',
    'Most likely.','Outlook good.','As I see it, yes.','Ask again later.',
    'Better not to tell you now.','Reply hazy, try again.',
    'My sources say no.','Don\'t count on it.','Very doubtful.'])
    return("<h1 style=color:blue;><div align='center'><br>"+answer+'</h1>')


@app.route('/', methods=['GET'])
def home():

    return'''<h1><div align='center'><br>8-Ball webapp</h1><br><div align='center'>\
    <button style="height: 35px; width: 100px" onclick=window.location.href='/api/ver0/resources/8ball';>Shake the ball!</button></a><br><br><br>\
    <button onclick=window.location.href='rodney.link';>back to rodney.link</button></a>'''

@app.route('/api/ver0/resources/8ball', methods=['GET'])
def api_8ball():

    return(magic_ball()+"<div align='center'><br>\
    <button style='height: 35px; width: 100px' onclick=window.location.reload();>Shake again</button></a><br><br><br>\
    <button onclick=window.location.href='rodney.link';>back to rodney.link</button></a>'")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Error</h1><p>Page doesn't exist.</p>", 404

if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)
