#VideoConverter
#Michael Patrick
#Last Edit 5 18
#MovToMP4

#Converts .mov files to .mp4
#Uses Converter library from PythonVideoConverter
#Requires ffmpeg installation, and setting PATH to
#ffmpeg.exe and ffprobe.exe

from converter import Converter

if (__name__ == "__main"):
    conv = Converter(r"C:\FFmpeg\bin\ffmpeg.exe", r"C:\FFmpeg\bin\ffprobe.exe")

