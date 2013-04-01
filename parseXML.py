#!/usr/bin/python
# -*- coding: utf_8 -*-

import os
from lxml import etree, objectify
import sys
import codecs
import re

# XML file name
#xml_file = os.getcwd() + "/" + sys.argv[1]
xml_file = sys.argv[1]
#print xml_file

# open output file
out1 = open('pubmed.txt', 'a')
out2 = open('pmc.txt', 'a')
out3 = open('mesh.txt', 'a')

# parse XML
tree = objectify.parse(xml_file, parser = etree.XMLParser())
root = tree.getroot()

for i in range(len(root)):
#	print str(i + 1) + " / " + str(len(root))
	try:

		# Journal
		Journal = root[i].xpath("Article")[0].xpath("Journal")[0].xpath("Title")[0].text
		# Year
		Year = root[i].xpath("Article")[0].xpath("Journal")[0].xpath("JournalIssue")[0].xpath("PubDate")[0].xpath("Year")[0].text
		# Title
		Title = root[i].xpath("Article")[0].xpath("ArticleTitle")[0].text
		# Abstruct
		Abstruct = root[i].xpath("Article")[0].xpath("Abstract")[0].xpath("AbstractText")[0].text
		# PMID / 6. Pumbed URL
		PMID = root[i].xpath("PMID")[0].text
		PM_URL = "http://www.ncbi.nlm.nih.gov/pubmed/" + PMID

		# output
		out1.write(PMID.encode("utf_8"))
		out1.write("\t")
		out1.write(Journal.encode("utf_8"))
		out1.write("\t")
		out1.write(Year.encode("utf_8"))
		out1.write("\t")
		out1.write(Title.encode("utf_8"))
		out1.write("\t")
		out1.write(Abstruct.encode("utf_8"))
		out1.write("\t")
		out1.write(PM_URL.encode("utf_8"))
		out1.write("\n")

	except IndexError:
		pass
		
	#  PMCID / PMCURL
	try:
		match = re.match("PMC\d+", root[i].xpath("OtherID")[0].text)
		if match:
			PMID = root[i].xpath("PMID")[0].text
			PMCID = match.group()
			PMC_URL = "http://www.ncbi.nlm.nih.gov/pmc/articles/" + PMCID + "/pdf/"

			# output
			out2.write(PMID.encode("utf_8"))
			out2.write("\t")
			out2.write(PMCID.encode("utf_8"))
			out2.write("\t")
			out2.write(PMC_URL.encode("utf_8"))
			out2.write("\n")

	except IndexError:
		pass

	#  MeSH Category / MeSH Term
	try:
		
		for j in range(len(root[i].xpath("MeshHeadingList")[0].xpath("MeshHeading"))):
			PMID = root[i].xpath("PMID")[0].text
			MeSH_Term = root[i].xpath("MeshHeadingList")[0].xpath("MeshHeading")[j].xpath("DescriptorName")[0].text

			# output
			out3.write(PMID.encode("utf_8"))
			out3.write("\t")
			out3.write(MeSH_Term.encode("utf_8"))
			out3.write("\n")
	except IndexError:
		pass

# close
out1.close()
out2.close()
out3.close()
