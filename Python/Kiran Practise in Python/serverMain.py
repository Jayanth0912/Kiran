# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request
from practise import logger

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    logger.info("Successfully Executed Hello Wor1d")
    return 'Hello World'

@app.route('/addNums')
# ‘/’ URL is bound with hello_world() function.
def add_nums():
    try:
        a = int(request.args.get("a",0))
        b = int(request.args.get("b",0))
        logger.info("Successfully Executed Add Nums for " + str(a) +" , " + str(b))
        return str(a+b)
    except Exception as e:
        logger.error(e)

@app.route('/diffNums')
# ‘/’ URL is bound with hello_world() function.
def diff_nums():
    try:
        a = int(request.args.get("a",0))
        b = int(request.args.get("b",0))
        logger.info("Successfully Executed Add Nums for " + str(a) +" , " + str(b))
        return str(a-b)
    except Exception as e:
        logger.error(e)



# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
	# on the local development server.
	app.run(port=7000)
