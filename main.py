from youtube_transcript_api import YouTubeTranscriptApi
from pytube import extract, YouTube

def get_transcript(video_url):
    video_id = extract.video_id(video_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    corpus = ""
    for element in transcript:
        text = element["text"].replace("\n", " ")
        corpus += text + " "

    return corpus


def get_metadata(video_url):
    """
    Returns the metadata of the given youtube video url
    """
    # channel_name = extract.channel_name(video_url)
    yt_object = YouTube(video_url)
    author = yt_object.author
    keywords = yt_object.keywords
    length = yt_object.length
    views = yt_object.views
    description = yt_object.description
    return author, keywords, length, views, description


from transformers import pipeline
summarization = pipeline("summarization")

# using pipeline API for summarization task
def get_summary(corpus):
    
    return summarization(corpus, max_length=50)[0]['summary_text']

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import readtime
import textstat
nltk.download('punkt')

def get_summary_analysis(summary):
    """
    Returns a detailed analysis of the summary text generated from the transcript
    """
    read_time = readtime.of_text(summary)
    text_complexity = textstat.flesch_reading_ease(summary)
    tokenized_words = word_tokenize(summary)
    lr = len(set(tokenized_words)) / len(tokenized_words)
    lexical_richness = round(lr,2)
    num_sentences = textstat.sentence_count(summary)
    return  read_time, text_complexity, lexical_richness, num_sentences
    


# import gensim
# from gensim.utils import simple_preprocess
# from gensim.parsing.preprocessing import STOPWORDS
# from nltk.stem import WordNetLemmatizer, SnowballStemmer
# from nltk.stem.porter import *
# import numpy as np

# import pandas as pd
# stemmer = SnowballStemmer("english")

# def lemmatize_stemming(text):
#     return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# # Tokenize and lemmatize
# def preprocess(text):
#     result=[]
#     for token in gensim.utils.simple_preprocess(text) :
#         if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
#             result.append(token)
            
#     return result





# print(bow_corpus)

# LDA mono-core -- fallback code in case LdaMulticore throws an error on your machine
# lda_model = gensim.models.LdaModel(bow_corpus, 
#                                    num_topics = 10, 
#                                    id2word = dictionary,                                    
#                                    passes = 50)




# def get_topics(transcript):
#     preprocessed_transcript = preprocess(transcript)

#     '''
#     Create a dictionary from 'processed_docs' containing the number of times a word appears 
#     in the training set using gensim.corpora.Dictionary and call it 'dictionary'
#     '''
#     dictionary = gensim.corpora.Dictionary([preprocessed_transcript])

#     '''
#     Create the Bag-of-words model for each document i.e for each document we create a dictionary reporting how many
#     words and how many times those words appear. Save this to 'bow_corpus'
#     '''
#     bow_corpus = [dictionary.doc2bow([word]) for word in preprocessed_transcript]

#     # LDA multicore 
#     '''
#     Train your lda model using gensim.models.LdaMulticore and save it to 'lda_model'
#     '''
#     lda_model =  gensim.models.LdaMulticore(bow_corpus, 
#                                     num_topics = 8, 
#                                     id2word = dictionary)
#     return lda_model



if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=0OQAE53uUxA"
    transcript = get_transcript(video_url)
    print(transcript)
    summary = get_summary(transcript)
    print(summary)
    analysis = get_summary_analysis(summary)
    print(analysis)
    metadata = get_metadata(video_url)



