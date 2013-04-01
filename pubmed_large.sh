#! /bin/sh

# Search all journal
ls Put_Data_Here/zip/*.xml > xml.txt

# Parse XML
while read line
do
txt=${line}
echo $txt
python parseXML.py $txt
done<xml.txt

# Remove duplicated row
#sort -i pubmed.txt | uniq > pre_pubmed.txt
#sort -i pmc.txt | uniq > pre_pmc.txt
#sort -i mesh.txt | uniq > pre_mesh.txt

#cat pre_pubmed.txt > pubmed.txt
#cat pre_pmc.txt > pmc.txt
#cat pre_mesh.txt > mesh.txt

#rm pre_pubmed.txt
#rm pre_pmc.txt
#rm pre_mesh.txt

# Constuct SQLite
#sqlite3 pubmed.sqlite < schema.query