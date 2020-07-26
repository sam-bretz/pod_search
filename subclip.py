from moviepy.editor import AudioFileClip
import sys

def subclip(start, stop, source_mp3, target_mp3):
  """
  This method will subclip a .mp3 file from the start time to the stop time in seconds

  Params:
  start - start time in the original clip in seconds (float)
  stop - stop time in the original clip in seconds (float)
  source_mp3 - the .mp3 file to subclip from (str)
  target_mp3 - the .mp3 file to write the subclip to (str)
  """

  # Get a clip
  clip = AudioFileClip(source_mp3)
  subclip = clip.subclip(start, stop)
  subclip.write_audiofile(target_mp3)


if __name__ == '__main__':
  subclip(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])