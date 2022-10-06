"""

"""

from numbercruncher import choose_occupation
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def occupation():
    # choose occupation
    return choose_occupation()

# serve to world
app.run(host='0.0.0.0')