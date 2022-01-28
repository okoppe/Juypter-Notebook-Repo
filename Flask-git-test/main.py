from flask import Flask, render_template, request, Response, send_from_directory
import os
import git

g = git.cmd.Git(git_dir)
g.pull()
####flask app

app = Flask(__name__)
#hone directory
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
