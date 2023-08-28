import os

os.mkdir('./chap07/sub', 0o666)
input('Hit any key...')
os.rename('./chap07/sub', './chap07/copy')
input('Hit any key...')
os.rmdir('./chap07/copy')