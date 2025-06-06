import streamlit as st
import asyncio
import edge_tts
import os

max_chars = 2000

async def generate_tts(text, file_path):
    tts = edge_tts.Communicate(text, voice="en-GB-RyanNeural")
    await tts.save(file_path)

st.title("Text-to-Speech Demo")

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
            output_file = "user_tts_demo.mp3"
            # Generate TTS audio asynchronously
            asyncio.run(generate_tts(user_text, output_file))

            if os.path.exists(output_file):
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
