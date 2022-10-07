'''
TEAM KrEWes: Elizabeth Paperno, Raven (Ruiwen) Tang, William Vongphanith
SoftDev
K08 -- Using Flask to Display Input on a Server
2022-10-06
Time Spent: 0.6 hours
DISCO
___________
- You can import methods from a file using  from [file] import [function]
- It would be good practice to have the function where generate output called seperate in a main function
- host='0.0.0.0' allows you to listen on network and local host
- Good practice to call run() in main() explicity.
QCC
___________
- Do you not include the extension (e.g numpercruncher.py vs just numbercruncher)
when you import from python files? If we ever import anything that is not a module
or python file should we include the extension?
- If we had multiple functions defined would all the functions be run and displayed on the web server?
OPS SUMMARY
___________
- First we essentially copied the flask starter code. Then we imported the choose_occupation
function from our origninal numbercruncher file in 06_py-csv. We then redefined the main function
in flask to return the output of numbercruncher (instead of "No hablo queso!"). We then called
app.run explicitly in main().
'''

from numbercruncher import choose_occupation
from flask import Flask

app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def occupation():
    """
    Returns the output of choose_occupation from numbercruncher.py as a string to Flask

    Returns:
        str: output of choose_occupation
    """
    # choose occupation
    return choose_occupation()


# serve to world
def main():
    app.run(host='0.0.0.0')

# main function, run when file is called directly
if __name__ == '__main__':
    main()