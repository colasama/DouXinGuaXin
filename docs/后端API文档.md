# 豆辛瓜辛后端API文档

## 概述

遵循前后端分离的思想，所以前端Web服务器和后端分开存放，文件目录如下

```
src
├─frontend    # 存放前端文件
├─backend    # 存放python文件
```

1. API遵循RESTful设计，通过域名来决定调用的API种类。
2. 用户身份验证采用token机制，用户登录时通过用户名和密码获取token，之后的身份验证均使用token进行。
3. 返回结果为JSON文件，正确的返回结果均位于`result`，如果出现错误一般会返回`message`。
4. 对于进行添加操作的API，一般规则是添加什么，返回什么。

**目前还处于开发阶段，并未进行部署。**

## 无需token的API

### 用户相关

#### 注册

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000/register`

请求参数

| 参数     | 是否可选 | 类型   | 范围      | 说明     |
| -------- | -------- | ------ | --------- | -------- |
| name     | 否       | string | 1-20      | 用户名   |
| password | 否       | string | 1-20      | 用户密码 |
| email    | 否       | string | 符合email | 邮箱     |
| phonenum | 否       | string | 11        | 手机号   |
| motto    | 是       | string | 11        | 个性签名 |

**返回说明**

返回参数

| 参数  | 是否可选 | 类型   | 说明                          |
| ----- | -------- | ------ | ----------------------------- |
| token | 否       | string | 用于身份认证，有效时间1小时。 |

#### 登录

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000/login`

请求参数

| 参数     | 是否可选 | 类型   | 范围 | 说明     |
| -------- | -------- | ------ | ---- | -------- |
| name     | 否       | string | 1-20 | 用户名   |
| password | 否       | string | 1-20 | 用户密码 |

**返回说明**

返回参数：

登录成功

| 参数  | 类型   | 说明                          |
| ----- | ------ | ----------------------------- |
| token | string | 用于身份认证，有效时间1小时。 |

登录失败

| 参数    | 类型   | 说明                                                 |
| ------- | ------ | ---------------------------------------------------- |
| message | string | 内容为'Login error, incorrect password or username.' |

返回状态码：403

### 电影相关

#### 获取电影列表

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/movies`

**返回说明**

返回参数

返回数据类型为列表，列表内参数表如下

| 参数           | 类型   | 说明                   |
| -------------- | ------ | ---------------------- |
| Movie_id       | int    | 自动分配的id           |
| Movie_name     | string | 电影名                 |
| Movie_intro    | string | 电影介绍               |
| Movie_score    | float  | 电影评分               |
| Movie_director | string | 电影导演               |
| Movie_src      | string | 该电影对应的资源文件夹 |

#### 根据id获取电影

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/movies/[Movie_id]`

**返回说明**

返回参数

| 参数     | 类型 | 说明                             |
| -------- | ---- | -------------------------------- |
| info     | 对象 | 电影信息，具体信息上述列表内参数 |
| comments | 列表 | 该电影对应的评论列表             |

`comments`参数

| 参数                     | 类型   | 说明       |
| ------------------------ | ------ | ---------- |
| Movie_comment_id         | int    | 评论id     |
| Movie_comment_title      | string | 评论标题   |
| Movie_comment_approve    | int    | 评论赞同数 |
| Movie_comment_disapprove | int    | 评论反对数 |
| Movie_comment_content    | string | 评论内容   |
| User_id                  | int    | 评论用户id |
| Movie_id                 | int    | 评论电影id |

### 书籍相关

#### 获取书籍列表

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/books`

**返回说明**

返回参数

返回数据类型为列表，列表内参数表如下

| 参数           | 类型   | 说明                   |
| -------------- | ------ | ---------------------- |
| Book_id        | int    | 自动分配的id           |
| Book_name      | string | 书籍名                 |
| Book_intro     | string | 书籍介绍               |
| Book_score     | float  | 书籍评分               |
| Book_ISBN      | string | 书籍ISBN号             |
| Book_writer    | string | 书籍作者               |
| Book_publisher | string | 出版社                 |
| Book_src       | string | 该书籍对应的资源文件夹 |

#### 根据id获取书籍

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/books/[Book_id]`

**返回说明**

返回参数

| 参数     | 类型 | 说明                             |
| -------- | ---- | -------------------------------- |
| info     | 对象 | 书籍信息，具体信息上述列表内参数 |
| comments | 列表 | 该书籍对应的评论列表             |

`comments`参数

