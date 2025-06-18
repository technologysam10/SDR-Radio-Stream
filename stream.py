import subprocess
global cmd

def openFM(frequency):
    cmd = ["rtl_fm", "-f", f"{frequency}M", "-M", "WBFM"]
    demodulated = subprocess.run(cmd)
    print(demodulated.stdout)
openFM("93.7")