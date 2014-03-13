#!/usr/env/python

fp = 0
rp = 0

queue = [0] * 10

def add(item):
	global fp
	global rp
	if not fp - rp == "1":
		queue[rp%len(queue)] = item
		rp += 1
		print(queue)
	else:
		print("Queue full!")

def remove():
	global fp
	global rp
	if not rp == fp:
		return queue[fp]
		fp += 1
	else:
		print("Queue empty!")

while True:

	string = input("Add or remove? ")

	if string == "add":
		item = input("Data to add: ")
		add(item)
	elif string == "remove":
		remove()
	else:
		print("Invalid command!")