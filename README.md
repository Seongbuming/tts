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

### Running Locally

Run the script with the text you want to convert and the output file name:

```sh
python tts.py output.wav "Your text here"
```

#### Arguments

- `output_file`: The name of the output audio file.
- `text`: The text to convert to speech.

#### Example

```sh
python tts.py output.wav "This is the end of the video. Thank you for watching."
```

### Running via GitHub Actions

1. Fork this repository to **your own GitHub account**.
2. Set up your Google Text-to-Speech API key as a secret in your GitHub repository settings:
   1. Go to your forked repository on GitHub.
   2. Click on **Settings**.
   3. Click on **Secrets and variables** → **Actions** in the left sidebar.
   4. Click on **New repository secret**.
   5. Name the secret `GOOGLE_TTS_API_KEY` and paste your API key.
3. Go to the **Actions** tab in your GitHub repository.
4. Select the **Run Text-to-Speech** workflow.
5. Click on **Run workflow**.
6. Enter the `text to convert to speech` and `output file name`.
7. Click **Run workflow**.
8. Once the workflow completes, download the generated audio file from the **Artifacts** section of the workflow run.

## Notes

- Ensure your Google Cloud project is set up with the Text-to-Speech API enabled.
- The API key should be stored securely and not shared publicly.
