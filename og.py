import argparse

from og_dict import og_dict

parser = argparse.ArgumentParser()

parser.add_argument("-endec", "--endec", type=str, help="encode or decode", default="decode")
parser.add_argument("-input", "--input", type=str, help="User input", default = "odoo gogs   odoo\ngogs gogs gogs")

args = parser.parse_args()

input_txt = args.input.lower()

if args.endec == 'encode':
	message = ''
	for letter in input_txt:
		if letter != " ":
			message += og_dict[letter] + "   "
		else:
			message += "\n"
	print(message)
elif args.endec == 'decode':
	message = ""
	for x in input_txt.split("\n"):
		for i in x.split("   "):
			message += list(og_dict.keys())[list(og_dict.values()).index(i)]
		message += "\n"
	print(message)
