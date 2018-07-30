from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from users.models import CustomUser

# Create your views here.

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open('Class of 2021 Student E-mails and Dues').sheet1

sheet1 = wks.get_all_records()
# wks.find(user_email)                       find a string
# values_list = worksheet.col_values(1)      all values from column 1

def index(request):

    return render(request, 'dues/index.html')
