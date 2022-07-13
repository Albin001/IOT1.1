from flask import *
app=Flask(__name__)
@app.route('/')
def n2():
    return render_template('login.html')
@app.route('/menu')
def sw1():
    return render_template('user.html')
@app.route('/check')
def check():
    return  render_template('message.html')
@app.route('/message1/<a>/<b>')
def m2(a,b):
    return "Your username {} and Password {}".format(a,b)
@app.route('/log',methods=['POST','GET'])
def n3():
    a1="albin"
    a2="123"
    if request.method=='POST':
        user = request.form['yt']
        pass1 = request.form['yt1']
        if(a1==user and a2==pass1):

             return render_template('user.html')
        else:
            return redirect(url_for('check'))
    else:
        user = request.args.get('yt')
        pass1 = request.args.get('yt1')
        return redirect(url_for('message1',a=user,b=pass1 ))
@app.route('/dash')
def d2():
    return render_template('dash.html')
@app.route('/set')
def s1():
    return render_template('settings.html')
@app.route('/login')
def log():
    return render_template('login.html')
@app.route('/rt/<name>/<name1>/<name2>')
def success(name,name1,name2):
   return " Temperature {} , Moisture {} and Water {} ".format(name,name1,name2)
@app.route('/process',methods=['POST','GET'])
def p2():
   if request.method == 'POST':
      user = request.form['nm']
      user1 = request.form['nm1']
      user2 = request.form['nm2']
      return redirect(url_for('success',name = user,name1=user1,name2=user2))
   else:
      user = request.args.get('nm')
      user1 = request.form['nm1']
      user2 = request.form['nm2']
      return redirect(url_for('rt',name = user,name1=user1,name2=user2))
if(__name__=='__main__'):
    app.run(debug=True)