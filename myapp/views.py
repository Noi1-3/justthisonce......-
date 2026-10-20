from django.http import HttpResponse
from datetime import datetime, timedelta

def current_datetime(request):
    return HttpResponse(f'<html><body>{datetime.now()}</body></html>')

def multiplication_table(request):
    html = '<html><body><table border="1">'
    for i in range(1, 11):
        html += '<tr>'
        for j in range(1, 11):
            html += f'<td>{i*j}</td>'
        html += '</tr>'
    html += '</table></body></html>'
    return HttpResponse(html)

def programmers_day(request):
    year = datetime.now().year
    date = datetime(year, 1, 1) + timedelta(days=255)
    return HttpResponse(f'<html><body>{date.strftime("%Y-%m-%d")}</body></html>')
