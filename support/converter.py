from pydub import AudioSegment

def convert_first_40_seconds(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)

    first_40_seconds = audio[:40000]

    audio.export(wav_file, format="wav")

    print(f"Conversion completed: {mp3_file} -> {wav_file}")

mp3_file = 'billie-jean-michael-jackson.mp3'
wav_file = 'tes1.wav'

convert_first_40_seconds(mp3_file, wav_file)
