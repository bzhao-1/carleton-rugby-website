<?php 
$to="support@rn53themes.net";
$subject="Website Enquiry";
$data=$_POST['trname']."<br>";
$data.=$_POST['trcname']."<br>";
$data.=$_POST['trcity']."<br>";
$data.=$_POST['troname']."<br>";
$data.=$_POST['trmem']."<br>";
$data.=$_POST['traddr']."<br>";
$data.=$_POST['trdesc']."<br>";
$data.=$_POST['trmail']."<br>";
$data.=$_POST['trphone']."<br>";

// Always set content-type when sending HTML email
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

// More headers
$headers .= 'From: <admin@website.com>' . "\r\n";
$headers .= 'Cc: rn53themes@gmail.com' . "\r\n";

mail($to,$subject,$data,$headers);
?>