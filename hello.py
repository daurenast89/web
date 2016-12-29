def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response (status, response_headers)
    raw_uri = str(environ.get('RAW_URI'))
    raw_uri = raw_uri[2:]
    params = raw_uri.split('&')
    data = ''
    for param in params:
        data += param + '\r\n'
    return iter([data])
