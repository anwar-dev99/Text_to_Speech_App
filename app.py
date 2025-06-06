import streamlit as st
import asyncio
import edge_tts
import os

max_chars = 2000

voice_map = {
    "English": {
        "Male": "en-GB-RyanNeural",
        "Female": "en-GB-SoniaNeural"
    },
    "Arabic": {
        "Male": "ar-SA-HamedNeural",
        "Female": "ar-SA-ZariyahNeural"
    }
}

async def generate_tts(text, voice, file_path):
    try:
        tts = edge_tts.Communicate(text, voice=voice)
        await tts.save(file_path)
        return True, None
    except Exception as e:
        return False, str(e)

st.title("Text-to-Speech Demo (English & Arabic)")

language = st.selectbox("Select Language:", ["English", "Arabic"])
gender = st.radio("Select Voice Gender:", ["Male", "Female"])

user_text = st.text_area("Enter text to convert to speech:", height=150, max_chars=max_chars)
chars_used = len(user_text)
st.write(f"Characters used: {chars_used}/{max_chars}")

if chars_used > max_chars:
    st.error(f"Please limit your input to {max_chars} characters or less.")
else:
    if st.button("Generate and Play Audio"):
        if user_text.strip() == "":
            st.warning("Please enter some text to generate speech.")
        else:
            selected_voice = voice_map[language][gender]
            output_file = "user_tts_demo.mp3"

            # Run the async function and handle errors
            success, error_msg = asyncio.run(generate_tts(user_text, selected_voice, output_file))

            if success:
                st.success("Audio generated successfully!")
                with open(output_file, "rb") as f:
                    audio_bytes = f.read()
                    st.audio(audio_bytes, format="audio/mp3")
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name="tts_audio.mp3",
                    mime="audio/mp3"
                )
            else:
                st.error(f"Failed to generate audio: {error_msg}")
