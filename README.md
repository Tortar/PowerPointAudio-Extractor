# PowerPointAudio-Extractor

Are you tired to listen to powerpoint audios at normal speed or to extract audio files from it manually ? Use this script ! 

For each powerpoint in the same folder of the script , it extracts and joins audio files in a single file .wav: you can easily speed up the audio from here. 

Don't worry about when moving on with the slides: a cute bell sound will warn you ! 

# Simplified Procedure : using exe_extractor folder

You can use exe_extractor folder with which you can run the program, even without installing python : download the script clicking on the 'code' button, create a new empty folder and extract the .zip file there, eventually put the powerpoints inside the exe_extractor folder and click on the file extractor.exe. That's it ! 

# Procedure for Python users : technical details 

The original files are inside py_extractor folder.

Make sure you have installed zipfile and pydub modules on your computer.
You can install them via command prompt with :
<figure><pre><code>> pip install zipfile
> pip install pydub
</code></pre></figure>

You need also to download [ffmpeg software](https://ffmpeg.org/download.html) and add the absolute path of the <code>bin</code> folder to the windows environment variables ; you have to modify the python path variable adding the absolute path.
