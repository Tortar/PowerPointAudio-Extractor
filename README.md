# PowerPointAudio-Extractor

Are you tired to listen to powerpoint audios at normal speed or to extract audio files from it manually ? Use this script ! 

For each powerpoint in the same folder of the script , it extracts and joins audio files in a single file .wav: you can easily speed up the audio from here. 

Don't worry about moving on with the slides: a cute bell sound will warn you ! (you can change the new_slide.wav sound if you don't like it, you just have to mantain the same name for the new file)

# Setup 

Make sure you have installed pydub module on your computer.
You can install it via command prompt with :
<figure><pre><code>> pip install pydub
</code></pre></figure>

You need also to download [ffmpeg software](https://ffmpeg.org/download.html) for your operating system .

If you have Windows, you need to add the absolute path of the <code>bin</code> folder of ffmpeg to the Windows environment variables : you have to modify the variable where the python path is located adding the absolute path of ffmpeg. For other operating systems the procedure is similar.

Lastly, you need to put your powerpoints(.pptx) inside the py_extractor folder. That's it!


# Recover corrupted powerpoints presentation

In the case you have corrupted audio file in your presentation (the audios could work when clicking on the .pptx, but the file are considered corrupted in .zip mode) it will not be possible to use the script. To recover the audio files follow this guide :

![corrupted](https://user-images.githubusercontent.com/68152031/110470930-c1a5e500-80db-11eb-9de8-4e6151a7ec21.PNG)

