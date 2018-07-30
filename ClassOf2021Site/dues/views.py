from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Create your views here.

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open('Class of 2021 Student E-mails and Dues').sheet1

sheet1 = wks.get_all_records()

def index(request):
    user_email = None
    # user = wks.find(user_email)

    return render(request, 'dues/index.html')
