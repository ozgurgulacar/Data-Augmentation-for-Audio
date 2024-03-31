

import soundfile as sf
import librosa
import numpy as np
import os



def gurultu_ekle(ses_dosyasi,sayi):
  ses, sr = librosa.load(r"Sesi Arttıralacak Dosyanın Yolu (Sadece Klasör yolu)"+ses_dosyasi)
  gurultu = np.random.normal(0, 0.01, len(ses))
  ses_gurultulu = ses + gurultu
  yeniisim=""
  if ses_dosyasi.endswith(".webm"):
      yeniisim=ses_dosyasi[:-5]
  else:
      yeniisim=ses_dosyasi[:-4]
  yeniisim="C:Kaydedilecek Dosya Yolu "+str(sayi)+".wav"
  sf.write(yeniisim, ses_gurultulu, sr)


def zaman_carpitma(ses_dosyasi,sayi):
  ses, sr = librosa.load(r"Sesi Arttıralacak Dosyanın Yolu (Sadece Klasör yolu)"+ses_dosyasi)
  ses_hizli=librosa.effects.time_stretch(ses,rate=1.2)
  ses_yavas=librosa.effects.time_stretch(ses,rate=0.8)
  yeniisim=""
  if ses_dosyasi.endswith(".webm"):
      yeniisim=ses_dosyasi[:-5]
  else:
      yeniisim=ses_dosyasi[:-4]
  yeniisim="Kaydedilecek Dosya Yolu"+str(sayi)
  sf.write(yeniisim+"ses_hizli.wav", ses_hizli, sr)
  sf.write(yeniisim+"ses_yavas.wav", ses_yavas, sr)
  

        

def klasor_gez_oksurukvar(dizin):
    sayi=1
    for a in os.listdir(dizin):
        tam_yol = os.path.join(dizin, a)
        if os.path.isdir(tam_yol):
            klasor_gez_oksurukvar(tam_yol)
        else:
            if a.endswith(".wav") or a.endswith(".webm"):
                zaman_carpitma(tam_yol,sayi)
                gurultu_ekle(tam_yol,sayi)
                sayi+=1
                
        

klasor_gez_oksurukvar(r"Seslerin bulunduğu Dosya")
