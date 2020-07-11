# PowerPointAudio-Extractor

Are you tired to listen to powerpoint audios at normal speed or to extract audio files from it manually ? Use this script ! 

For each powerpoint in the same folder of the script , it extracts and joins audio files in a single file .wav: you can easily speed up the audio from here. 

Don't worry about when moving on with the slides: a cute bell sound will warn you ! 

# Simplified Procedure : using exe_file folder

You can use exe_file folder with which you can run the program, even without installing python. Put the powerpoints on the same folder 
and click on the file extractor.exe. That's it !

# Procedure for Python users : technical details 

The original files are inside .github/workflows.

Make sure you have installed zipfile and pydub modules on your computer.
You can install them via commands prompt with :
<figure><pre><code>> pip install zipfile
> pip install pydub
</code></pre></figure>

You need also to download [ffmpeg software](https://ffmpeg.org/download.html) and add the absolute path of the <code>bin</code> folder to the windows environment variables ; you have to modify the python path variable adding the absolute path.
