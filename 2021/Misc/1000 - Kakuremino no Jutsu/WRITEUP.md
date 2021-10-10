# WRITEUP

* Sử dụng tool binwalk để kiểm tra tệp được nhúng bên trong ảnh.

<img src=solve/010649.png>

```
# binwalk Scroll.png                    

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 200 x 200, 8-bit/color RGB, non-interlaced
91            0x5B            Zlib compressed data, compressed
83762         0x14732         RAR archive data, version 5.x
```

* Phát hiện có file .rar bên trong ảnh. Tiến hành giải nén file ảnh với option `-e`.

```
# binwalk -e Scroll.png
```

* Tiếp tục giải nén file .rar ta được 1 file .txt và 1 file .png

```
Nội dung file hint2.txt
What is the name of the mountain containing this scroll?
```

File ảnh
<img src=solve/010919.png>

* Tiếp tục kiểm tra file ảnh.

```
# binwalk 'Toad tomb scroll.png'

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 720 x 360, 8-bit/color RGB, non-interlaced
91            0x5B            Zlib compressed data, compressed
130123        0x1FC4B         RAR archive data, version 5.x
```

* Tiếp tục có file .rar được nhúng bên trong ảnh. Nhưng không thể giải nén được do có password.
* Theo gợi ý `hint2.txt` là tên ngọn núi được đề cập trong ảnh. Vậy núi cóc `MYOBOKU` là pass của file .rar (Bạn nào xem Naruto sẽ biết nhé)
* Giải nén file .rar với pass `MYOBOKU` ta được 1 folder và 1 file .txt

<img src=solve/011829.png>

```
Nội dung file F^ckkkkkkkkkkkkkkkkkkkk.txt
[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]][([][(![]+[])[+[]]+(![]+[])...

```

Bên trong folder Scroll Room
<img src=solve/012049.png>

* Nhìn vào nội dung file F^ck thi đây là [JSFuck](http://www.jsfuck.com/). Tiếp theo sử dụng [JSfuck Decoder](https://enkhee-osiris.github.io/Decoder-JSFuck/) ta được.

```
The flag is planted on the ground but it flies in the sky
```

* Sử dụng binwalk kiểm tra tất cả file ảnh trong folder Scroll Room. Phát hiện có 1 được nhúng.

```
# binwalk *
...
Target File:   /root/_Scroll.png.extracted/_Toad tomb scroll.png.extracted/1FC4B/Scroll Room/d2hlcmUgaXMgdGhlIGZsYWc.png
MD5 Checksum:  f9e9c6dde4e68aef88accb12db9fdc7d
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 199 x 326, 8-bit/color RGB, non-interlaced
91            0x5B            Zlib compressed data, compressed
117341        0x1CA5D         RAR archive data, version 5.x
...
```




