<!DOCTYPE html>
<html>
<body>

<?php
$last_line = exec("python crawlerpchome.py http://24h.m.pchome.com.tw/prod/DYAM5C-A9007WN52", $return_arr, $errorCode);

echo $return_arr[0]; // name
echo $return_arr[1]; // price
echo $return_arr[2]; // img
echo $errorCode;
?>

</body>
</html>