| 参数                    | 类型   | 说明       |
| ----------------------- | ------ | ---------- |
| Book_comment_id         | int    | 评论id     |
| Book_comment_title      | string | 评论标题   |
| Book_comment_approve    | int    | 评论赞同数 |
| Book_comment_disapprove | int    | 评论反对数 |
| Book_comment_content    | string | 评论内容   |
| User_id                 | int    | 评论用户id |
| Book_id                 | int    | 评论书籍id |

### 话题相关

#### 获取话题列表

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/topics`

**返回说明**

返回参数

返回数据类型为列表，列表内参数表如下

| 参数          | 类型   | 说明     |
| ------------- | ------ | -------- |
| Topic_id      | int    | 话题id   |
| Topic_name    | string | 话题名   |
| Topic_related | string | 话题相关 |
| Topic_intro   | string | 话题介绍 |

#### 根据id获取话题

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/topics/[Topic_id]`

**返回说明**

返回参数

| 参数     | 类型 | 说明                             |
| -------- | ---- | -------------------------------- |
| info     | 对象 | 话题信息，具体信息上述列表内参数 |
| contents | 列表 | 该话题对应的内容列表             |

`contents`参数

| 参数                  | 类型   | 说明                         |
| --------------------- | ------ | ---------------------------- |
| Topic_content_id      | int    | 话题内容id                   |
| Topic_content_content | string | 话题内容正文                 |
| Topic_content_image   | string | 话题内容对应的图片资源文件夹 |
| Topic_id              | int    | 该内容所在话题               |
| User_id               | int    | 该内容的发布人id             |

### 小组相关

#### 获取小组列表

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/groups`

**返回说明**

返回参数

返回数据类型为列表，列表内参数表如下

| 参数          | 类型   | 说明         |
| ------------- | ------ | ------------ |
| Group_id      | int    | 小组id       |
| Group_name    | string | 小组名       |
| Group_related | string | 小组相关     |
| Group_intro   | string | 小组介绍     |
| User_id       | int    | 小组管理员id |

#### 根据id获取小组

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/groups/[Group_id]`

**返回说明**

返回参数

| 参数     | 类型 | 说明                             |
| -------- | ---- | -------------------------------- |
| info     | 对象 | 小组信息，具体信息上述列表内参数 |
| contents | 列表 | 该小组对应的帖子列表             |

`contents`参数

| 参数                  | 类型   | 说明                         |
| --------------------- | ------ | ---------------------------- |
| Group_content_id      | int    | 帖子id                       |
| Group_content_content | string | 帖子正文                     |
| Group_content_title   | string | 帖子内容对应的图片资源文件夹 |
| Group_id              | int    | 该帖子所在小组               |
| User_id               | int    | 该帖子的发布人id             |
| Group_content_image   | string | 帖子对应的图片资源文件夹     |

### 检索相关

#### 关键字检索

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/search/[type]?keywords=[关键词]`

type可选：`movies,books,groups,topics,group_content,topic_content`

URL参数：

| 参数     | 是否可选 | 类型   | 范围 | 说明             |
| -------- | -------- | ------ | ---- | ---------------- |
| keywords | 否       | string | 无   | 用于检索的关键词 |

**返回说明**

返回参数

| 参数   | 类型 | 说明                                      |
| ------ | ---- | ----------------------------------------- |
| 无名称 | 列表 | 包含关键词的列表数据，数据类型参照相关API |

## 需要token的API

### 概述

token均通过headers传入，参数名为`token`

**所有返回说明默认token合法，token不合法时有统一的返回内容**

| 参数    | 类型   | 说明                   |
| ------- | ------ | ---------------------- |
| message | string | 内容为'Illegal token.' |

返回状态码：403

### 用户相关

#### 获取用户信息

HTTP方法：`GET`

请求URL：`http://182.92.57.178:5000/users/info`

**返回说明**

| 参数           | 类型   | 说明     |
| -------------- | ------ | -------- |
| User_id        | int    | 用户id   |
| User_name      | string | 用户名   |
| User_email     | string | 用户邮箱 |
| User_phonenum  | string | 手机号   |
| User_authority | int    | 用户权限 |
| User_motto     | string | 个性签名 |

#### 密码修改

HTTP方法：`POSTs`

请求URL：`http://182.92.57.178:5000/users/modify_password`

请求参数

| 参数         | 是否可选 | 类型   | 范围 | 说明   |
| ------------ | -------- | ------ | ---- | ------ |
| old_password | 否       | string | 1-20 | 旧密码 |
| new_password | 否       | string | 1-20 | 新密码 |

