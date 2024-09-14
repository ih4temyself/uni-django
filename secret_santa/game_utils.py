import random


def generate_pairs(participants):
    if len(participants) < 2:
        return None

    givers = participants.copy()
    receivers = participants.copy()
    random.shuffle(receivers)

    pairs = {}
    for giver in givers:
        for receiver in receivers:
            if giver != receiver and receiver not in pairs.values():
                pairs[giver] = receiver
                receivers.remove(receiver)
                break
    return pairs
