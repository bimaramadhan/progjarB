import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        path = '/gambar/'
        logging.warning(f"writing {namafile}.{ekstensi}")

        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

array_gambar = ['https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
                'https://s.kaskus.id/images/2020/03/09/8976698_20200309035223.jpg',
                'https://www.itb.ac.id/files/footer/top/Banner_Entrepreneurial_University_-_opening_v34.jpg']

if __name__=='__main__':
    threads = []
    for i in array_gambar:
        t = threading.Thread(target=download_gambar, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()