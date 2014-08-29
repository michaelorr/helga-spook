from helga.plugins import command
import random


@command('spook', aliases=['spook'])
def spook(client, channel, nick, message, cmd, args):
    """
    prints NSA buzzwords
    """
    words = [w.strip() for w in open('spook.lines', 'r').readlines()]
    num = random.randint(6, 15)
    res = random.sample(words, num)
    return u' '.join(res)


print spook()
