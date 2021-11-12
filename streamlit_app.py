from yt_summary import get_transcript, get_summary
import streamlit as st
 
st.title("Youtube Summarizer")
st.header("This application help you to get the summary of a youtube video")
video_url = st.text_input("Enter youtube video URL: [you can try https://www.youtube.com/watch?v=j70AA9arThc]")
button = st.button("Get Summary")
try:
    if button:
        st.video(video_url)
        transcript_corpus = get_transcript(video_url)
        st.header("Transcript")
        with st.expander("View Transcript"):
            st.write(transcript_corpus)
        summary = get_summary(transcript_corpus)
        st.header("Summary")
        with st.expander("View Summary"):
            st.write(summary)
        st.balloons()
except Exception as e:
    st.warning("Whooops! Could not retrieve a transcript for the video")
    st.exception(e)
    
    
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:"Made with 💓 by Chandra Sekhar Mullu"; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 5px;
                top: 2px;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    

    
