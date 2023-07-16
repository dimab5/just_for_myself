import telebot
import speech_recognition as sr
from pydub import AudioSegment
import os

API_TOKEN = '5784225971:AAHr-6UzmRqRxo_OOZHSC5PwVJ8dNYschyY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Запишите голосовое сообщение, чтобы оно было переведено в текст.")

@bot.message_handler(content_types=['voice'])
def handle_docs_audio(message):
    file_info = bot.get_file(message.voice.file_id)
    file_path = file_info.file_path

    downloaded_file = bot.download_file(file_path)

    voice_message_file = 'voice_message.ogg'
    with open(voice_message_file, 'wb') as file:
        file.write(downloaded_file)

    AudioSegment.ffmpeg = "C:\\prog\\ffmpeg-4.0.2-win64-static\\bin\\ffmpeg.exe"
    AudioSegment.ffprobe = "C:\\prog\\ffmpeg-4.0.2-win64-static\\bin\\ffprobe.exe"

    audio = AudioSegment.from_file(voice_message_file)

    wav_file = "voice.wav"
    audio.export(wav_file, format="wav")

    r = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='ru-RU')

    os.remove(voice_message_file)
    os.remove(wav_file)

    bot.reply_to(message, text)
    print(text)

bot.infinity_polling()

