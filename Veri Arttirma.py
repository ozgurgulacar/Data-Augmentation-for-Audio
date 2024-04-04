import soundfile as sf
import librosa
import numpy as np
import os



def noise_add(audio_file,sayi):
  voice, sr = librosa.load(r"Path to the File to Increase the Volume (Only Folder Path)"+audio_file)
  noise = np.random.normal(0, 0.01, len(voice))
  voice_noisy = voice + noise
  newname2=""
  if audio_file.endswith(".webm"):
      newname2=audio_file[:-5]
  else:
      newname2=audio_file[:-4]
      
  #newname2="Save File Path "+str(sayi)+" "+newname+".wav"
  #sf.write(newname2, voice_noisy, sr)
  
  newname="Save File Path "+str(sayi)+".wav"
  sf.write(newname, voice_noisy, sr)
  


def time_dilation(audio_file,sayi):
  voice, sr = librosa.load(r"Path to the File to Increase the Volume (Only Folder Path)"+audio_file)
  sound_fast=librosa.effects.time_stretch(voice,rate=1.2)
  sound_slow=librosa.effects.time_stretch(voice,rate=0.8)
  
  newname2=""
  if audio_file.endswith(".webm"):
      newname2=audio_file[:-5]
  else:
      newname2=audio_file[:-4]
  
  
  #newname2="Save File Path "+str(sayi)+" "+newname2
  #sf.write(newname2+"sound_fast.wav", sound_fast, sr)
  #sf.write(newname2+"sound_slow.wav", sound_slow, sr)
  
  newname="Save File Path"+str(sayi)
  sf.write(newname+" sound_fast.wav", sound_fast, sr)
  sf.write(newname+" sound_slow.wav", sound_slow, sr)
  

        

def travers_all_folders(Directory):
    sayi=1
    for item in os.listdir(Directory):
        full_path = os.path.join(Directory, item )
        if os.path.isdir(full_path):
            travers_all_folders(full_path)
        else:
            if item.endswith(".wav") or item.endswith(".webm"):
                time_dilation(full_path,sayi)
                noise_add(full_path,sayi)
                sayi+=1
                
        

travers_all_folders(r"Audio files folder")
