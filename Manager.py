import streamlit as st
from whisperModel import process_audio, ai_support
import assemblyai as aai
import streamlit_extras as ste


try:
    if not st.session_state['transcription']['processed']:
        # set the session state
        st.session_state['replicate_key'] = None
        st.session_state["transcription"] = {
            "processed": False,
            "FileName": "",
            "Transcription": "",
            "Detected Language": "",
        }
except KeyError:
    st.session_state['replicate_key'] = None
    st.session_state["transcription"] = {
        "processed": False,
        "FileName": "",
        "Transcription": "",
        "Detected Language": "",
    }

st.title("AI Transcription Engine")

# tabs [Transcribe, Co-pilot]
t, c = st.tabs(["Transcribe", "Co Pilot"])

with t:
    # 
    st.subheader("Upload Audio")
    uploaded_file = st.file_uploader("audio file")

    if uploaded_file is not None:
        if st.button("Process Audio"):
            audio_file_location = uploaded_file.name
            result = process_audio(audio_file_location)

            transcription = result["transcription"]
            detected_language = result["detected_language"]

            # declare the session state
            st.session_state['transcription'] = {
                "processed": True,
                "FileName": audio_file_location,
                "Transcription": transcription,
                "Detected Language": detected_language
            }

            # show treanscrtipton
            st.markdown(f"""
                #### Transcription
                **Detected Language**: {detected_language}   
                **Transcription**:   
                {transcription}
                """)
# Analyze the returned transcription
with c:
    st.subheader("Transcription Analysis")
    if st.session_state['transcription']['processed']:
        st.markdown(f"""
        #### Transcription
        **Detected Language**: {st.session_state['transcription']['Detected Language']}   
        **Transcription**:   
        {st.session_state['transcription']['Transcription']}
        """)

        user_input = st.text_input("what do you need to change about the transcription?")
        submit = st.button("Submit")
        if submit and user_input:
            prompt = f"We Using this Transcription: \n {st.session_state['transcription']['Transcription']} as the context and below is our previous conversation:\n  'User': {user_input}"

            # call the model for a response from the AI
            response = ai_support(prompt) 
            st.write(response)




    
