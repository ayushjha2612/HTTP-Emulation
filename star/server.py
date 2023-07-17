import socket

serverIP = "10.0.1.3"
key_val = {}

def parse_msg(msg): 
   #PUT /assignment1/key1/val1 HTTP/1.1\r\n\r\n\r\n
  if (msg.find('PUT')!= -1):
      ind1= msg.find('/', 0)
      ind2= msg.find('/', ind1+1)
      ind1= msg.find('/', ind2+1)
      key = msg[ind2+1: ind1]
      ind2= msg.find(' HTTP/1.1', ind1+1)
      val = msg[ind1+1: ind2]  
      if(key_val.get(key)):
          key_val[key]= val
          return ("PUT", "OVERWRITE")
      else:
          key_val[key]= val
          return ("PUT", "NEW")

   #GET /assignment1?request=key1 HTTP/1.1\r\n\r\n\r\n
  elif (msg.find('GET')!= -1):
      ind1= msg.find('=', 0)
      ind2= msg.find(' HTTP/1.1', ind1+1)
      key= msg[ind1+1: ind2]
      if(key_val.get(key)):
        val= key_val[key]
        return ("GET", val)
      else:
        return ("GET", "404")
  else:
       return ("BAD", "FAILURE")

dst_ip = serverIP

s = socket.socket()
print ("Socket successfully created")

dport = 12346

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("Server is listening")

while True:
  c, addr = s.accept()
  print ('Server got connection from', addr )


  while True: 
    recvmsg = c.recv(1024).decode()
    if recvmsg == "":
      break
    action, status = parse_msg(recvmsg)
    if action == "PUT":
      if status== "NEW" : 
        c.send(b"HTTP/1.1 201 Created \r\n\r\n")
      elif status == "OVERWRITE" :
        c.send(b"HTTP/1.1 204 No Content \r\n\r\n")

    elif action == "GET":
      if status== "404":
        c.send(b"HTTP/1.1 404 Not Found \r\n\r\n")
      else:
        msg = "HTTP/1.1 200 OK \r\n\r\n"+ status
        c.send(msg.encode())
    elif action == "DELETE":
      c.send(b"HTTP/1.1 204 No Content \r\n\r\n")
    else: 
      c.send(b"HTTP/1.1 400 Bad Request \r\n\r\n")
    

  c.close()
  #break
