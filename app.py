from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# credentials and gspread setup
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# sheet setup
options = client.open("Options").sheet1
period1 = client.open("Library Passes").get_worksheet(0)
period2 = client.open("Library Passes").get_worksheet(1)
period3 = client.open("Library Passes").get_worksheet(2)
period4 = client.open("Library Passes").get_worksheet(3)
period5 = client.open("Library Passes").get_worksheet(4)
period6 = client.open("Library Passes").get_worksheet(5)
period7 = client.open("Library Passes").get_worksheet(6)
period8 = client.open("Library Passes").get_worksheet(7)

# variable setup
maxStudents = int(options.cell(2, 9).value)


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
