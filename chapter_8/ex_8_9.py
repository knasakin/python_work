# 8.9. Сообщения
def show_messages(messages_list: list):
    for msg in messages_list:
        print(msg)


messages = ['1..', '2..', '3..']
sent_messages = []

show_messages(messages_list=messages)
