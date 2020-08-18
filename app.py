from flask import Flask

from orcalib import system_info

app = Flask(__name__)


@app.route("/")
def index():
    return system_info.result
    # return template_rendered("index.html", system_info=systeminfo.result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
