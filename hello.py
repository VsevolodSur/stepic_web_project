def app(environ, start_response):
    data = environ['QUERY_STRING']
    # data = '127.0.0.1/?a=1&a=2&b=3'
    args = data.split('&')
    ret = ''
    for arg in args:
        ret = ret + arg + '\n'
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return [bytes(ret, 'utf-8')]
