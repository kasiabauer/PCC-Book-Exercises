def send_messages(messages, sent_messages):
    """Wysyła komunikaty z listy"""
    while messages:
        print_message = messages.pop()
        print(print_message)
        sent_messages.append(print_message)


msgs = ['Ruch został przekierowany', 'Utrudnienia na trasie',
        'Uwaga silne opady deszczu']
s_msgs = []
send_messages(msgs, s_msgs)
print(msgs)
print(s_msgs)