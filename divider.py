#!/usr/bin/python

import sys, getopt, math

def main(argv):
	inputFile = None
	outputDir = None
	c = 0
	helpText = 'divider.py -i <inputfile> -o <outputdir> -c <countofparts>'
	try:
		opts, args = getopt.getopt(argv, "hi:o:c:", ["ifile=", "ofile=", "cnumber="])
	except getopt.GetoptError:
		print helpText
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print helpText
			sys.exit(2)
		elif opt in ("-i", "--ifile"):
			inputFile = arg
		elif opt in ("-o", "--ofile"):
			outputDir = arg
		elif opt in ("-c", "--cnumber"):
			c = arg
	if inputFile and outputDir and c > 0:
		divider(inputFile, outputDir, c)
	else:
		print helpText

def divider(inputFile, output, c):
	for iter in range(int(c)):
		file = open(inputFile, 'r')
		lineCount =  sum(1 for line in file)
		currentMin = (lineCount / float(c)) * iter
		currentMax = (lineCount / float(c)) * (iter + 1)
		file.close()
		file = open(inputFile, 'r')
		newFileName = output + str(iter + 1) + '.txt'
		print newFileName + " > " + str(int(currentMin)) + ":" + str(int(currentMax))
		newFile = open(newFileName, 'w')
		for lineNumber, line in enumerate(file.readlines()):
			if (lineNumber >= math.ceil(currentMin) and lineNumber < math.ceil(currentMax)):
				newFile.write(line)
		newFile.close()
		file.close()

if __name__ == '__main__':
	main(sys.argv[1:])
