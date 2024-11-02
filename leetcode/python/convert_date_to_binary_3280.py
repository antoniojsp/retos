class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_str = date.split("-")
        date_int = list(map(lambda x: int(x), date_str))
        return f"{bin(date_int[0])[2:]}-{bin(date_int[1])[2:]}-{bin(date_int[2])[2:]}"
