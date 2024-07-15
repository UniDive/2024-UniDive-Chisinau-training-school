import sys
import argparse

cmd = argparse.ArgumentParser()
cmd.add_argument("--input", type=str, required=True)
cmd.add_argument("--feats", action="store_true")
args = cmd.parse_args()

with open(args.input, "r") as f:
	heading = True
	id = 0
	print ("# global.columns = ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC")
	for line in f:
		l = line.strip()
		if heading:
			if l == "":
				heading = False
		else:
			if l == "" or l.startswith("#"):
				id = 0
				print (l)
			else:
				fields = l.split("\t")
				form = fields[0] if 0 < len(fields) else "_"
				gloss = fields[1] if 1 < len(fields) and fields[1] != "" else "_"
				upos = fields[2] if 2 < len(fields) else "_"
				if args.feats:
					feats = fields[3] if 3 < len(fields) else "_"
				else:
					comment = f"|Comment={fields[3]}" if 3 < len(fields)  and fields[3] != "" else ""
				id += 1
				if args.feats:
					print (f"{id}\t{form}\t_\t{upos}\t_\t{feats}\t_\t_\t_\tGloss={gloss}")
				else:
					print (f"{id}\t{form}\t_\t{upos}\t_\t_\t_\t_\t_\tGloss={gloss}{comment}")
	print ()