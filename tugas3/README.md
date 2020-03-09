# Tugas 3
### Mengubah proses saat download gambar menjadi menggunakan thread :
* Idenya adalah dengan menampung url gambar-gambar yang akan diunduh pada sebuah array list seperti di bawah
```py
array_gambar = ['https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
                'https://s.kaskus.id/images/2020/03/09/8976698_20200309035223.jpg',
                'https://www.itb.ac.id/files/footer/top/Banner_Entrepreneurial_University_-_opening_v34.jpg']
```
* Lalu tambahkan thread pada program untuk mengunduh url pada array_gambar
```py
threads = []
for i in array_gambar:
    t = threading.Thread(target=download_gambar, args=(i,))
    threads.append(t)

for thr in threads:
    thr.start()
```

### Proses Running Program
![](https://github.com/bimaramadhan/progjarB/blob/master/tugas3/gambar/1.PNG?raw=true)

### Hasil Download Gambar
![](https://github.com/bimaramadhan/progjarB/blob/master/tugas3/gambar/2.PNG?raw=true)
