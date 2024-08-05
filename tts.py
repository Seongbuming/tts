import os
import requests
import base64
import argparse
from dotenv import load_dotenv

load_dotenv()

language_code = "en-US"
voice_name = "en-US-Studio-Q"

def synthesize_text_to_speech(api_key, text, output_file):
    url = f"https://texttospeech.googleapis.com/v1beta1/text:synthesize?key={api_key}"
    
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    data = {
        "audioConfig": {
            "audioEncoding": "LINEAR16",
            "effectsProfileId": [
                "small-bluetooth-speaker-class-device"
            ],
            "pitch": 0,
            "speakingRate": 1
        },
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": language_code,
            "name": voice_name
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        audio_content = response_data['audioContent']

        with open(output_file, 'wb') as out_file:
            out_file.write(base64.b64decode(audio_content))
        
        print(f"Audio content written to {output_file}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert text to speech using Google Text-to-Speech API.')
    parser.add_argument('output_file', type=str, help='Output audio file name')
    parser.add_argument('text', type=str, help='Text to be converted to speech')

    args = parser.parse_args()
    text = args.text
    output_file = args.output_file

    api_key = os.environ.get("GOOGLE_TTS_API_KEY")
    if not api_key:
        raise ValueError("The GOOGLE_TTS_API_KEY environment variable is not set")

    synthesize_text_to_speech(api_key, text, output_file)
