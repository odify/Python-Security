# import requests
#
# ::::......
#
#
#if ip == '':
#	ip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(5,250),4))
#
#print('\n\033[4;33mRedirecting...\033[0m')
#print('\033[0;33m  Redirecting \033[0;32m'+hostname+'\033[0;33m to \033[0;32m'+ip+'\033[0;33m...')
#
#r = requests.get('https://'+username+':'+password+'@dynupdate.no-ip.com/nic/update?hostname='+hostname+'&myip='+ip)
#
#
#
#
#if 'good' in r.text:
#	print('\033[4;32mHostname modified successfully\033[0m')
#	print('\033[0;32m  Hostname \033[0;33m'+hostname+'\033[0;32m has been successfully modified to redirect to \033[0;33m'+ip+'\033[0;32m.')
#elif 'badauth' in r.text:
#	print('\033[4;31mAuthentication Error\033[0m')
#	print('\033[0;31m  Failed to authenticate. Please check your credentials and try again.')
#elif 'nohost' in r.text:
#	print('\033[4;31mInvalid Hostname\033[0m')
#	print('\033[0;31m  That Hostname is not associated with your No-IP account.')
#else:
#	print('\033[4;31mError\033[0m')
#	print('\033[0;31m  An unknown error has occurred: '+r.text)
#print('\033[0m')
#
##UNDER CONST...
