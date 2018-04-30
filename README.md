# Summarizer with Python and NLTK 

an algorithm to reduce bodies of text but keeping its original meaning, or giving a great insight into the original text.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Requires:
* python2.7 / python 3. 
* nltk 
* nltk stopwords corpora (python -c 'import nltk; nltk.download("stopwords")'). 


### Deployment [steps to build a Summarizer]

* Remove stop words (defined below) for the analysis 
* Create frequency table of words - how many times each word appears in the text 
* Assign score to each sentence depending on the words it contains and the frequency table
* Build summary by adding every sentence above a certain score threshold 


 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
