import librosa
import soundfile
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pickle

def extract_feature(file_name,mfcc,chroma,mel):
  with soundfile.SoundFile(file_name) as sound_file:
    X=sound_file.read(dtype="float32")
    sample_rate=sound_file.samplerate
    if chroma:
      stft=np.abs(librosa.stft(X))
    result=np.array([])
    if mfcc:
      mfccs=np.mean(librosa.feature.mfcc(y=X,sr=sample_rate,n_mfcc=40).T,axis=0)
      result=np.hstack((result,mfccs))
    if chroma:
      chromas=np.mean(librosa.feature.chroma_stft(S=stft,sr=sample_rate).T,axis=0)
      result=np.hstack((result,chromas))
    if mel:
      mels=np.mean(librosa.feature.melspectrogram(X,sr=sample_rate).T,axis=0)
      result=np.hstack((result,mels))
    return result


emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}

observed_emotions=['calm', 'happy','angry', 'fearful', 'disgust']


def load_new_data():
    x,y=[],[]
    for file in glob.glob("C:\\xampp\\www\\SpeechToEmotion\\uploads\\*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
    
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return np.array(x),y

xx_test,yy_test=load_new_data()
pickle_off = open("abcd.pickle","rb")
model,accuracy = pickle.load(pickle_off)
yy_pred=model.predict(xx_test)

print(yy_pred[len(yy_pred)-1])
print(" {:.2f}".format(accuracy*100))
# accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)
