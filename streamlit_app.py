from yt_summary import get_transcript, get_summary
import streamlit as st
 
st.title("Youtube Summarizer")
st.header("This application help you to get the summary of a youtube video")
video_url = st.text_input("Enter youtube video URL: [you can try https://www.youtube.com/watch?v=j70AA9arThc]")
button = st.button("Get Summary")

if button:
    try:
        transcript_corpus = get_transcript(video_url)
        st.header("Transcript")
        with st.expander("View Transcript"):
            st.write(transcript_corpus)
        summary = get_summary(transcript_corpus)
        st.header("Summary")
        with st.expander("View Summary"):
            
            st.write(summary)
    except Exception as e:
        st.warning("Whooops! Could not retrieve a transcript for the video")
        st.exception(e)
    
    

    
    

    
