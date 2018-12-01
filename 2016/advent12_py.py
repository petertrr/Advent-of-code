from goto import with_goto

a = 0
b = 0
c = 0
d = 0


@with_goto
def code(a, b, c, d):
	a = 1
	b = 1
	d = 26
	if c != 0:
		goto .label1
	if 1 != 0:
		goto .label2
	label .label1c = 7
	label .label2d += 1
	c -= 1
	if c != 0:
		goto .label3
	label .label1label .label2c = a
	label .label1a += 1
	b -= 1
	if b != 0:
		goto .label4
	b = c
	d -= 1
	if d != 0:
		goto .label5
	c = 16
	label .label2d = 17
	label .label1a += 1
	d -= 1
	if d != 0:
		goto .label6
	c -= 1
	if c != 0:
		goto .label7
	
	print(a, b, c, d)
	return (a, b, c, d)
code(a, b, c, d)