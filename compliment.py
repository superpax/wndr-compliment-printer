#!/usr/bin/python
# coding: utf-8

from __future__ import print_function
from Adafruit_Thermal import *
import random

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

flattery = [
    "You're someone's reason to smile.",
    "You are making moves and it SHOWS.",
    "That color is perfect on you.",
    "Jokes are funnier when you tell them.",
    "You're more fun than bubble wrap.",
    "Your talent is next level.",
    "Your perspective on the world is refreshing.",
    "It's a known fact that you're gonna go far.",
    "You take on challenges like you were born for it.",
    "You know you're slaying, right?",
    "It's so cool to watch you be in your element.",
    "Everything is brighter when you're in a room.",
    "People spend years trying to get what you've got.",
    "In the middle of chaos, you are an ocean of calm.",
    "You're great now and you've probably been great since forever.",
    "Actions speak louder than words, and yours tell an incredible story.",
    "You've got a lot of people that look up to you.",
    "If you were a box of crayons, you'd be the giant name-brand one with the built-in sharpener.",
    "You're more helpful than you realize.",
    "There's nothing more powerful than your presence in a room.",
    "Your imagination is like an infinity room.",
    "You are the most perfect you there is.",
    "You really know exactly who you are.",
    "You are the person equivalent of that new-book smell.",
    "Even if you were cloned, you'd still be one-of-a-kind. And the cooler one.",
    "No one could take what you've got away from you.",
    "People love just being around you. How could they not?",
    "You've got the biggest heart this world has ever seen.",
    "All obstacles are opportunities to you.",
    "It's almost unbelievable to think of what you've already accomplished in life."
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
