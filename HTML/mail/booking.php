<?php 
$to="support@rn53themes.net";
$subject="Website Enquiry";
$data=$_POST['bname']."<br>";
$data.=$_POST['bmail']."<br>";
$data.=$_POST['bphone']."<br>";
$data.=$_POST['bdate']."<br>";
$data.=$_POST['bcity']."<br>";
$data.=$_POST['baddress']."<br>";

// Always set content-type when sending HTML email
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

// More headers
$headers .= 'From: <admin@website.com>' . "\r\n";
$headers .= 'Cc: rn53themes@gmail.com' . "\r\n";

mail($to,$subject,$data,$headers);
?>