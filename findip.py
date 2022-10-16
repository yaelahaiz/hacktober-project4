import request

ip = request.get('https://ipinfo.io/json').json()['ip']

print ('your ip : ', ip)
