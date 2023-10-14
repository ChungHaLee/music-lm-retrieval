from audioset_download import Downloader
d = Downloader(root_path='./audioset', labels=["Music"], n_jobs=2, download_type='eval', copy_and_replicate=False)
d.download(format = 'wav', quality=5)




