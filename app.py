import asyncio
import edge_tts

# General-purpose default script
quality_script = """
Hello and welcome!

This is a sample text-to-speech demonstration.  
You can use this script to generate spoken audio from any text you like.  

Text-to-speech technology helps make information more accessible and engaging by converting written words into natural-sounding speech.

Feel free to customize this script with your own content, whether for education, entertainment, or communication.

Thank you for listening, and have a great day!
"""

# إعداد TTS
async def main():
    tts = edge_tts.Communicate(quality_script, voice="en-GB-RyanNeural")
    await tts.save("general_tts_demo.mp3")

asyncio.run(main())
