from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

speech_file_path = Path(__file__).parent / "mice-dia.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="alloy",
  input="دو چُوہے تھے جو ایک دُوسرے کے بَہُت گہرے دوست تھے۔ ایک چُوہا شہر کی ایک حویلی میں بِل بنا کر رہتا تھا اور دُوسرا پَہاڑوں کے درمِیان ایک گاؤں میں رہتا تھا۔ گاؤں اور شہر میں فاصِلَہ بَہُت تھا، اِس لِئے وہ کبھی کبھار ہی ایک دُوسرے سے مِلتے تھے۔"

)

response.stream_to_file(speech_file_path)