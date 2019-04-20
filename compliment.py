#!/usr/bin/python
# coding: utf-8

from __future__ import print_function
from Adafruit_Thermal import *
import random

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

flattery = [
    "You're someone's reason to \n smile",
    "You are making moves and it \n SHOWS.",
    "That color is perfect on you.",
    "Jokes are funnier when you tell \n them.",
    "You're more fun than bubble wrap",
    "Your talent is next level.",
    "Your perspective on the world \n is refreshing.",
    "It's a known fact that you're \n gonna go far.",
    "You take on challenges like you \n were born for it.",
    "You know you're slaying, right?",
    "It's so cool to watch you be \n in your element.",
    "Everything is brighter when \n you're in a room.",
    "People spend years trying to \n get what you've got.",
    "In the middle of chaos, you \n are an ocean of calm.",
    "You're great now and you've \n probably been great since \n forever.",
    "Actions speak louder than words,\n and yours tell an incredible \n story.",
    "You've got a lot of people \n that look up to you.",
    "If you were a box of crayons,\n you'd be the giant name-brand \n one with the built-in sharpener.",
    "You're more helpful than you \n realize.",
    "There's nothing more powerful \n than your presence in a room.",
    "Your imagination is like an \n infinity room.",
    "You are the most perfect you \n there is.",
    "You really know exactly who you \n are.",
    "You are the person equivalent \n of that new-book smell.",
    "Even if you were cloned, you'd \n still be one-of-a-kind. \n And the cooler one.",
    "No one could take what you've \n got away from you.",
    "People love just being around \n you. How could they not?",
    "You've got the biggest heart \n this world has ever seen.",
    "All obstacles are opportunities to you.",
    "It's almost unbelievable to \n think of what you've already \n accomplished in life."
]
compliment = random.choice(flattery)

printer.setSize('M')
printer.setLineHeight(50)
printer.print('{:^32}'.format(compliment))
printer.setSize('L')
printer.feed(1)
printer.justify('C')
printer.println("WNDR")
printer.feed(3)
