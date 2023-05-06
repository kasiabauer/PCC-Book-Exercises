
def show_messages(messages):
    """Wyświetla komunikaty z listy"""
    for message in messages:
        print(message)

msgs = ['Ruch został przekierowany', 'Utrudnienia na trasie',
            'Uwaga silne opady deszczu']
show_messages(msgs)