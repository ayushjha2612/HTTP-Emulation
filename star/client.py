import socket
import time

def parse_resp(msg):
    ind1 = msg.find('\r',0)
    print("Response: ")
    print(msg[0: ind1])
    if(msg.find('200 OK',0)!= -1):
        ind2 = msg.find('\n', ind1+2)
        print(msg[ind2+1:])

cacheIP = "10.0.1.2"

dst_ip = cacheIP
s = socket.socket()
port = 12347

s.connect((dst_ip, port))


'''
for i in range(3):
	if i == 0 :
		req = "PUT /assignment1/key1/val1 HTTP/1.1\r\n\r\n"
	elif i==1 :
		req = "GET /assignment1?request=key1 HTTP/1.1\r\n\r\n"
	else :
		req = "GET /assignment1?request=key1 HTTP/1.1\r\n\r\n"

	print("Client Request: ")
	print(req)

	start_time = time.time()
	s.send(req.encode())
	respmsg = s.recv(1024).decode()
	print("Time taken :  %s seconds " % (time.time() - start_time))

	parse_resp(respmsg)
'''


# Part b 
for i in range(1,7) :
    req =  "PUT /assignment1/key"+  str(i) + "/val" +  str(i)+ " HTTP/1.1\r\n\r\n"
    print("Client Request: ")
    print(req)

    start_time = time.time()
    s.send(req.encode())
    respmsg = s.recv(1024).decode()
    print("Time taken :  %s seconds " % (time.time() - start_time))

    parse_resp(respmsg)

for j in range(3): 
  for i in range(1,7) :
    req = "GET /assignment1?request=key"+ str(i) + " HTTP/1.1\r\n\r\n"
    print("Client Request: ")
    print(req)

    start_time = time.time()
    s.send(req.encode())
    respmsg = s.recv(1024).decode()
    print("Time taken :  %s seconds " % (time.time() - start_time))

    parse_resp(respmsg)


s.close()

