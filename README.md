### Pubmed_large
=======

### Pipeline for converting .xml to .sqlite of Pubmed (NLM licensed)

![my image](fig2.002.jpg)

### To convert .xml to .sqlite

At first, you have to get the licence of NLM. Fill the form of agreement in http://www.nlm.nih.gov/databases/license/license.html You can get "zip" file of Pubmed from NLM.

Second, put this file in Put_Data_Here directory and decompress them.

Finally, run this shell script (it costs several weeks). 

    ./pubmed_large.sh

This script parses the xml and you can get pubmed.sqlite.