# Tugas 4
## Ketentuan Membaca Format dan Daftar Fitur
```
PROTOCOL FORMAT

KETENTUAN MEMBACA FORMAT
string terbagi menjadi 2 bagian, dipisahkan oleh enter
ENTER COMMAND : (perintah)
ENTER NAMEFILE : (nama file)

FITUR

- upload : untuk membuat file yang dikirim oleh client
  request : upload
  parameter : nama file
  response : berhasil -> OK
             gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar file yang ada

- download : untuk mencari file berdasar nama yang akan dikirimkan ke client
  request: download
  parameter: nama file yang dicari
  response: file yang dicari

- jika command tidak dikenali akan merespon dengan ERRCMD
```

## Cara Melakukan Request & Respon yang Didapat

- Sebelum menjalankan client jalankan **server_thread_file.py** terlebih dahulu
 ![](gambar/server.PNG)

- Jalankan **client.py** dan masukkan perintah sesuai fitur yang tersedia
 ![](gambar/client.PNG)
### Meletakkan File (Upload)

- Pada **client.py** masukkan perintah **upload**
  
  ![](gambar/upload.PNG)
  
- Masukkan nama file yang ingin diupload ke **File Server**

  ![](gambar/upload_meme.PNG)
  
- Berikut respon yang didapat jika file berhasil diupload

  ![](gambar/upload_success.PNG)
  
- Dapat dilihat bahwa file yang bersangkutan sudah berada di dalam direktori File Server

  ![](gambar/upload_hasil.PNG)

### Mengambil File (Download) 

- Pada **client.py** masukkan perintah **download**
  
  ![](gambar/download.PNG)
  
- Masukkan nama file yang ingin didownload ke **File Client**

  ![](gambar/download_11.PNG)
  
- Berikut respon yang didapat jika file berhasil didownload

  ![](gambar/download_sukses.PNG)
  
- Dapat dilihat bahwa file yang bersangkutan sudah berada di dalam direktori **File CLient**

  ![](gambar/download_hasil.PNG)

### Melihat Daftar File (List)

- Pada **client.py** masukkan perintah **list**
  
  ![](gambar/list.PNG)
  
- Client akan mengirimkan string bebentuk json ke server, setelah mendapat balasan dari server maka client akan menampilkan list lalu server akan menerima string berbentuk json dan mengirimkan balasan ke client untuk menampilkan list
- Hasilnya adalah sebagai berikut
  ![](gambar/list_hasil.PNG)
