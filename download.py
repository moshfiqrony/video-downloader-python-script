import requests
import progressbar

urls = [
	# give your url strings here
	]

for url in urls:
	fileName = url.split('?')[0].split('//')[1].replace('/', '_')
	print(fileName+' ----------- Started')

	response = requests.get(url, stream=True)
	contentLen = int(response.headers.get('Content-Length'))/1000000


	print(contentLen)
	print('Downloading ---- ')


	c = 1
	downloaded = 0
	downloadedFile = ''


	bar = progressbar.ProgressBar(maxval=contentLen, \
	widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	bar.start()


	for chunk in response.iter_content(chunk_size = 256):
		downloaded = 256*c
		bar.update(int(downloaded/1000000))
		c = c+1
		downloadedFile= downloadedFile+chunk
	bar.finish()


	with open(fileName, 'wb') as f:
		f.write(downloadedFile)
		print(fileName+' ----------- Finished')
