"""



"""

import requests

# get请求
r = requests.get('http://httpbin.org/get')
print(r.status_code, r.reason)
# print(r.text)
print(r.json())
print(r.json().get('headers').get('Host'))
# post请求
r = requests.post('http://httpbin.org/post', data={'a': '1'})
print(r.json())

# 主动抛出状态码异常
bad_r = requests.get('http://httpbin.org/status/200')
print(bad_r.raise_for_status())
#bad_r.raise_for_status()

# 使用requests.Session对象请求
# 创建一个Session对象
s = requests.Session()
# Session 对象会保存服务器返回的set-cokkies头信息里面的内容
s.get('http://httpbin.org/cookies/set/usrid/123456')
s.get('http://httpbin.org/cookies/set/token/xxxxxx')
# 下次请求会将本地所有的cookies信息自动添加到请求头信息里
r = s.get('http://httpbin.org/cookies')
print(r.json())

# 在requests中使用代理

# zip
a = ['a','b','c']
b = [1,2,3]
c = [1,2,3,4]
zip_list = list(zip(a,b))  #  [('a', 1), ('b', 2), ('c', 3)]
zip_list1 = list(zip(a,c))  # [('a', 1), ('b', 2), ('c', 3)]

"""
响应状态码
200 OK - [GET]：服务器成功返回用户请求的数据 
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数 据成功。 
202 Accepted - [*]：表示一个请求已经进入后台排队 （异步任务） 
204 NO CONTENT - [DELETE]：用户删除数据成功。 
3xx 重定向
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发 出的请求有错误，服务器没有进行新建或修改数据的操作，该 操作是幂等的。 
401 Unauthorized - [*]：表示用户没有权限（令牌、用 户名、密码错误）。 
403 Forbidden - [*] 表示用户得到授权（与401错误相 对），但是访问是被禁止的。 
404 NOT FOUND - [*]：用户发出的请求针对的是不存在 的记录，服务器没有进行操作，该操作是幂等的。 
406 Not Acceptable - [GET]：用户请求的格式不可得 （比如用户请求JSON格式，但是只有XML格式）。 
410 Gone -[GET]：用户请求的资源被永久删除，且不会再 得到的。 
422 Unprocesable entity - [POST/PUT/PATCH] 当 创建一个对象时，发生一个验证错误。 
500 INTERNAL SERVER ERROR - [*]：服务器发生错误
"""
"""
flask应用
get请求 可以使用requests.args.get()获取请求参数 
post请求可以使用requests.form.get()获取请求查询参数
falsk的MVC设计思想
1.客户端发起请求后，通过路由找到试图处理函数
2.路由（请求资源）和视图处理函数（controller）事先在app中声明
3.在视图的处理函数中根据业务需求，加载数据（model）并渲染到模板中（view）
4.将渲染之后的模板数据返回给客户端

flask特有的mtv设计思想
MTV设计思想，基于MVC，M-model T- template V-view
"""
