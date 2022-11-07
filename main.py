import datetime as dt

from flask import Flask, render_template, request

from check_dates import check_dates

app = Flask(__name__)


@app.route('/')
def index():
    current_start_date = request.args.get('current_start_date', type=str)
    current_finish_date = request.args.get('current_finish_date', type=str)
    print(current_start_date, current_finish_date)
    result = "Enter dates"
    if current_start_date and current_finish_date:
        current_start_date = dt.date.fromisoformat(request.args.get('current_start_date', type=str))
        current_finish_date = dt.date.fromisoformat(request.args.get('current_finish_date', type=str))
        result = check_dates(current_start_date, current_finish_date)
    return render_template(
        'index.html',
        result=result,
        current_start_date=current_start_date,
        current_finish_date=current_finish_date
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
