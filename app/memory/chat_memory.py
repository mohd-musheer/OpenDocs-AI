from collections import deque

recent_messages = deque(maxlen=10)


def add_message(role, content):

    recent_messages.append(
        {
            "role": role,
            "content": content
        }
    )


def get_recent():

    return list(recent_messages)