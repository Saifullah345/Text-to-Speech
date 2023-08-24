import streamlit as st
import gtts
import tempfile

# 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
def text_to_speech(text):
    try:
        speech = gtts.gTTS(text=text)
        # 
        return speech
    except Exception as e:
        st.error("Error occurred during text-to-speech conversion.")
        st.error(str(e))
        return None


def main():
    st.title("Text-to-Speech App")
    st.subheader("Instantly Convert Text to Speech")
    st.info("This is a simple Streamlit application that converts text to speech using the Google Text-to-Speech (gtts) library. It allows the user to enter or paste text, and then generates speech based on that text. The generated speech can be played back using an audio player, or downloaded as an audio file.")

    prompt_text = st.text_area("Enter or paste the text:")

    if st.button("Generate speech"):
        speech = text_to_speech(text=prompt_text)
        if speech:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                speech.save(f.name)
                st.audio(f.name, format='audio/wav')

    if st.button("Download audio file"):
        if prompt_text:
            speech = text_to_speech(text=prompt_text)
            if speech:
                with tempfile.NamedTemporaryFile(delete=False) as f:
                    speech.save(f.name)
                    st.download_button("Download", f.name,
                                       file_name="speech.wav")


if __name__ == "__main__":
    main()
