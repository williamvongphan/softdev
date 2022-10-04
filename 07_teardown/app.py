"""
Team JAW: William Vongphanith, Abid Talukder, Jonathan Song
SoftDev
K07 -- Flask
2022-10-03
Time Spent: 0.4 hour
"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run(
    host="0.0.0.0", # fix for remote machine -- allows me to access from 1.mcdns.me:5000
)  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. I've seen this syntax in Java: importing a class from a package.
1. / is the root directory. Or in this case, the root route.
2. This will print to the terminal.
3. This will print __main__ if this is the main file being run.
4. This will appear in the browser once it is pointed towards the root route.
5. It's a function!
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
