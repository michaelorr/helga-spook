import os
import random

from helga.plugins import command


@command('spook', aliases=['spook'])
def spook(client, channel, nick, message, cmd, args):
    """
    prints NSA buzzwords
    """
    filename = 'spook.lines'
    my_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
    words = [w.strip() for w in open(my_file, 'r').readlines()]
    num = random.randint(6, 15)
    res = random.sample(words, num)
    return u' '.join(res)
