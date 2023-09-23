<?php
$user = 'root';
$password = '';
 
// Database name is geeksforgeeks
$database = 'webcam';
 
// Server is localhost with
// port number 3306
$servername='localhost:3307';
$conn = new mysqli($servername, $user,
                $password, $database);

if(isset($_FILES["webcam"]["tmp_name"])){
  $tmpName = $_FILES["webcam"]["tmp_name"];
  $imageName = date("Y.m.d") . " - " . date("h.i.sa") . '.jpeg';
  move_uploaded_file($tmpName, 'img/' . $imageName);
  
  $date = date("Y/m/d") . " & " . date("h:i:sa");
  $query = "INSERT INTO tb_image VALUES('', '$date', '$imageName')";
  mysqli_query($conn, $query);
}
