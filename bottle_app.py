
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, template, Bottle, request, SimpleTemplate
from hashlib import sha256

def create_hash(password):               #this part is taken from
    pw_bytestring = password.encode()    # https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
    return sha256(pw_bytestring).hexdigest()

def index():
	return template("index")
route('/', 'GET', index)

def index_html():
	return template("index")
route('/index.html', 'GET', index_html)

def about():
	return template("about")
route('/about.html', 'GET', about)

def contacts():
	return template("contacts")
route('/contacts.html', 'GET', contacts)

def elon():
	return template("elonmusk")
route('/elonmusk.html', 'GET', elon)

def fail():
	return template("failures")
route('/failures.html', 'GET', fail)

def launch():
	return template("launches")
route('/launches.html', 'GET', launch)

def static_file_callback(filename):
	return static_file(filename, root='./')
route('/static/<filename>', 'GET', static_file_callback)

def photos(filename):
	return static_file(filename, root="./photos")
route('/static/photos/<filename>', 'GET', photos)	

def css(filename):
	return static_file(filename, root="./css")
route('/static/css/<filename>', 'GET', css)

def comment(filename):
    comments = request.forms.comment.strip()
    pswrd = request.forms.password
    terms= request.forms.terms
    hsh1 = create_hash(pswrd)
    point= " ("  + " rate: " + request.forms.get("point") + " )" + "\n"
    while True:
        if hsh1 == "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92" and terms == "accepted":
            comment = open("comment.txt", "a+", encoding='utf-8')
            comment.write(comments + point)
            comment.close()
            return template('./contacts.html')
        elif terms != "accepted":
            return template("./agreements.html")
        else:
            return template("./wrong.html")       
route('/<filename>', 'POST', comment)



#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
