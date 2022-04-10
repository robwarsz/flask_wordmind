from fileinput import filename
from flask import Flask, request, url_for, redirect, render_template, session
from io import open
import random


app = Flask(__name__)
app.secret_key = "slowoku"

@app.route('/')
def index():
    desc = f'''
    This is index
    '''
    return render_template('index.html',desc=desc) 

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method =='GET':
        return render_template('form.html') 
    else:
        if 'email' in request.form:
            email = request.form['email']
        if 'pswd' in request.form:
            pswd = request.form['pswd']   
        
        return render_template('form-result.html', email=email, pswd=pswd) 

@app.route('/slowoku',methods=['GET','POST'])
def slowoku():
    if request.method =='GET':
        filename='static/slowa5.txt'
        selected_words=[]
        with open(filename,'r', encoding="utf-8") as file:
            for line in file:
                line = line.rstrip('\n',)
                if len(line)==5:
                    selected_words.append(line)            
        file.close

        filename='static/slowa.txt'
        words=[]
        user_words=[]
        with open(filename,'r', encoding="utf-8") as file:
            for line in file:
                line = line.rstrip('\n',)
                if len(line)==5:
                    words.append(line)
                    # print(line)
        file.close
        num1 = random.randint(0, 150)

        session['selected_word']=selected_words[num1]
        session['user_words']=user_words

        return render_template('slowoku.html',words=words,selected_word=selected_words[num1],user_words=user_words) 
    else:
        filename='static/slowa.txt'
        words=[]
        with open(filename,'r', encoding="utf-8") as file:
            for line in file:
                line = line.rstrip('\n',)
                if len(line)==5:
                    words.append(line)
                    # print(line)
        
        if 'slowo' in request.form:
            slowo = request.form['slowo']
            # print(slowo)
            user_words=session['user_words']    
            if slowo in words and 'user_words' in session:
                user_words=session['user_words']
                user_words.append(slowo)
                session['user_words']=user_words
                print(user_words)
        
        if 'selected_word' in session:
          selected_word = session['selected_word']
                
        file.close
        if slowo not in words:
            slowo = 'W słowniku nie występuje: ' + slowo
            print(slowo)
            return render_template('slowoku.html',words=words,selected_word=selected_word,user_words=user_words,slowo=slowo)
        
        return render_template('slowoku.html',words=words,selected_word=selected_word,user_words=user_words,slowo=slowo)    



