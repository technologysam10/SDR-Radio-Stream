import subprocess
global cmd
baseurl = ""
def openFM(frequency):
    samplerate = 48000
    rtlfm_cmd = ["rtl_fm", "-f", f"{frequency}M", "-M", "WBFM", "-r", str(samplerate)]
    rtlfm_process = subprocess.Popen(rtlfm_cmd, stdout=subprocess.PIPE)
    sox_cmd = ["sox", "-t", "raw", "-r", str(samplerate), "-e", "signed", "-b", "16", "-c", "1", "-", "-t", "wav", "-"]
    sox_process = subprocess.Popen(sox_cmd, stdin=rtlfm_process.stdout, stdout=subprocess.PIPE)
    ffmpeg_cmd = ["ffmpeg", "-f", "wav", "-i", "-", "-f", "mp3", f"{baseurl}/stream/{frequency}.mp3" ]

        
        


openFM("93.7")