# Audio Transcription Script

This Python script is designed to transcribe long audio files by splitting them into smaller chunks and then using Google's Cloud Speech-to-Text API to convert speech into text. 

## Features
- **Audio Splitting**: The script splits large audio files into smaller chunks of 60 seconds by default.
- **Speech Recognition**: It uses Google's Cloud Speech-to-Text API to transcribe each chunk of audio.
- **Customizable Starting Point**: The script allows you to start transcribing from a specific chunk index, useful for resuming transcriptions.

## Prerequisites

1. **Google Cloud Account**: 
   - You must have a Google Cloud account and a service account key with access to the Speech-to-Text API. Download the JSON key file and set its path in the script.

2. **Python 3.x**:
   - Make sure you have Python 3.x installed on your system.

3. **Pip**:
   - You will need to install the required Python packages. Ensure `pip` is installed on your system.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/audio-transcription-script.git
    cd audio-transcription-script
    ```

2. **Install Required Python Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Google Cloud Credentials**:
    - Place your Google Cloud service account key JSON file in an accessible location.
    - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to this file.

    ```python
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "path/to/your/keyfile.json"
    ```

## Usage

1. **Place Your Audio File**:
    - Place the `.wav` audio file you want to transcribe in the same directory as the script or specify the path in the `audio_file` variable.

2. **Run the Script**:
    ```bash
    python your_script_name.py
    ```

3. **Transcribe Chunks**:
    - The script will automatically split the audio into chunks and transcribe each one. Transcriptions will be printed in the terminal.

4. **Resume Transcription**:
    - If you need to resume transcribing from a specific chunk, set the `start_chunk` parameter in the `transcribe_chunks()` function.

## Example

```python
transcribe_chunks(chunks, start_chunk=0)
