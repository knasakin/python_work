# # 8.10. Отправка сообщений
def send_messages(messages_list: list, completed_sents: list):
    while messages_list:
        msg = messages_list.pop()
        completed_sents.append(msg)


messages = ['1..', '2..', '3..']
sent_messages = []

send_messages(messages_list=messages, completed_sents=sent_messages)
print(messages)
print(sent_messages)
