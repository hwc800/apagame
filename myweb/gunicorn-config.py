from multiprocessing import cpu_count

bind = ["9.135.94.3:8080"]  # 注意：上线的项目需要使用 服务器 内网的 ip 地址
daemon = True  # 是否开启守护进程模式
pidfile = 'logs/gunicorn.pid'

workers = cpu_count() * 2  # 工作进程数量
worker_class = "gevent"  # 指定一个异步处理的库
worker_connections = 65535

keepalive = 60  # 服务器保持连接的时间，能够避免频繁的三次握手过程
timeout = 30
graceful_timeout = 10
forwarded_allow_ips = '*'

# 日志处理
capture_output = True
loglevel = 'info'
errorlog = 'logs/gunicorn-error.log'
# 启动命令 gunicorn -c ./myweb/gunicorn-config.py myweb.wsgi
# 启动后，项目根路径下会生成一个logs目录，里面有gunicorn-error.log记录日志，gunicorn.pid记录进程id
# 重启服务kill -HUP id
# 关闭服务kill -9 id
