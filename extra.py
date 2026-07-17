import os
import sys



ascii = Ascii_Class()
colors = Colors_Class()



class Ascii_Class():
	def __init__(self):
		self.CATGIRL = """
　　　 　,,
,＿, -ｰ'"{
゛ヌ ﾉﾉﾉﾊヾ
ﾉ li .ﾟ ヮﾟﾉi
彡と}   .{つ
"""
		self.CAT = """

 ╱|、
(˚ˎ。7  
|、˜ 〵          
じ しˍ,)ノ
"""

class Colors_Class():
	def __init__(self):
		self.RED = "\033[31m"
		self.GREEN = "\033[32m"
		self.YELLOW = "\033[0;33m"
		self.BLUE = "\033[34m"
		self.PINK = "\u001b[38;5;212m"
		self.PURPLE = "\033[0;35m"
		self.WHITE = "\033[0;37m"
		self.CYAN = "\033[0;36m"

		self.RESET = "\033[0m"
		self.R = "\033[0m"


