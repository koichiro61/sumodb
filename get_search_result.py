from bs4 import BeautifulSoup
from urllib import request
import ssl
import sys
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getSource(url, outf, encoding):
	response = request.urlopen(url, context=ctx)
	soup = BeautifulSoup(response, "html.parser", from_encoding='shift_jis')
	response.close()

	f = open(outf, 'w', encoding='utf_8')
	print(soup.prettify(), file=f)
	f.close

for i in range(1927,2023):
	target_url = f'http://sumodb.sumogames.de/Query_bout.aspx?l=j&show_form=0&group_by=kimarite&year={i}&rowcount=4&onlyw1=on'
	getSource(target_url, f'html/kimarite{i}.html', 'shift_jis')
	time.sleep(5)
