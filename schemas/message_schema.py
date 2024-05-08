def message_schema(msg) -> str:
    print(msg)
    return str(msg["content"])


def messages_schema(messages) -> list:
    return [message_schema(message) for message in messages]

def convert_dict(messages):
    cleaner = CleanerMlUtil()
    # for i in range(0, len(messages)-1, 1):
    # print(messages[i].content, jsonable_encoder(messages[i+1]))
    # msg = jsonable_encoder(messages[i+1])
    # print(str(msg["content"]))
    res_dct = {cleaner.clean_words(messages[i].content): messages[i + 1].content for i in range(0, len(messages)-1, 1)}
    return res_dct