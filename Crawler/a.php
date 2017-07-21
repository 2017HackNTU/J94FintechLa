<!DOCTYPE html>
<html>
<body>

<?php
$last_line = exec("python crawlerpchome.py http://24h.m.pchome.com.tw/prod/DYAM5C-A9007WN52", $return_arr, $errorCode);
echo $last_line;
print_r($return_arr);// receive data from python
echo $errorCode; // 0 為正常執行
?>

</body>
</html>