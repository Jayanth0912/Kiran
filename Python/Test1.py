    #
    #
    #
    # num = int(input("enter a number:"))
    # for i in range(2, num):
    #     if num % i == 0:
    #         print(num, "is Not prime number")
    #         break
    # else:
    #     print(num, "is a prime Number")

#
# # Importing flask module in the project is mandatory
# # An object of Flask class is our WSGI application.
# from flask import Flask
#
# # Flask constructor takes the name of
# # current module (__name__) as argument.
# app = Flask(__name__)
#
# # The route() function of the Flask class is a decorator,
# # which tells the application which URL should call
# # the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'
#
# # main driver function
# if __name__ == '__main__':
#
# 	# run() method of Flask class runs the application
# 	# on the local development server.
# 	app.run()

'''
from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/getUserDetails')
def get_user_details():
    return {"name":"sagar"}

@app.route('/saveUser',methods=["POST"])
def saveuser_details():
    print(request.data)
    return {"name":"sagar"}

if __name__=='__main__':
        app.run(port=3000)
'''


json = {
    "name":"Bharath",
    "Age":24,
    "Address":{
        "Door_No":"2-2",
        "Mandal":"Madanapalle",
        "Postal_code":517325
    },
    "languages_known":[
        "Telugu","English"
    ],
    "Hobbies":{"indoor":["Chess","Internet"],"outdoor":["cricket","football"]},
    "PlacesVisited":[
        {
        "name":"Bangalore",
        "Pincode":560100
    },
        {
            "name":"Madanapalle",
            "Pincode":517325
        }
    ]
}
