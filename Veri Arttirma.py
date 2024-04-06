import soundfile as sf
import librosa
import numpy as np
import os



#Write here where you would like to save the Increases sounds
save_file_path="C:\\Users\\....\\Desktop\\Augmented Sounds\\"

#Write the file path of the voices you want to increase here (Only Folder Path)
voices_location="C:\\Users\\....\\Desktop\\Sounds\\"





#Traverses all directories and subdirectories to find all audio data
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
                pitch_swift(full_path, sayi)
                sayi+=1



#Increases Audio data by changing the frequency of the sound
def pitch_swift(audio_file,sayi):
    voice, sr = librosa.load(audio_file)
    shifted_up_sound = librosa.effects.pitch_shift(voice, sr=sr, n_steps=2)
    shifted_down_sound = librosa.effects.pitch_shift(voice, sr=sr, n_steps=-2)
    
    newname=save_file_path+str(sayi)
    sf.write(newname+" shifted_up_sound.wav", shifted_up_sound, sr)
    sf.write(newname+" shifted_down_sound.wav", shifted_down_sound, sr)




#Increases Audio data by adding noise to audio
def noise_add(audio_file,sayi):
  voice, sr = librosa.load(audio_file)
  noise = np.random.normal(0, 0.01, len(voice))
  voice_noisy = voice + noise
  
  newname=save_file_path+str(sayi)+".wav"
  sf.write(newname, voice_noisy, sr)

  


#Increases Audio data by speeding up or slowing down the audio
def time_dilation(audio_file,sayi):
  voice, sr = librosa.load(audio_file)
  sound_fast=librosa.effects.time_stretch(voice,rate=1.2)
  sound_slow=librosa.effects.time_stretch(voice,rate=0.8)
  
  
  newname=save_file_path+str(sayi)
  sf.write(newname+" sound_fast.wav", sound_fast, sr)
  sf.write(newname+" sound_slow.wav", sound_slow, sr)
  

                
        
        
        
        
        
travers_all_folders(voices_location)