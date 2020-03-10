# Tugas 2
### Mengunakan wireshark, capture :
### 1. Hasil keluaran dari program udpfileclient.py ke alamat 127.0.0.1 ke port 5006
* Ubah file udpfileclient.py, ganti TARGET_IP menjadi **127.0.0.1** dan TARGET_PORT menjadi **5006**

![Hasil_capture_UdpFileClient](https://github.com/bimaramadhan/progjarB/blob/master/tugas2/gambar/no1_1%20-%20Copy.PNG?raw=true)

* Karena menggunakan koneksi local klik 2x pada tulisan **Adapter for loopback traffic capture** dan isi filter menjadi **ip.dst == 127.0.0.1 && udp && udp.port == 5006**
* Berikut hasil capture dari filter

![Hasil_capture_UdpFileClient](https://github.com/bimaramadhan/progjarB/blob/master/tugas2/gambar/no1.PNG?raw=true)


### 2. Hasil keluaran dari program udp_simple.py ke alamat 127.0.0.1 ke port 5006
* Ubah udp_simple.py, ganti TARGET_IP menjadi **127.0.0.1** dan TARGET_PORT menjadi **5006**
* Pesan yang ingin dikirimkan adalah ```Halo Bima Satria Ramadhan NRP 05111740000081```

![Hasil_capture_udp_simple](https://github.com/bimaramadhan/progjarB/blob/master/tugas2/gambar/no2_3%20-%20Copy.PNG?raw=true)

* Karena menggunakan koneksi local klik 2x pada tulisan **Adapter for loopback traffic capture** dan isi filter menjadi **ip.dst == 127.0.0.1 && udp && udp.port == 5006**
* Berikut hasil capture dari filter

![Hasil_capture_udp_simple](https://github.com/bimaramadhan/progjarB/blob/master/tugas2/gambar/no2_1.PNG?raw=true)

* Dapat dilihat bahwa pesan yang dikirimkan dapat tertangkap dan terbaca oleh wireshark
![Hasil_capture_udp_simple](https://github.com/bimaramadhan/progjarB/blob/master/tugas2/gambar/no2_2.PNG?raw=true)

### 3. Hasil keluaran dari program udpfileclient.py ke pc lain dengan alamat 10.151.254.120 ke port 5006
![](https://github.com/bimaramadhan/progjarB/blob/master/tugas2/gambar/no3_1.PNG?raw=true)

### 4. Hasil keluaran dari program udp_simple.py ke pc lain dengan alamat 10.151.254.120 ke port 5006
![](https://github.com/bimaramadhan/progjarB/blob/master/tugas2/gambar/no4_1.PNG?raw=true)
