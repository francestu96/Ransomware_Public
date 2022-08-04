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

Function Set-EncryptedData{
    [CmdletBinding()]
    Param
    (
        $Key,
        [string]$TextInput
    )    
    $SecureString = New-Object System.Security.SecureString; 
    $Chars = $TextInput.ToCharArray();    
    ForEach($Char in $Chars)
    {
        $SecureString.AppendChar($Char);
    }    
    $EncryptedData = ConvertFrom-SecureString -SecureString $SecureString -Key $Key;
    Return $EncryptedData;
}
 
$Key = Set-SecretKey -Key "YRTWHTRJUUYUYRKB";
$EncrptedData = Set-EncryptedData -Key $Key -TextInput $args[0];
Write-Output $EncrptedData