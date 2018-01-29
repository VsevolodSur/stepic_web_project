def app(environ, start_response):
    data = str(environ['QUERY_STRING']).encoding()
    # data = '127.0.0.1/?a=1&a=2&b=3'
    args = data.split('&')
    print(args)
    ret = ''
    for arg in args:
        ret = ret + arg + '\n'
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return iter([ret])
