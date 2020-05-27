from requests import put, get,post
post('http://localhost:5000/register', data={'name': 'yzy','password':'yzy123456','email':'123@qq.com','phonenum':'123456789','motto':'balabalabala'}).json()
post('http://localhost:5000/login', data={'name': 'yzy','password':'yzy123456'}).json()