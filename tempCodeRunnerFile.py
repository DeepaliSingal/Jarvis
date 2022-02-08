import speedtest
st=speedtest.Speedtest()
dl=st.download()
up=st.upload()
self.speak(f"we have {dl} bit per second downloading speed and {up} bit per second uploading speed")