from flask import Flask,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)




@app.route('/4521')
def clue1():
    return jsonify({'clue':"On my way back to my hideout.I saw this guy.This guy has 4 legs and has hair at night?You might have seen him this morning.Probably I've left my next clue under it",
    'code':"4521"})


@app.route('/3895')
def clue2():
    return jsonify({'clue':"Wah!so you do have detective skills. but probably that won't help you get me.This thing is white in color but turns yellow when falls on the floor.Probably you'll see something here"
    ,'code':"3895"})

@app.route('/1235')
def clue3():
    return jsonify({'clue':"Haa! good thinking there...but I guess you'll have to try harder to reach me.Meet one of my loyal servants.He loses his head in the morning and get it back at nights.You think you can find him? Let's see.",
    'code':"1235"})

@app.route('/7854')
def clue4():
    return jsonify({'clue':"hmm good thinking there..I under estimated you..haha now see if you can guess this...'I stand up and make your day brighter' ",
    'code':"7854"})

@app.route('/1256')
def clue5():
    return jsonify({'clue':"I'm used on heads,toes maybe your entire body,the more I work for my boss the thinner I grow.",
    'code':"1256"})

@app.route('/9561')
def clue6():
    return jsonify({'clue':"You've come this far...I appreciate that...But here on things will not be the same..let's not meet again...still I'll give you a chance. 'this guy likes amplifying what is fed into him and he speaks loudly cuz he's probably the best in it'",
    'code':"9561"})

@app.route('/3644')
def clue7():
    return jsonify({'clue':"Wow you just solved one of the hardes one! lemme give u an easy one : think you can find me where you find books..let's see",
    'code':"3644"})

@app.route('/4932')
def clue8():
    return jsonify({'clue':"haha...this is probably the funniest place to find a clue 'one sheet,two sheets,three sheets, some use more some less'",
    'code':"4932"})

@app.route('/1099')
def clue9():
    return jsonify({'clue':"You've almost found your way...let us see if you break the supreme ones mystery:- 'time to think time to chill,for your next due please go here for a cool cool drink'",
    'code':"1099"})

@app.route('/1007')
def final():
    return jsonify({'clue':'you fool! you started searching for me from the place where i am still hiding..haha',
    'code':"0000"})

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'NO clue here..!!'})
    
if __name__ == '__main__':
    app.run(debug=True)