#Import all the necessary modules
import librosa
import soundfile
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pickle

#Extracting features from monotonic audio files - mfcc, mel, chroma
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


#List of all emotions
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

#List of observed emotions that will be displayed in the o/p
observed_emotions=['calm', 'happy','angry', 'fearful', 'disgust']


#Getting the dataset and spilitting into train and test
def load_data(test_size=0.25):
    x,y=[],[]
    for file in glob.glob("C:\\xampp\\www\\SpeechToEmotion\\dataset\\Actor_*\\*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)

x_train,x_test,y_train,y_test=load_data(test_size=0.25)

#MLP Classifier with 300 hidden layers and batch size = 256
model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)

model.fit(x_train,y_train)

y_pred=model.predict(x_test)


def load_new_data():
    x,y=[],[]
    for file in glob.glob("C:\\xampp\\www\\SpeechToEmotion\\uploads\\*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return np.array(x),y

xx_test,yy_test=load_new_data()

yy_pred=model.predict(xx_test)

print(yy_pred[len(yy_pred)-1]);

accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)
print(" {:.2f}".format(accuracy*100))
