# lightweighttagger
Python script to recommend tags, given a text input

## Requirements
nltk==3.4.5
textblob==0.15.3

## Usage
This script is built on nltk and textplob and should be invoked using python3. To install nltk and textblob:

pip3 install nltk


pip3 install textblob

To then invoke the script, call it from where it's installed (/Users/shared/tagger in the below example) and provide a --file option with the path and a --tags option to define how many tags to respond with, as follows:


python3 /Users/shared/tagger/tagger.py --file='/Users/ce/Downloads/tagger/test.txt' --tags=5


The response will be the number of tags, delimited with a end of line. 


## Future work
If you were to put this into production, I'd add a model json file that could then be used to further train it. This is really just using the natural language toolkit to isolate top meaninful words but looking at each industry something like this could be used in, there are lots of sets that can obtained in an automated fashion using nltk or other sources and then trained to make the output more specific for the intended use case. 
