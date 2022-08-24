import datetime
import os
import sys
import time
import sounddevice as sd
from scipy.io.wavfile import write

date = datetime.datetime.now().strftime("%h:%H:%M:%S")
act_log = str(date).replace(":", "-") + "-Log.txt"
audio_log = str(date).replace(":", "-") + "-Audio.wav"

#first of all create a folder named Activity Log
folder = "Activity Log"
save_path = os.path.join(folder, act_log)

folderB = "Activity Log"
save_pathB = os.path.join(folder, audio_log)


def chronicle_log(write, stealth):
    #enabled activity logging
    if stealth == 0:
        print_save = sys.stdout
        f = open(save_path, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        print(y)
        sys.stdout = print_save
        f.close()

    #disabled activity logging
    elif stealth == 1:
        print_save = sys.stdout
        f = open(save_path, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        pass
        #activity logging diabled
        sys.stdout = print_save
        f.close()


def chronicle_audio(dur):
    print("<<< INITIATED CHRONICLE AUDIO MODE >>>")
    print("(●) Recording...")

    frequency = 44100
    duration = dur #records for given amount of mins/secs
    record_audio = sd.rec(int(duration * frequency), samplerate=frequency, channels=2)
    sd.wait()
    write(save_pathB, frequency, record_audio)
    print("Recoding audio completed")


def clean_slate():
    print("<<< INITIATED CLEAN SLATE PROTOCOL >>>")

    mydir = "Activity Log"
    txtfiles = [f for f in os.listdir(mydir) if f.endswith(".txt")]
    wavfiles = [f for f in os.listdir(mydir) if f.endswith(".wav")]
    for f in txtfiles:
        os.remove(os.path.join(mydir, f))

    for f in wavfiles:
        os.remove(os.path.join(mydir, f))

    time.sleep(1)
    print("All activity log files has been deleted")
    #deletes all activity log files in the folder
