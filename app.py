from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# credentials and gspread setup
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# sheet setup
options = client.open("Options").sheet1
idsheet = client.open("id").sheet1
period1 = client.open("Library Passes").get_worksheet(0)
period2 = client.open("Library Passes").get_worksheet(1)
period3 = client.open("Library Passes").get_worksheet(2)
period4 = client.open("Library Passes").get_worksheet(3)
period5 = client.open("Library Passes").get_worksheet(4)
period6 = client.open("Library Passes").get_worksheet(5)
period7 = client.open("Library Passes").get_worksheet(6)
period8 = client.open("Library Passes").get_worksheet(7)

periods = [period1, period2, period3, period4, period5, period6, period7, period8]

# variable setup
maxStudents = int(options.cell(2, 9).value)
name = ""
pArr = [0, 0, 0, 0, 0, 0, 0, 0]

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('index.html')


@app.route("/select_period", methods=['POST', "GET"])
def select_period():
    global name
    if request.method == 'POST':
        data = request.form['input']
        try:
            sid = idsheet.find(data)
        except:
            return render_template("error.html")
        name = idsheet.cell(sid.row, sid.col + 1).value
        if name == '':
            return render_template("error.html")
    return render_template('select_period.html', name=name, pArr=pArr, maxStudents=maxStudents)


@app.route("/select_teacher", methods=['POST', "GET"])
def select_teacher():
    global name
    global pArr
    global maxStudents
    global periods

    if request.method == 'POST':
        pIndex = int(request.form['period'])
        if pArr[periods] > maxStudents:
            return render_template('full.html')
        teacherList = []
        teacher = periods[pIndex].cell(1, 1).value
        i = 1
        while teacher != '':
            teacherList.append(teacher)
            i += 1
            teacher = periods[pIndex].cell(1, i).value
    return render_template('select_teacher.html', name=name, p=periods, teacherList=teacherList)


if __name__ == '__main__':
    app.run()
