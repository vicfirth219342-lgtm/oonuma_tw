import http.server, os
os.chdir("/Users/kiyo/Desktop/大沼ヴィラ販売")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=3002, bind="127.0.0.1")
