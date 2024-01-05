#pip install speedtest-cli
import speedtest

speed = speedtest.speedtest()
download = speed.download()
upload = speed.upload()

print(f"Download speed:{download}")
print(f"Upload speed:{upload}")


