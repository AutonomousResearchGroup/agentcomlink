import os
import time
from agentconnectors.discord import start_discord_connector, generate_tts, message_queue
from dotenv import load_dotenv
from elevenlabs import set_api_key

from agentconnectors.discord.connector import send_message

load_dotenv()
voice = os.getenv("ELEVENLABS_VOICE")
model = os.getenv("ELEVENLABS_MODEL")
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def test_generate_tts():
    message = "Hello, world!"

    file_path = generate_tts(message)

    # Check that the file path is constructed correctly
    assert file_path.startswith("./temp/reply_")
    assert file_path.endswith(".mp3")

    # Check that the file has been created
    assert os.path.exists(file_path)

    print("TTS file generated successfully")

    # Additional assertions could check the contents of the file or other properties


def test_start_connector(capfd):
    # Call start_connector function
    start_discord_connector()
    time.sleep(2)
    send_message("Hello, world!", 1107883421759447040)

    # Check the print output
    captured = capfd.readouterr()
    assert "Starting Discord connector" in captured.out
    assert "Discord connector started" in captured.out
