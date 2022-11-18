import bs4
import csv # モジュール"CSV"の呼び出し
import sys

output_file_name = 'kimarite_hassei_history.csv'
f = open("output_sample.csv", "w", encoding = 'utf-8')
writecsv = csv.writer(f, lineterminator='\n')

for i in range(1927,2023):
	input_file = f'html/kimarite{i}.html'
	soup = bs4.BeautifulSoup(open(input_file, encoding = 'utf-8'), 'html.parser', from_encoding='utf-8')
	kimarite_tr = soup.select('tr', class_='gs')
	
	for trtr in kimarite_tr:
		
		td_kimarite = trtr.find('td', class_='left')
		if td_kimarite is None:
			continue
		kimarite = td_kimarite.text.strip()
		td_hassei = trtr.find('td', class_='center')
		hassei = td_hassei.text.strip()
				
		csvlist = [i, kimarite, hassei] # 配列を作成
		
		#print(csvlist)
		writecsv.writerow(csvlist) # 出力		

f.close() # CSVファイルを閉じる
sys.exit()
