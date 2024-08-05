# Text-to-Speech Converter

This script converts text to speech using the Google Text-to-Speech API. The generated speech is saved as an audio file.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

You can install the required libraries using pip:

```sh
pip install requests python-dotenv
```

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-repo/text-to-speech-converter.git
    cd text-to-speech-converter
    ```

2. Create a .env file in the project directory and add your Google Text-to-Speech API key:
    ```env
    GOOGLE_TTS_API_KEY=your_api_key_here
    ```

## Usage

Run the script with the text you want to convert and the output file name:

```sh
python tts.py output.wav "Your text here"
```

### Arguments

- `output_file`: The name of the output audio file.
- `text`: The text to convert to speech.

### Example

```sh
python tts.py output.wav "This is the end of the video. Thank you for watching."
```

## Notes

- Ensure your Google Cloud project is set up with the Text-to-Speech API enabled.
- The API key should be stored securely and not shared publicly.
