#!/usr/bin/python

from Adafruit_Thermal import *
import random

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

flattery = [
    "You are beautiful",
    "You're a gift to those around you",
    "You're a smart cookie",
    "You are awesome!",
    "I like your style.",
    "On a scale from 1 to 10, you're an 11.",
    "You should be proud of yourself",
    "You're all that and a super-size bag of chips",
    "Being around you makes everything better!",
    "You're one of a kind!"
]
# compliment = random.choice(flattery)
compliment = "The quick brown fox jumped over the laxy dog"


printer.setSize('M')
printer.setLineHeight(50)
printer.print('{:<32}'.format(compliment))
printer.setSize('L')
printer.feed(1)
printer.justify('C')
printer.println("WNDR")
printer.feed(3)
