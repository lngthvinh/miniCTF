# WRITEUP

Xem nguồn trang Ctrl+U > hint.txt

```php
<?php
if (isset($_GET["password"])) {
    if (hash("md5", $_GET["password"]) == $_GET["password"]) {
       echo $flag;
    }
    else {
        echo "Try again bro";
    }
}
```

Lỗi [Type Juggling md5](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md)
| Hash | “Magic” Number / String    | Magic Hash                                    | Found By / Description      |
| ---- | -------------------------- |:---------------------------------------------:| -------------:|
| MD5  | 0e1137126905               | 0e291659922323405260514745084877              | [@spazef0rze](https://twitter.com/spazef0rze/status/439352552443084800) |

> ISPCLUB{php_1s_Suck}

