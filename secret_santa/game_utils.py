import random


def generate_pairs(participants):
    if len(participants) < 2:
        return None

    givers = participants.copy()
    random.shuffle(givers)

    receivers = givers[1:] + [givers[0]]  # moving 1 pos right

    pairs = {
        giver: receiver for giver, receiver in zip(givers, receivers)
    }  # giver -reciever dict

    return pairs
