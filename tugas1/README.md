# Tugas 1
### Jalankan program server.py di 3 port yang berbeda (31000, 31001, 31002) 
* Hasil capture :
    * Saat server berjalan<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/server%203%20port.PNG?raw=true)

    * Client mengirimkan pesan ke port 31000<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/client%2031000.PNG?raw=true)

    * Client mengirimkan pesan ke port 31001<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/client%2031001.PNG?raw=true)

    * Client mengirimkan pesan ke port 31002<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/client%2031002.PNG?raw=true)


### Jalankan program client.py untuk konek ke server yang jalan pada poin sebelumnya dan mengirimkan string “JARINGAN TEKNIK INFORMATIKA PEMROGRAMAN” 
* Hasil capture :
    * Client mengirimkan pesan<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/client%20string%20informatika.PNG?raw=true)

    * Server menerima pesan dari clien<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/server%20string%20informatika.PNG?raw=true)
    

### Jalankan program server.py di 3 port yang berbeda di 2 komputer yang berbeda dan jalankan program client.py untuk konek ke server pada poin sebelumnya, kirimkan string yang sama
* Hasil capture :
    * Server dijalankan di komputer lain dengan IP : 192.168.100.29. <br>
     ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/server%20kirim%20komputer%20lain.png?raw=true)
    * Client dijalankan di komputer saya dengan IP 192.168.100.6. <br>
     ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/client%20kirim%20komputer%20lain.PNG?raw=true)

### MODIFIKASILAH program client.py dan server.py agar dapat MENTRANSFER file dari client ke server (letakkan program modifikasi di direktori tugas1a)
* Hasil capture :
    * Menjalankan server.py pada PC saya (IP: 192.168.100.6)<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/1a_1.png?raw=true)

    * Menjalankan client.py pada PC lain (IP: 192.168.100.29)<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/1a_2.png?raw=true)

    * File telah terkirim pada PC saya (IP: 192.168.100.6)<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/1a_3.png?raw=true)

### MODIFIKASILAH program server.py agar dapat mengirimkan MENTRANSFER FILE yang di request oleh client (letakkan program modifikasi di direktori tugas1b) 
* Hasil capture :
    * Menjalankan server.py pada PC saya (IP: 192.168.100.6)<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/1b_1.png?raw=true)

    * Menjalankan client.py pada PC lain (IP: 192.168.100.29)<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/1b_2.png?raw=true)

    * File yang di request oleh client.py pada PC lain (IP: 192.168.100.29) telah berhasil dikirimkan oleh server.py pada PC saya (IP: 192.168.100.6)<br>
    ![](https://github.com/bimaramadhan/progjarB/blob/master/tugas1/gambar/1b_3.png?raw=true)
