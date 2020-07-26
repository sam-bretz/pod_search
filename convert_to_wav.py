import sys
from pydub import AudioSegment

def convert_mp3_to_wav(file_mp3):
  file_wav = file_mp3.replace('.mp4', '.wav')
  sound = AudioSegment.from_mp3(file_mp3)
  sound.export(file_wav, format="wav")

def subclip(start, stop, source_mp3=None, target_wav=None):
  """
  This method will subclip a .mp3 file from the start time to the stop time in seconds
  and export it to .wav

  Params:
  start - start time in the original clip in seconds (float)
  stop - stop time in the original clip in seconds (float)
  source_mp3 - the .mp3 file to subclip from (str)
  target_wav - the .wav file to write the subclip to (str)
  """

  # Get a clip
  audio_seg = AudioSegment.from_file(source_mp3)
  audio_seg = audio_seg[int(start)*1000:int(stop)*1000]
  audio_seg.export(target_wav, format='wav')

if __name__ == '__main__':
  file = sys.argv[1]
  subclip(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


