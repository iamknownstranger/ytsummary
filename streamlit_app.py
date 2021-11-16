from main import *
import streamlit as st
 
st.title("Youtube Summarizer")
st.header("This application help you to get the summary of a youtube video")
video_url = st.text_input("Enter youtube video URL: [you can try https://www.youtube.com/watch?v=_FdDgJAw-YM]")
button = st.button("Get Summary")
try:
    if button:
        st.header("Video")
        with st.expander("Watch Video"):
            st.markdown('___')
            st.video(video_url)
        st.header("Metadata")
        with st.expander("View Metadata"):
            
            st.markdown('___')
            author, keywords, length, views, description = get_metadata(video_url)
            st.subheader("Author")
            st.write(author)
            st.markdown('___')
            st.subheader("Keywords")
            st.write(keywords)
            st.markdown('___')
            st.subheader("Views")
            st.write(views)
            st.markdown('___')
            st.subheader("Description")
            st.write(description)

        transcript_corpus = get_transcript(video_url)
        st.header("Transcript")
        with st.expander("View Transcript"):
            st.markdown('___')
            st.write(transcript_corpus)
        try:
            summary = get_summary(transcript_corpus)
            st.header("Summary")
            with st.expander("View Summary"):
                st.markdown('___')
                st.write(summary)
        
            st.header("Summary Analysis")
            with st.expander("View Analysis"):
                read_time, text_complexity, lexical_richness, num_sentences = get_summary_analysis(summary)
                st.markdown('___')
                st.subheader('Reading Time')
                st.write(read_time)
                st.markdown('___')
                st.subheader('Text Complexity')
                st.text("values ranges from 0 or negative (hard to read), to 100 or more (easy to read)")
                st.write(text_complexity)
                st.markdown('___')
                st.subheader('Lexical Richness')
                st.text("distinct words over total number of words")
                st.write(lexical_richness)
                st.markdown('___')
                st.subheader('Number of sentences')
                st.write(num_sentences)
            st.balloons()
        except Exception as e:
            st.warning("Ugh ohh! Something went wrong while summarizing the transcript.")
        
except Exception as e:
    st.warning("Whooops! Could not retrieve a transcript for the video")
    
    
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
