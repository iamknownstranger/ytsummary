from youtube_transcript_api import YouTubeTranscriptApi
from pytube import extract

def get_transcript(video_url):
    """
    Returns the transcript of the given youtube video url
    """
    video_id = extract.video_id(video_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    corpus = ""
    for element in transcript:
        text = element["text"].replace("\n", " ")
        corpus += text + " "

    return corpus


from transformers import pipeline
summarization = pipeline("summarization")

# using pipeline API for summarization task
def get_summary(corpus):
    """
    Returns the summary of the transcript 
    """
    return summarization(corpus)[0]['summary_text']

