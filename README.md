# Talk to Llama

This project sets up a local Llama model for interactive chatting, offline-capable.

## Setup

1. Install Ollama: `brew install ollama` (on macOS).

2. Start Ollama service: `brew services start ollama`.

3. Pull the model: `ollama pull llama3.2:3b`.

4. Install Python dependencies: `pip install -r requirements.txt`.

## Usage

- CLI Chat: `ollama run llama3.2:3b` for direct terminal interaction.

- Python Script: `python chat.py` for a simple interactive loop.

Type 'quit' to exit the script.

## Offline

Once the model is pulled, you can chat offline by disconnecting from the internet.