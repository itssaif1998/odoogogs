import argparse

from og_dict import og_dict

parser = argparse.ArgumentParser()

parser.add_argument("-endec", "--endec", type=str, help="encode or decode", default="decode")
parser.add_argument("-path", "--path", type=str, help="File path", default="")
parser.add_argument("-input", "--input", type=str, help="User input", default = "odoo gogs   odoo\ngogs gogs gogs")
parser.add_argument("-output", "--output", type=str, help="Define output: console or path", default = "console")

args = parser.parse_args()

if args.path != "":
	file = open(args.path, "r")
	input_txt = file.read().lower()
	file.close()
else:
	input_txt = args.input.lower()

if args.endec == 'encode':
	message = ''
	for letter in input_txt:
		if letter != " ":
			message += og_dict[letter] + "   "
		else:
			message += "\n"
elif args.endec == 'decode':
	message = ""
	for x in input_txt.split("\n"):
		for i in x.split("   "):
			message += list(og_dict.keys())[list(og_dict.values()).index(i)]
		message += "\n"

if args.output == "console":
	print(message)
else:
	file = open(args.output, "w")
	file.write(message)
	file.close()
