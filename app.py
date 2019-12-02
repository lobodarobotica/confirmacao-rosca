import paho.mqtt.client as paho
import uuid
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)


def send_confirmacao(action): ## action == 1 => ligado;    action == 0 => desligado;
	client = paho.Client("client-"+str(uuid.uuid1()))
	client.connect("mqtt.positiva.app", 1883)
	message_to_send = {
		"timestamp": int(time.time()),
		"action": action
	}
	client.publish("confirmacao", str(message_to_send))

last_action = 0
while True:
	if(GPIO.input(29) == 1 and last_action == 0):
		print("DESLIGADO")
		send_confirmacao(1)
		last_action = 1
	elif(GPIO.input(29) == 0 and last_action == 1):
		print("LIGADO")
		send_confirmacao(0)
		last_action = 0

	time.sleep(1)

gpio.cleanup()
exit()
