import time
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_unix_time():
    current_time = int(time.time())
    return f"The current Unix time is: {current_time}"


if __name__ == "__main__":
    app.run()
