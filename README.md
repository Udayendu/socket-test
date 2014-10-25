socket-test
===========

This is a socket program for testing. To test this script:

1. Run the server script as below in the terminal:

    $ python server.py  &

2. Then run the client script:

    $ python client.py

Then the __OUT_PUT__ should be like:

$ python client.py 
{'cod': '01', 'type': 'info', 'status': 'up', 'svc': 'httpd'}
{'cod': '00', 'status': True}
Cool!

$ ls -l /tmp/svc_httpd.log 
-rw-r--r--. 1 root root 30 Oct 25 18:03 svc_httpd.log

$ cat /tmp/svc_httpd.log 
COD: 01
TYPE: info
STATUS: up
