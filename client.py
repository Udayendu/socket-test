#!/usr/bin/python

import socket                                                                      
import json                                                                        
                                                                                   
s = socket.socket()                                                                
host = socket.gethostname()                                                        
port = 12346                                                                       
                                                                                   
def _send_data(data):                                                              
    s.connect((host, port))                                                        
    s.sendall(json.dumps(data).encode('utf-8'))                                    
    reply = json.loads(s.recv(4096).decode('utf-8'))                               
    s.close()                                                                      
    return reply                                                                   
                                                                                   
                                                                                   
def _test_svc(svc):                                                                
    msg = {}                                                                       
                                                                                   
    if svc == 'httpd':                                                             
        # test httpd service here                                                  
        #                                                                          
                                                                                   
        # creating the message to the server                                       
        # you better have the protocol specification first                         
        msg['cod'] = '01'                                                          
        msg['type'] = 'info'                                                       
        msg['svc'] = svc                                                           
        msg['status'] = 'up'                                                       
                                                                                   
        reply = _send_data(msg)                                                    
        print(reply)                                                               
                                                                                   
        if reply['status']:                                                        
            print('Cool!')                                                         
                                                                                   
    if svc == 'other_svc':                                                         
        print("other_svc")                                                         
                                                                                   
                                                                                   
if __name__ == "__main__":                                                         
    _test_svc('httpd')
