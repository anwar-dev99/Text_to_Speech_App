import streamlit as st
import asyncio
import edge_tts
import os

# General-purpose default script
tts_text = """
Hello and welcome!

This is a sample text-to-speech demonstration.  
You can use this script to generate spoken audio from any text you like.  

Text-to-speech technology helps make information more accessible and engaging by converting written words into natural-sounding speech.

Feel free to customize this script with your own content, whether for education, entertainment, or communication.

Thank you for listening, and have a great day!
"""

async def generate_tts(text, file_path):
    tts = edge_tts.Communicate(text, voice="en-GB-RyanNeural")
    await tts.save(file_path)

st.title("Text-to-Speech Demo")

if st.button("Generate and Play Audio"):
    output_file = "general_tts_demo.mp3"
    # Run async function to generate audio
    asyncio.run(generate_tts(tts_text, output_file))
    
    if os.path.exists(output_file):
        st.success("Audio generated successfully!")
        with open(output_file, "rb") as f:
            st.audio(f.read(), format="audio/mp3")