**返回说明**

返回参数

修改成功

| 参数    | 具体内容             | 类型   | 说明         |
| ------- | -------------------- | ------ | ------------ |
| message | Modify successfully. | string | 密码更改成功 |

修改失败

| 参数    | 具体内容                   | 类型   | 说明                                        |
| ------- | -------------------------- | ------ | ------------------------------------------- |
| message | The old password is wrong. | string | 旧密码与数据库中存储不符                    |
| message | User does not exist.       | string | 根据token得到的id在数据库中没法找到对应用户 |

返回码：403

### 书籍相关

#### 评论书籍

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000//books/<int:book_id>/comments`

请求参数

| 参数                 | 是否可选 | 类型   | 范围 | 说明                    |
| -------------------- | -------- | ------ | ---- | ----------------------- |
| book_id              | 否       | int    | /    | 从url获取，不用显式传递 |
| book_comment_title   | 否       | string | 1-20 | 评论标题                |
| book_comment_content | 否       | string | 1-20 | 评论内容                |

**返回说明**

返回添加的完整评论信息，具体参见`comments`参数

#### 书籍评分

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000//books/<int:book_id>/scroes`

请求参数

| 参数       | 是否可选 | 类型  | 范围 | 说明                    |
| ---------- | -------- | ----- | ---- | ----------------------- |
| book_id    | 否       | int   | /    | 从url获取，不用显式传递 |
| book_score | 否       | float | 0-10 | 书籍评分                |

**返回说明**

返回参数

| 参数       | 类型  | 说明                   |
| ---------- | ----- | ---------------------- |
| book_score | float | 返回该书籍修改后的评分 |

### 电影相关

#### 评论电影

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000//movies/<int:movie_id>/comments`

请求参数

| 参数                  | 是否可选 | 类型   | 范围 | 说明                    |
| --------------------- | -------- | ------ | ---- | ----------------------- |
| movie_id              | 否       | int    | /    | 从url获取，不用显式传递 |
| movie_comment_title   | 否       | string | 1-20 | 评论标题                |
| movie_comment_content | 否       | string | 1-20 | 评论内容                |

**返回说明**

返回添加的完整评论信息，具体参见`comments`参数

#### 电影评分

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000//movies/<int:movie_id>/scroes`

请求参数

| 参数        | 是否可选 | 类型  | 范围 | 说明                    |
| ----------- | -------- | ----- | ---- | ----------------------- |
| movie_id    | 否       | int   | /    | 从url获取，不用显式传递 |
| movie_score | 否       | float | 0-10 | 电影评分                |

**返回说明**

返回参数

| 参数        | 类型  | 说明                   |
| ----------- | ----- | ---------------------- |
| movie_score | float | 返回该电影修改后的评分 |

### 小组相关

#### 用户参与小组

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000//groups/<int:group_id>/join`

请求参数

| 参数     | 是否可选 | 类型 | 范围 | 说明                    |
| -------- | -------- | ---- | ---- | ----------------------- |
| group_id | 否       | int  | /    | 从url获取，不用显式传递 |

**返回说明**

返回参数

| 参数     | 类型 | 说明         |
| -------- | ---- | ------------ |
| Group_id | int  | 参加的小组id |
| User_id  | int  | 参加的用户id |

失败

| 参数    | 类型   | 说明                                  |
| ------- | ------ | ------------------------------------- |
| message | string | 返回You have joined the group before. |

返回码 403

### 话题相关

#### 用户参与话题

HTTP方法：`POST`

请求URL：`http://182.92.57.178:5000//topics/<int:topic_id>/join`

请求参数

| 参数     | 是否可选 | 类型 | 范围 | 说明                    |
| -------- | -------- | ---- | ---- | ----------------------- |
| topic_id | 否       | int  | /    | 从url获取，不用显式传递 |

**返回说明**

返回参数

| 参数     | 类型 | 说明         |
| -------- | ---- | ------------ |
| Topic_id | int  | 参加的话题id |
| User_id  | int  | 参加的用户id |

成功参与

失败

| 参数    | 类型   | 说明                                  |
| ------- | ------ | ------------------------------------- |
| message | string | 返回You have joined the topic before. |

返回码 403

## 附录

### HTTP状态码

