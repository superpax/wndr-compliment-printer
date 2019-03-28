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


printer.setSize('M')
printer.println(random.choice(flattery))
printer.setSize('L')
printer.justify('C')
printer.println("WNDR Museum")

