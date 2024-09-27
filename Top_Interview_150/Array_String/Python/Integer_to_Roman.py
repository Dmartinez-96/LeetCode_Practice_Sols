class Solution:
    def intToRoman(self, num: int) -> str:
        # reversed because need to start from biggest values and work the way down
        val_to_roman = reversed([
            (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
            (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'),
            (500, 'D'), (900, 'CM'), (1000, 'M') 
        ])
        my_rom_num = ''
        for value, romNum in val_to_roman:
            count = num // value
            if count:
                my_rom_num += romNum * count
                num -= value * count
            if num == 0:
                break
        return my_rom_num
