#!/usr/bin/python

import socket                                                                      
import json                                                                        
                                                                                   
s = socket.socket()                                                                
host = socket.gethostname()                                                        
port = 12346                                                                       
s.bind((host, port))                                                               
s.listen(5)                                                                        
                                                                                   
def _reply(data):                                                                  
    c.sendall(json.dumps(data).encode('utf-8'))                                    
                                                                                   
while True:                                                                        
    c, addr = s.accept()                                                           
    data = json.loads(c.recv(4096).decode('utf-8'))                                
    print(data)                                                                    
                                                                                   
    if data['svc'] == 'httpd':                                                     
                                                                                   
        reply_data = {}                                                            
        reply_data['cod'] = '00'                                                   
        reply_data['status'] = True                                                
        _reply(reply_data)                                                         
                                                                                   
        f = open('/tmp/svc_httpd.log', 'a')                                        
        f.write('COD: %s\n' % data['cod'])                                         
        f.write('TYPE: %s\n' % data['type'])                                       
        f.write('STATUS: %s\n' % data['status'])                                   
        f.close()
