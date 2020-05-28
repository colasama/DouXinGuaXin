import pymysql
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
from sshtunnel import SSHTunnelForwarder
import werkzeug
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
app.secret_key = '\xc9ixnRb\xe40\xd4\xa5\x7f\x03\xd0y6\x01\x1f\x96\xeao+\x8a\x9f\xe4'
api = Api(app)
server = SSHTunnelForwarder(
    ssh_address_or_host=('182.92.57.178', 22),  # 指定ssh登录的跳转机的address
    ssh_username='root',  # 跳转机的用户
    ssh_password='Buaa1813Se',  # 跳转机的密码
    remote_bind_address=('127.0.0.1', 3306))
server.start()
db = 'platform'
connection = pymysql.connect(
    user="root",
    passwd="8cn1D89ncac",
    host="127.0.0.1",
    db=db,
    port=server.local_bind_port)
cursor = connection.cursor(pymysql.cursors.DictCursor)


# 资源未找到时调用
def abort_if_doesnt_exist(string):
    abort(404, message=string + " doesn't exist")


def create_token(User_id):
    '''
    生成token
    :param api_user:用户id
    :return: token
    '''

    # 第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    # 第二个参数是有效期(秒)
    s = Serializer(app.config["SECRET_KEY"], expires_in=3600)
    # 接收用户id转换与编码
    token = s.dumps({"id": User_id}).decode("ascii")
    return token


def verify_token(token):
    '''
    校验token
    :param token: 
    :return: 用户信息 or None
    '''

    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(app.config["SECRET_KEY"])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据
    return data["id"]


class register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("phonenum", type=str, required=True)
        parser.add_argument("motto", type=str)
        req = parser.parse_args(strict=True)
        name = req['name']
        password = req['password']
        pwhash = werkzeug.security.generate_password_hash(
            password, method='pbkdf2:sha1', salt_length=8)
        email = req['email']
        phonenum = req['phonenum']
        motto = req['motto']
        cursor.execute(
            "INSERT INTO `User` (User_password,User_name,User_email,User_phonenum,User_authority,User_motto) VALUES ('%s','%s','%s','%s',1,'%s')" %
            (pwhash, name, email, phonenum, motto))
        connection.commit()
        cursor.execute(
            "SELECT User_id FROM User WHERE User_name LIKE '%s'" %
            (name)
        )
        result = cursor.fetchone()
        print(result)
        token = create_token(result['User_id'])
        return {'result': {
                'token': token
                }}


class login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        req = parser.parse_args(strict=True)
        name = req['name']
        password = req['password']
        print(name)
        print(password)
        cursor.execute(
            "SELECT * FROM User WHERE User_name LIKE '%s'" %
            (name)
        )
        result = cursor.fetchone()
        if result == None:
            return {'message': 'Login error, incorrect password or username.'}, 403
        if werkzeug.security.check_password_hash(result['User_password'], password):
            token = create_token(result['User_id'])
            return {'result': {
                'token': token
            }}
        else:
            return {'message': 'Login error, incorrect password or username.'}, 403


class get_user_info(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        token = req['token']
        user_id = verify_token(token)
        if user_id!=None:
            cursor.execute(
            "SELECT User_id,User_name,User_email,User_phonenum,User_authority,User_motto FROM User WHERE User_id LIKE '%s'" %
            (user_id))
            result = cursor.fetchone()
            return{'result':result}
        else:
            return {'message': 'Illegal token.'}, 403

class get_all_movies(Resource):
    def get(self):
        cursor.execute('SELECT * FROM Movies;')
        return {'result': cursor.fetchall()}


class get_movies_by_id(Resource):
    def get(self, movie_id):
        cursor.execute(
            "SELECT * FROM Movies WHERE Movie_id LIKE '%s'" % (movie_id))
        result = cursor.fetchone()
        if result == None:
            abort_if_doesnt_exist("Movie_id")
        cursor.execute(
            "SELECT * FROM Movie_Comments WHERE Movie_id LIKE '%s'" % (movie_id))
        content = cursor.fetchall()
        return {'result': {
            'info': result,
            'comments': content,
        }}


class get_movies_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Movies WHERE Movie_name LIKE '%s' " % (keywords))
        result = cursor.fetchall()
        return {'result': result}


class get_all_books(Resource):
    def get(self):
        cursor.execute('SELECT * FROM Books;')
        return {'result': cursor.fetchall()}


class get_books_by_id(Resource):
    def get(self, book_id):
        cursor.execute(
            "SELECT * FROM Books WHERE Book_id LIKE '%s'" % (book_id))
        result = cursor.fetchone()
        if result == None:
            abort_if_doesnt_exist("Book_id")
        cursor.execute(
            "SELECT * FROM Book_Comments WHERE Book_id LIKE '%s'" % (book_id))
        content = cursor.fetchall()
        return {'result': {
            'info': result,
            'comments': content,
        }}


class get_books_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Books WHERE Book_name LIKE '%s' " % (keywords))
        result = cursor.fetchall()
        return {'result': result}


class get_all_topics(Resource):
    def get(self):
        cursor.execute('SELECT * FROM Topics;')
        return {'result': cursor.fetchall()}


class get_topics_by_id(Resource):
    def get(self, topics_id):
        cursor.execute(
            "SELECT * FROM Topics WHERE Topic_id LIKE '%s'" % (topics_id))
        result = cursor.fetchone()
        if result == None:
            abort_if_doesnt_exist("Topic_id")
        cursor.execute(
            "SELECT * FROM Topic_Contents WHERE Topic_id LIKE '%s'" % (topics_id))
        content = cursor.fetchall()
        return {'result': {
            'info': result,
            'contents': content,
        }}


class get_topics_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Topics WHERE Topic_name LIKE '%s' OR Topic_related LIKE '%s' " % (keywords, keywords))
        result = cursor.fetchall()
        return {'result': result}


# 添加API路由
# 用户
api.add_resource(register, '/register')
api.add_resource(login, '/login')
api.add_resource(get_user_info, '/userinfo')


# 电影
api.add_resource(get_all_movies, '/movies')
api.add_resource(get_movies_by_id, '/movies/<movie_id>')

# 书籍
api.add_resource(get_all_books, '/books')
api.add_resource(get_books_by_id, '/books/<books_id>')

# 话题
api.add_resource(get_all_topics, '/topics')
api.add_resource(get_topics_by_id, '/topics/<topics_id>')

# 检索
api.add_resource(get_movies_by_keywords, '/search/movies')
api.add_resource(get_books_by_keywords, '/search/books')

if __name__ == '__main__':
    app.run(debug=True)
