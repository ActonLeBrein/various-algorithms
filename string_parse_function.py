'''
test: or_test ['if' or_test 'else' test] | lambdef
or_test: and_test ('or' and_test)*
and_test: not_test ('and' not_test)*
not_test: 'not' not_test | comparison
comparison: expr (comp_op expr)*
expr: xor_expr ('|' xor_expr)*
xor_expr: and_expr ('^' and_expr)*
and_expr: shift_expr ('&' shift_expr)*
shift_expr: arith_expr (('<<'|'>>') arith_expr)*
arith_expr: term (('+'|'-') term)*
term: factor (('*'|'/'|'%'|'//') factor)*
factor: ('+'|'-'|'~') factor | power
power: atom trailer* ['**' factor]
trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME
'''

def expression(rbp=0):
	global token
	t = token
	token = next()
	left = t.nud()
	while rbp < token.lbp:
		t = token
		token = next()
		left = t.led(left)
	return left

class literal_token:
	def __init__(self, value):
		self.value = int(value)
	def nud(self):
		return self.value

class operator_add_token:
	lbp = 10
	def nud(self):
		return expression(100)
	def led(self, left):
		right = expression(10)
		return left + right

class operator_sub_token:
	lbp = 10
	def nud(self):
		return -expression(100)
	def led(self, left):
		return left - expression(10)

class operator_mul_token:
	lbp = 20
	def led(self, left):
		return left * expression(20)

class operator_div_token:
	lbp = 20
	def led(self, left):
		return left / expression(20)

class operator_pow_token:
	lbp = 30
	def led(self, left):
		return left ** expression(30-1)

class end_token:
	lbp = 0

import re

token_pat = re.compile("\s*(?:(\d+)|(\*\*|.))")

def tokenize(program):
	for number, operator in token_pat.findall(program):
		if number:
			yield literal_token(number)
		elif operator == "+":
			yield operator_add_token()
		elif operator == "-":
			yield operator_sub_token()
		elif operator == "*":
			yield operator_mul_token()
		elif operator == "/":
			yield operator_div_token()
		elif operator == "**":
			yield operator_pow_token()
		else:
			raise SyntaxError("unknown operator")
	yield end_token()

def parse(program):
	global token, next
	next = tokenize(program).next
	token = next()
	return expression()