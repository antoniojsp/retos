from typing import List


def string_split(msg:str)->List[str]:
    return msg.split(" ")


text = "How are you doing today"

print(string_split(text))