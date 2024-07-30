# Vimeo Audio Downloader: from video to audio

## Introduction

While watching a conference video on Vimeo, I realized that what I was most interested in was the audio content. To facilitate extracting audio from Vimeo videos, I decided to create this project. This tool allows you to download the audio from any Vimeo video and save it as an MP3 file.

## Features

- Download audio from Vimeo videos
- Save the audio in MP3 format
- Handle TLS fingerprint blocking issues with robust error handling
- Use `yt-dlp` and `youtube-dl` as fallback for better reliability

## Requirements

- Python 3.11.5
- `yt-dlp`
- `brotli`
- `cryptography`

## Python Environment Setup

To ensure a consistent and isolated environment for running the script, it is recommended to set up a Python virtual environment using `pyenv` and `venv`.

### Install `pyenv` using Homebrew

First, install `pyenv` using Homebrew:

```bash
brew install pyenv
```
### Set a Specific Python Version

To use a specific version of Python, run the following commands:
```bash
pyenv install 3.11.5
pyenv shell 3.11.5
```
This sets your shell to use the specified Python version.

### Create a Virtual Environment

To create a virtual environment, run the following command:
```bash
pyenv exec python -m venv .vimeo 
```
This creates a virtual environment named `.vimeo`.

### Activate the Virtual Environment

To activate the virtual environment, run the following command:
```bash
source .vimeo/bin/activate
```
This activates the virtual environment.

### Install Required Packages

To install the required packages, run the following command:
```bash
pip install -r requirements.txt
```
This installs the required packages.

### Install ffmpeg

install ffmpeg using Homebrew:
```bash
brew install ffmpeg
```
## Usage

To download the audio from a Vimeo video, run the following command:
```bash
python src/downloader.py
```
You will be prompted to enter the Vimeo video URL and the output directory where the MP3 file will be saved.


## example

```bash
python src/downloader.py
Enter the Vimeo video URL: https://vimeo.com/123456789
Enter the output directory: /path/to/output
```
## Troubleshooting

- 	•	Ensure ffmpeg is installed and accessible from your PATH.
- 	•	Verify you have the correct permissions to write to the output directory.
- 	•	If the download fails, check your internet connection and try again.
