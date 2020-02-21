import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-endec", "--endec", type=str, help="encode or decode", default="decode")
parser.add_argument("-input", "--input", type=str, help="User input", default = "odoo gogs   odoo\ngogs gogs gogs")

og_dict = {'a':"odoo gogs", 'b':"gogs odoo odoo odoo", 'c':"gogs odoo gogs odoo", 'd':"gogs odoo odoo", 'e':"odoo", 'f':"odoo odoo gogs odoo", 'g': "goggs goggs odoo", 'h': "odoo odoo odoo odoo", 'i': "odoo odoo", 'j': "odoo gogs gogs gogs", 'k':"gogs odoo gogs", 'l':"odoo gogs odoo odoo", 'm':"gogs gogs", 'n':"gogs odoo", 'o':"gogs gogs gogs", 'p':"odoo gogs gogs odoo", 'q':"gogs gogs odoo gogs", 'r':"odoo gogs odoo", 's':"odoo odoo odoo", 't':"gogs", 'u':"odoo odoo gogs", 'v':"odoo odoo odoo gogs", 'w':"odoo gogs gogs", 'x':"gogs odoo odoo gogs", 'y':"gogs odoo gogs gogs", 'z':"gogs gogs odoo odoo"}

args = parser.parse_args()


if args.endec == 'encode':
	message = ''
	for letter in args.input:
		if letter != " ":
			message += og_dict[letter] + "   "
		else:
			message += "\n"
	print(message)
elif args.endec == 'decode':
	message = ""
	for x in args.input.split("\n"):
		for i in x.split("   "):
			message += list(og_dict.keys())[list(og_dict.values()).index(i)]
		message += "\n"
	print(message)
