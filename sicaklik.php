<?php
echo "<span style='font-size:15px;'><font face='Tahoma,Verdana,Arial tur' color='#000000'>";
echo "Raspberry Cpu Isı Verileri<br>";

///////// Database Bilgileri
$host = "localhost"; /* Host name */
$user = "raspberry"; /* User */
$password = "pi"; /* Password */
$dbname = "raspberry_sistem"; /* Database name */

/////// Database Bağlantısı
$con = mysqli_connect($host, $user, $password,$dbname);
if (!$con) {
 die("Connection failed: " . mysqli_connect_error());
}

////////////// Veri Çek
$sql  = "SELECT * FROM cpu_temp";
$sorgu=mysqli_query($con,$sql);
while( $sonuc=mysqli_fetch_array($sorgu,MYSQLI_NUM) ){
echo "No: $sonuc[0]<br>";
echo "Tarih: $sonuc[1]<br>";
echo "Saat: $sonuc[2]<br>";
echo "Sıcaklık: $sonuc[3] °C<br>";
echo "<br>";
}
echo "</font></span>";
?>
