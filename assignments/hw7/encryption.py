def encode(input_msg, input_key):
    output = ""
    for i in range(len(input_msg)):
        msg_value = ord(input_msg[i])
        key_value = input_key
        result_code = (msg_value + key_value)
        output = output + chr(result_code)
    return output


def encode_better(input_msg, input_key):
    user_code = input_msg
    user_key = input_key
    output = ""
    for i in range(len(user_code)):
        msg_value = ord(user_code[i]) - 65
        key_value = ord(user_key[i % len(user_key)]) - 65
        result_msg = ((msg_value + key_value) % 58) + 65
        output = output + chr(result_msg)
    return output
