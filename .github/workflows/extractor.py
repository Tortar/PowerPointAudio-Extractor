import os, zipfile, re, shutil
from pydub import AudioSegment

print('Extracting...')
parts = 1
audio_extensions = ('.aiff', '.au', '.mid', '.midi', '.mp3', '.m4a', '.mp4', '.wav', '.wma')
init_dir = os.getcwd() ; init_files = os.listdir()
break_slide = init_dir + '\\' + 'new_slide.wav' #  new_slide.wav (bell sound) is used as a separator from one slide to the other
number_power = len(init_files) - 2

for power in init_files :

    if not power.endswith('.zip') and not power.endswith('.pptx') : continue
    
    base = os.path.splitext(power)[0] ; new_zip = base + '.zip' ; os.rename(power , new_zip)
    with zipfile.ZipFile(new_zip) as myzip:
        for file in myzip.namelist() :
            if file.endswith(audio_extensions) :
                myzip.extract(file)
    myzip.close()

    try : os.chdir(init_dir + '\ppt\media')
    except FileNotFoundError : print('No audio files in {}'.format(power)) ; continue
    
    audio_files = os.listdir()
    for file in audio_files : based = os.path.splitext(file)[0] ; os.rename(file , based + '.wav') 

    wav_audio_files = os.listdir()
    sort_audios = sorted(wav_audio_files, key = lambda x : int(re.search('[0-9]+', x).group()))
    
    repeated = AudioSegment.from_file(break_slide)
    combined_sounds = sum((AudioSegment.from_file(audio) + repeated for audio in sort_audios), AudioSegment.empty())

    name_file = "{}.wav".format(base) ; combined_sounds.export(name_file, format="wav")
    os.rename(os.getcwd() + '\\' + name_file , init_dir + '\\' + name_file)
    
    os.chdir(init_dir); shutil.rmtree('ppt', ignore_errors=True)

    print('Extracted {}/{} audios'.format(parts,number_power)) ; parts += 1
