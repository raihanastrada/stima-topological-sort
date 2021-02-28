# Tugas Kecil 2 IF2211 Strategi Algoritma
Topological Sort

## Deskripsi Program
Algoritma Topological Sort merupakan suatu algoritma pengurutan simpul (node) dalam graf
berarah (directed graph) yang mana untuk setiap sisi berarah dari A ke B, simpul A akan diurutkan lebih
dahulu jika dibandingkan dengan B. Terdapat berbagai kegunaan pada topological sort dan salah satu kegunaannya adalah untuk menyusun rencana mata kuliah. Program akan membaca file input dengan format 
```
<kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah
prasyarat - 3>.
<kode_kuliah_2>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode_kuliah_3>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah
prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode_kuliah_4>
.
.
.
```
kemudian akan menentukan mata kuliah yang akan diambil untuk setiap semesternya. Program ini menerapkan pendekatan *Decrease & Conquer* yaitu dengan cara mengubah file input menjadi *Directed Acyclic Graph* kemudian menghapus simpul & sisi berarah dari simpul dengan *in-degree* yang bernilai 0 secara terus menerus hingga menemukan dan menuliskan solusinya dengan format
```
Semester I    : <kode_kuliah_1>,<kode_kuliah_2>
Semester II   : <kode_kuliah_3>
Semester III  : <kode_kuliah_4>,<kode_kuliah_5>
.
.
Semester VIII : <kode_kuliah_X>.
```
*Panjang semester dan banyaknya mata kuliah pada satu semester bergantung pada input*

## Requirement
* Python v3.8+

## Cara menjalankan
1. Download file .zip kemudian extract ke dalam folder atau dapat juga dengan menjalankan command dibawah pada terminal
```
git clone https://github.com/raihanastrada/stima-topological-sort.git
```
2. Buka terminal / IDE yang akan digunakan
3. Masuk ke folder src
4. Jalankan program dengan command
```
python3 13519113.py
```
atau
```
python 13519113.py
```
5. Masukkan nama file permasalahan dan program akan menampilkan hasilnya

## Dibuat oleh
* Raihan Astrada Fathurrahman (13519113)
