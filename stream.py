import subprocess
global cmd
baseurl = "http://0.0.0.0:8234"
def openFM(frequency):
    samplerate = 48000
    rtlfm_cmd = ["rtl_fm", "-f", f"{frequency}M", "-s", "200000", "-M", "WBFM", "-r", str(samplerate)]
    rtlfm_process = subprocess.Popen(rtlfm_cmd, stdout=subprocess.PIPE)
    sox_cmd = ["sox", "-t", "raw", "-r", str(samplerate), "-e", "signed", "-b", "16", "-c", "1", "-", "-t", "wav", "-"]
    sox_process = subprocess.Popen(sox_cmd, stdin=rtlfm_process.stdout, stdout=subprocess.PIPE)
    ffmpeg_cmd = ["ffmpeg", "-f", "wav", "-i", "-", "-f", "mp3", "-"]
    ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdin=sox_process.stdout)

        
        


