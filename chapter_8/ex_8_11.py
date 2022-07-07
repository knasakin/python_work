# 8.11. Архивированные сообщения
def send_messages(messages_list: list, completed_sents: list):
    for msg in messages_list:
        completed_sents.append(msg)


messages = ['1..', '2..', '3..']
sent_messages = []

send_messages(messages_list=messages, completed_sents=sent_messages)
print(messages, sent_messages, sep='\n')
