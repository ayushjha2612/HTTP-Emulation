import socket

cacheIP = "10.0.1.2"
serverIP = "10.0.1.3"
key_val = {}
def parse_msg(msg): 

   #GET /assignment1?request=key1 HTTP/1.1\r\n\r\n\r\n
  if (msg.find('GET')!= -1):
      ind1= msg.find('=', 0)
      ind2= msg.find(' HTTP/1.1', ind1+1)
      key= msg[ind1+1: ind2]
      if(key_val.get(key)):
        val= key_val[key]
        return ("GET", val)
      else:
        return (key, "NOT_FOUND")
     
  else:
      return ("BAD", "FAILURE")

def store_key(msg, key):
    ind1 = msg.find('\r',0)
    ind2 = msg.find('\n', ind1+2)
    val= msg[ind2+1:]
    key_val[key]= val

s1 = socket.socket()
#print ("Socket successfully created")

dport = 12346
port2 = 12347

s1.bind((cacheIP, port2))
print ("Cache socket binded to %s" %(dport))

s1.listen(5)
print('Cache is listening')
s2= socket.socket()
s2.connect((serverIP, dport))

while True:
  c, addr = s1.accept()
  print ('Cache got connection from', addr )

  while True: 
    recvmsg = c.recv(1024).decode()
    if recvmsg == "":
      break

    action, status = parse_msg(recvmsg)
 
    if action == "GET":
      msg = "HTTP/1.1 200 OK \r\n\r\n"+ status+"\n(Cached Response)"
      c.send(msg.encode())

    elif status == "NOT_FOUND":
      s2.send(recvmsg.encode())
      respmsg = s2.recv(1024).decode()
      c.send(respmsg.encode())
      store_key(respmsg, action)


    else: 
      s2.send(recvmsg.encode())
      respmsg = s2.recv(1024).decode()
      c.send(respmsg.encode())
    

  #
  s2.close()
  c.close()


    
