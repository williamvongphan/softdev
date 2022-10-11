"""
Team KReWEs: William Vongphanith, Elizabeth Paperno, Konstantin Dubovskiy, and Raven Tang
SoftDev pd2 sec1
K09 -- Some Things Never Change
2022-10-11
"""

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print(__name__) 
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run(
            host="0.0.0.0"
            ) # run app
