# DFS-BFS

Nama  : Ira Dwita Syafitri Tarigan 
NPM   : 1184024
Kelas : D4 TI 3A

1. DFS atau Depth First Search meruapakan algoritma penelusuaran struktur graf berdasarkan 
kedalaman . Dfs adalah metode berbasis tepi dan bekerja secara rekursif diaman simpul 
dieksplorasi di sepnajang jalur atau tepi .aplikasi Dfs mencakup pemeriksaan dua graf yang terhubung ke tepi , graf yang terhubung kuat , grafik asiklik dan urutan topologi . dalam DFS ruang memori digunakan secara efisien . 

  DFS 

Reprensentasi untuk konfigurasi papan adalah angka antara 00 dan n -1n -1,  dimana nomor iith menunjukan kolom utama di baris ii untuk 0≤i<n0≤i<n . konfigurasi lengkapnya ialah ditentukan oleh daftar yang berisi nomor nn . n dalam Commond "n_queens_solutions (n)" adalah angka seperti 4,5,6 dan lain lain yang menghasilkan semua penempatan yang valid dari n utama di papan n demi n , menggunakan representasi angka antara 00 dan n -1n -1 . contohnya jalan kode berikut dan hasilnya 

  solutions = n_queens_solutions(4)

  next(solutions)

   [1, 3, 0, 2]
   
   next(solutions)
   
   [2,0,3,1]
   
   list(n_queens_solutions(6))
   
   [[1, 3, 5, 0, 2, 4,] , [2, 5, 1, 4, 0, 3],
    [3, 0, 4, 1, 5, 2,], [4, 2, 0, 5, 3, 1]]
    
   len(list(n_queens_solutions(8)))
    
   92 
 
2. BFS atau Breadth First Search merupakan metode traversing yang digunakan dalam grafik . dalam metode ini yang ditekankan adalah pada simpul grafik , BFS dapat berguna dalam menemukan apakah grafik memiliki komponen yang terhubung atau tidak dan itu juga dapat diguanakan dalam mendeteksi grafik bipartit . pemanfaatan ruang memori di bfs tidak efektif . 

   BFS 
   
baris argumen dan kolom adalah biilangan bulat positif yang munujukan ukuran teka teki . misalnya . jalankan di baris perintah : 
python lights_out_gui.py 3 3 

gerakan disk linear BFS 
konfigurasi awal dari teka teki ini adalah baris sel l, dengan disk yang terletak di sel 0 hingga n - 1 . hasilnya ialah memindahkan disk ke akhir baris menggunakan serangkaian tindakan yang dibatasi . disetiap langkah disk hanya dapat dipindahkan ke sel kosong yang berdekatan atau ke sel kosong yang berjarak dua spasi , asalkan disk lain terletak ditengah kotak , dengan adanya pembatas ini terlihat bahwa dalam banyak kasus tidak ada pergerakan yang mungkin dilakukan oleh mayoritas dari disk . misalnya dari posisi awal hanya ada dua pilihan untuk  emindahkan disk terakhir dari sel n - 1 ke sel n atau untuk memindahkan disk kedua ke terakhir dari sel n - 2 ke sel n . 
misalkan seperti berikut ini .

   solve_distinct_disks(4, 2)
    
   [(0, 2), (2, 3), (1, 2)]
    
   solve_distinct_disks(5, 2)
    
   [(0, 2), (1, 3), (2, 4)]
    
   solve_distinct_disks(4, 3)
    
   [(1, 3), (0, 1), (2, 0), (3, 2), (1, 3), (0, 1)]
    
   solve_distinct_disks(5, 3)
    
   [(1, 3), (2, 1), (0, 2), (2, 4), (1, 2)]
    