| 状态码 | 状态码英文名称                  | 中文描述                                                     |
| :----- | :------------------------------ | :----------------------------------------------------------- |
| 100    | Continue                        | 继续。客户端应继续其请求                                     |
| 101    | Switching Protocols             | 切换协议。服务器根据客户端的请求切换协议。只能切换到更高级的协议，例如，切换到HTTP的新版本协议 |
|        |                                 |                                                              |
| 200    | OK                              | 请求成功。一般用于GET与POST请求                              |
| 201    | Created                         | 已创建。成功请求并创建了新的资源                             |
| 202    | Accepted                        | 已接受。已经接受请求，但未处理完成                           |
| 203    | Non-Authoritative Information   | 非授权信息。请求成功。但返回的meta信息不在原始的服务器，而是一个副本 |
| 204    | No Content                      | 无内容。服务器成功处理，但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档 |
| 205    | Reset Content                   | 重置内容。服务器处理成功，用户终端（例如：浏览器）应重置文档视图。可通过此返回码清除浏览器的表单域 |
| 206    | Partial Content                 | 部分内容。服务器成功处理了部分GET请求                        |
|        |                                 |                                                              |
| 300    | Multiple Choices                | 多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端（例如：浏览器）选择 |
| 301    | Moved Permanently               | 永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。今后任何新的请求都应使用新的URI代替 |
| 302    | Found                           | 临时移动。与301类似。但资源只是临时被移动。客户端应继续使用原有URI |
| 303    | See Other                       | 查看其它地址。与301类似。使用GET和POST请求查看               |
| 304    | Not Modified                    | 未修改。所请求的资源未修改，服务器返回此状态码时，不会返回任何资源。客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源 |
| 305    | Use Proxy                       | 使用代理。所请求的资源必须通过代理访问                       |
| 306    | Unused                          | 已经被废弃的HTTP状态码                                       |
| 307    | Temporary Redirect              | 临时重定向。与302类似。使用GET请求重定向                     |
|        |                                 |                                                              |
| 400    | Bad Request                     | 客户端请求的语法错误，服务器无法理解                         |
| 401    | Unauthorized                    | 请求要求用户的身份认证                                       |
| 402    | Payment Required                | 保留，将来使用                                               |
| 403    | Forbidden                       | 服务器理解请求客户端的请求，但是拒绝执行此请求               |
| 404    | Not Found                       | 服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面 |
| 405    | Method Not Allowed              | 客户端请求中的方法被禁止                                     |
| 406    | Not Acceptable                  | 服务器无法根据客户端请求的内容特性完成请求                   |
| 407    | Proxy Authentication Required   | 请求要求代理的身份认证，与401类似，但请求者应当使用代理进行授权 |
| 408    | Request Time-out                | 服务器等待客户端发送的请求时间过长，超时                     |
| 409    | Conflict                        | 服务器完成客户端的 PUT 请求时可能返回此代码，服务器处理请求时发生了冲突 |
| 410    | Gone                            | 客户端请求的资源已经不存在。410不同于404，如果资源以前有现在被永久删除了可使用410代码，网站设计人员可通过301代码指定资源的新位置 |
| 411    | Length Required                 | 服务器无法处理客户端发送的不带Content-Length的请求信息       |
| 412    | Precondition Failed             | 客户端请求信息的先决条件错误                                 |
| 413    | Request Entity Too Large        | 由于请求的实体过大，服务器无法处理，因此拒绝请求。为防止客户端的连续请求，服务器可能会关闭连接。如果只是服务器暂时无法处理，则会包含一个Retry-After的响应信息 |
| 414    | Request-URI Too Large           | 请求的URI过长（URI通常为网址），服务器无法处理               |
| 415    | Unsupported Media Type          | 服务器无法处理请求附带的媒体格式                             |
| 416    | Requested range not satisfiable | 客户端请求的范围无效                                         |
| 417    | Expectation Failed              | 服务器无法满足Expect的请求头信息                             |
|        |                                 |                                                              |
| 500    | Internal Server Error           | 服务器内部错误，无法完成请求                                 |
| 501    | Not Implemented                 | 服务器不支持请求的功能，无法完成请求                         |
| 502    | Bad Gateway                     | 作为网关或者代理工作的服务器尝试执行请求时，从远程服务器接收到了一个无效的响应 |
| 503    | Service Unavailable             | 由于超载或系统维护，服务器暂时的无法处理客户端的请求。延时的长度可包含在服务器的Retry-After头信息中 |
| 504    | Gateway Time-out                | 充当网关或代理的服务器，未及时从远端服务器获取请求           |
| 505    | HTTP Version not supported      | 服务器不支持请求的HTTP协议的版本，无法完成处理               |