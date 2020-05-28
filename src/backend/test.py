from requests import put, get,post
post('http://localhost:5000/register', data={'name': 'yzy','password':'yzy123456','email':'123@qq.com','phonenum':'123456789','motto':'balabalabala'}).json()
post('http://localhost:5000/login', data={'name': 'yzy','password':'yzy123456'}).json()
token=post('http://localhost:5000/login', data={'name': 'yzy','password':'yzy123456'}).json()['result']['token']
get('http://localhost:5000/userinfo?token=%s' % token).json()
get('http://localhost:5000/movies/1').json()