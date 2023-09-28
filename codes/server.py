# http://www.html.it/pag/53419/websocket-server-con-python/
# sudo -H easy_install tornado

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time
import argparse
        #import os, sys
        #sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')
        #import pepper_cmd
        #from pepper_cmd import *
#NON USATO: import qi
from threading import Thread
import HanoiTowersPlanner # OUR PLANNER

#from dummy_robot import begin,end,forward,backward,left,right

#import sys
#sys.path.append('../program')

#NON USATO: import pepper_cmd
#NON USATO: from pepper_cmd import *

# Global variables

websocket_server = None     # websocket handler
websocket_server_2 = None   # websocket handler
run = True                  # main_loop run flag
server_port = 9020          # web server port
server_port_2 = 9030        # web server port
code = None
status = "Idle"             # robot status sent to websocket

session = None
tablet_service = None
webview = "http://198.18.0.1/apps/spqrel/index.html"

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

# Websocket server handler
class MyWebSocketServer(tornado.websocket.WebSocketHandler):

    def open(self):
        global websocket_server, run
        websocket_server = self
        print('New connection with the website\n')
       
    def on_message(self, data):
        global code, status
        received = data.split("_");
        if(received[0]=="RuleViolation"):
            print("%s!!RuleViolation!!%s" %(RED,RESET))
            websocket_server_2.write_message(received[0])
        elif(received[0]=="OK"):
            # ONLY FOR DEBUG: print(received)
            left = []
            center = []
            right = []
            if received[1]!='':
                left = received[1].split(",");
            if received[2]!='':
                center = received[2].split(",");
            if received[3]!='':
                right = received[3].split(",");
            num_disk = len(left)+len(center)+len(right);
            moveToDo = HanoiTowersPlanner.initProblem(num_disk, left, center, right);
            self.write_message(moveToDo)
            print("%sPlan Sent%s" %(GREEN,RESET))
            print()
        elif ...
  
    def on_close(self):
        print('Connection closed\n')
  
    def on_ping(self, data):
        print('ping received: %s' %(data))
  
    def on_pong(self, data):
        print('pong received: %s' %(data))
  
    def check_origin(self, origin):
        #print("-- Request from %s" %(origin))
        return True


class MyWebSocketServer2(tornado.websocket.WebSocketHandler):

    def open(self):
        global websocket_server_2, run
        websocket_server_2 = self
        print('New connection with Pepper\n')
       
    def on_message(self, data):
        global code, status
        '''
        received = data.split("_");
        if(received[0]=="RuleViolation"):
            print("%s!!RuleViolation!!%s" %(RED,RESET))
            pepper_cmd.robot.say('You violated the game rules. Try again.')
        elif(received[0]=="EmptyRod"):
            print("%s!!EmptyRod!!%s" %(RED,RESET))
            pepper_cmd.robot.say('You chose an empty rod. Try again.')
        elif(received[0]=="OK"):
            # ONLY FOR DEBUG: print(received)
            left = []
            center = []
            right = []
            if received[1]!='':
                left = received[1].split(",");
            if received[2]!='':
                center = received[2].split(",");
            if received[3]!='':
                right = received[3].split(",");
            num_disk = len(left)+len(center)+len(right);
            moveToDo = HanoiTowersPlanner.initProblem(num_disk, left, center, right);
            self.write_message(moveToDo)
            print("%sPlan Sent%s" %(GREEN,RESET))
            print()
        elif(received[0]=="ActionDone"):
            print("%s!!ActionDone!!%s" %(GREEN,RESET))
            pepper_cmd.robot.say('Now it\'s your turn.')
        else:
            print("%s!!uNKNOWN ERROR!!%s" %(RED,RESET))
        '''
        print("Received by Pepper: "+data)

  
    def on_close(self):
        print('Connection closed\n')
  
    def on_ping(self, data):
        print('ping received: %s' %(data))
  
    def on_pong(self, data):
        print('pong received: %s' %(data))
  
    def check_origin(self, origin):
        #print("-- Request from %s" %(origin))
        return True
# Main loop (asynchrounous thread)

def main_loop(data):
    global run, websocket_server, status, tablet_service
    while (run):
        time.sleep(1)
        #if (run and not websocket_server is None):
            #try:
                #websocket_server.write_message(status)
                #print(status)
            #except tornado.websocket.WebSocketClosedError:
                #print('Connection closed.')
                #websocket_server = None

    print("Main loop quit.")


           

def run_code(code):
    global status
    if (code is None):
        return
    print("=== Start code run ===")
    #code = beginend(code)
    print("Executing")
    print(code)
    try:
        status = "Executing program"
        exec(code)
    except Exception as e:
        print("CODE EXECUTION ERROR")
        print(e)
    status = "Idle"
    print("=== End code run ===")



# Main program

def main():
    global run
    
    # To find out the external address so as to show it and make the client connect
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IPAddr=s.getsockname()[0]
    print("%sYour Computer IP Address is: %s %s" %(GREEN,IPAddr,RESET))
    print("%sEnter the IP Address in Pepper's browser so that it connects properly to the server%s" %(GREEN,RESET))


    # Run main thread
    t = Thread(target=main_loop, args=(None,))
    t.start()

    # Run robot
    #begin()

    # Run web server for HTML
    application = tornado.web.Application([(r'/websocketserver', MyWebSocketServer),])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(server_port)
    print("%sWebsocket server for HTML listening on port %d%s" %(GREEN,server_port,RESET))
        
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print(" -- Keyboard interrupt --")
    

    if (not websocket_server is None):
        websocket_server.close()
    print("Web server for HTML quit.")
    if (not websocket_server_2 is None):
        websocket_server_2.close()
    print("Web server for Pepper quit.")

    run = False    
    print("Waiting for main loop to quit...")
    
    # Quit
    #end()



if __name__ == "__main__":
    main()

