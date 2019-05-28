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

periods = [period1, period2, period3, period4, period5, period6, period7, period8]

for p in periods:
    p.clear()

print('Generating List of Teachers')

# Looping to create teacher names
for i in range(8):
    j = 3
    name = options.cell(j, i+1).value
    while name != '':
        p = periods[i]
        p.update_cell(1, j - 2, name)
        j = j + 1
        name = options.cell(j, i + 1).value
print('Generation Complete')
print('Starting Server')
