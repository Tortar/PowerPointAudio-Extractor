# PowerPointAudio-Extractor

Are you tired to listen to powerpoint audios at normal speed or to extract audio files from it manually ? Use this script ! 

For each powerpoint in the same folder of the script , it extracts and joins audio files in a single file .wav: you can easily speed up the audio from here. 

Don't worry about moving on with the slides: a cute bell sound will warn you ! 

# Simplified Procedure : using exe_extractor folder

Thanks to the .exe file inside the exe_extractor folder, you can run the program even without installing python.

Setting's steps :

1) Download the script clicking on the 'code' button;

2) Create a new empty folder and extract the .zip file there;

3) Put the powerpoints inside the exe_extractor folder;

4) Click on the file extractor.exe 

That's it ! 

- Antivirus could warn you after clicking on the .exe, just quiet it :D : if you don't trust me, check the file first with the antivirus.

# Procedure for Python users : technical details 

The original files are inside py_extractor folder.

Make sure you have installed zipfile and pydub modules on your computer.
You can install them via command prompt with :
<figure><pre><code>> pip install zipfile
> pip install pydub
</code></pre></figure>

You need also to download [ffmpeg software](https://ffmpeg.org/download.html) and add the absolute path of the <code>bin</code> folder to the windows environment variables ; you have to modify the python path variable adding the absolute path.
