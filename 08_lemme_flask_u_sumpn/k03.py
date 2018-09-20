# Soojin Choi
# SoftDev1 pd08
# K08 -- Fill Yer Flask
# 2018 - 09 - 19

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign fxn to route
def index():
    print('the __name__ of this module is...')
    print(__name__) #where will this go?
    return '/ --leads to----> index <br> /greeting --leads to----> hello_world <br> /info --leads to----> some_info <br> /fact --leads to----> fun_fact'

@app.route('/greeting')
def hello_world():
   return 'No hablo queso!'

@app.route('/fact')
def fun_fact():
   return 'Some bold words'

if __name__ == '__main__':
    app.debug = True
    app.run()


