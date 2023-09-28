# https://github.com/ilkerkesen/tornado-websocket-client-example
# https://www.georgeho.org/tornado-websockets/
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect
import time
import datetime
import os, sys
sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')
import pepper_cmd
from pepper_cmd import *

class Client(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
        PeriodicCallback(self.keep_alive, 20000).start()
        self.ioloop.start()

    @gen.coroutine
    def connect(self):
        print "trying to connect"
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception, e:
            print "connection error"
        else:
            print "connected"
            self.run()

    @gen.coroutine
    def run(self):
        while True:
            data = yield self.ws.read_message()
            received = data.split("_");
            if(received[0]=="RuleViolation"):
                print("%s!!RuleViolation!!%s" %(RED,RESET))
                pepper_cmd.robot.say('You violated the game rules. Try again.')
            elif(received[0]=="EmptyRod"):
                print("%s!!EmptyRod!!%s" %(RED,RESET))
                pepper_cmd.robot.say('You chose an empty rod. Try again.')        
            elif(received[0]=="ActionDone"):
                print("%s!!ActionDone!!%s" %(GREEN,RESET))
                pepper_cmd.robot.say('Now it\'s your turn.')
            elif(received[0]=="Victory"):
                print("%s!!Victory!!%s" %(GREEN,RESET))
                pepper_cmd.robot.say('Victory')
                victoryDance();
            elif(received[0]=="moveToLeft"):
                doMoveToLeft()
            elif(received[0]=="moveToRight"):
                doMoveToRight()
            else:
                print("%s!!uNKNOWN ERROR!!%s" %(RED,RESET))

    def keep_alive(self):
        if self.ws is None:
            self.connect()
        #else:
            #self.ws.write_message("keep alive")
            
def victoryDance():
	ourSession = pepper_cmd.robot.session_service("ALMotion")
	jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RWristYaw", "RHand", "HipRoll", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LWristYaw", "LHand"]
	jointValues = [-0.141, -0.46, 0.892, -0.8, 0.98, -0.07, -0.07, -0.141, 0.46, -0.892, 0.8, -0.98]
	times  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
	isAbsolute = True
	ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)
	
	for i in range(2):
		jointNames = ["RElbowYaw", "LElbowYaw", "HipRoll", "HeadPitch"]
		jointValues = [2.7, -1.3, -0.07, -0.07]
		times  = [0.8, 0.8, 0.8, 0.8]
		isAbsolute = True
		ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

		jointNames = ["RElbowYaw", "LElbowYaw", "HipRoll", "HeadPitch"]
		jointValues = [1.3, -2.7, -0.07, -0.07]
		times  = [0.8, 0.8, 0.8, 0.8]
		isAbsolute = True
		ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)
	
	
	
def doHello():
	ourSession = pepper_cmd.robot.session_service("ALMotion")

	jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RWristYaw", "RHand", "HipRoll", "HeadPitch"]
	jointValues = [-0.141, -0.46, 0.892, -0.8, 0.98, -0.07, -0.07]
	times  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
	isAbsolute = True
	ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

	for i in range(2):
		jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
		jointValues = [1.7, -0.07, -0.07]
		times  = [0.8, 0.8, 0.8]
		isAbsolute = True
		ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

		jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
		jointValues = [1.3, -0.07, -0.07]
		times  = [0.8, 0.8, 0.8]
		isAbsolute = True
		ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

	return
	    
def raiseMyArm(whatArm, ourSession):
	if(whatArm=="R"):
	    jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RWristYaw", "RHand", "HipRoll", "HeadPitch"]
	    jointValues = [-0.141, -0.46, 0.892, -0.8, 0.98, -0.07, -0.07]
	else:
	    jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LWristYaw", "LHand", "HipRoll", "HeadPitch"]
	    jointValues = [-0.141, 0.46, -0.892, 0.8, -0.98, -0.07, -0.07]
	times  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
	isAbsolute = True
	ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)
	return
	

def doHello():
	ourSession = pepper_cmd.robot.session_service("ALMotion")

	raiseMyArm("R", ourSession)

	for i in range(2):
		jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
		jointValues = [1.7, -0.07, -0.07]
		times  = [0.8, 0.8, 0.8]
		isAbsolute = True
		ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

		jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
		jointValues = [1.3, -0.07, -0.07]
		times  = [0.8, 0.8, 0.8]
		isAbsolute = True
		ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

	return
	    

def doMoveToRight():
	ourSession = pepper_cmd.robot.session_service("ALMotion")

	raiseMyArm("R", ourSession)

	jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
	jointValues = [0.4, -0.07, -0.07]
	times  = [0.8, 0.8, 0.8]
	isAbsolute = True
	ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

		
def doMoveToLeft():
	ourSession = pepper_cmd.robot.session_service("ALMotion")

	raiseMyArm("L", ourSession)

	jointNames = ["LElbowYaw", "HipRoll", "HeadPitch"]
	jointValues = [-0.3, -0.07, -0.07]
	times  = [0.8, 0.8, 0.8]
	isAbsolute = True
	ourSession.angleInterpolation(jointNames, jointValues, times, isAbsolute)

	return


if __name__ == "__main__":
    begin()
        
    # Sonar Activation
    pepper_cmd.robot.startSensorMonitor()
    
    stop_flag = True
    try:
		while stop_flag:
			p = pepper_cmd.robot.sensorvalue()
			if(p[1]!=None and p[1]<3):
				print("I have located the user")
				stop_flag=False
			else:
				if p[1]==None or p[1]=="None":
				    print("I don't locate any users near me")
				else:
					print("I have located the user, but it is not close enough")
				#I stop 3 seconds before checking for another person
				time.sleep(3)
    except KeyboardInterrupt:
        pass 
    
    # Sonar Deactivation
    pepper_cmd.robot.stopSensorMonitor()
    
    if(stop_flag):
		print("\n\nDetected KeyboardInterrupt. Exit\n")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
			
	
    pepper_cmd.robot.white_eyes()
	
    Our_tts_service = pepper_cmd.robot.session_service("ALTextToSpeech")
    Our_tts_service.setLanguage("English")
    Our_tts_service.setVolume(1.0)
    Our_tts_service.setParameter("speed", 1.0)

    Our_tts_service.say("Hello! Do you want to play with me?"+" "*4, _async=True)
    doHello()


    pepper_cmd.robot.showurl("http://192.168.1.20:5500/WebApp/main.html")

    
    IPAddr="127.0.0.1:9030"
    client = Client("ws://"+IPAddr+"/websocketserver", 5)

#python write.py --key Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value --val 2
