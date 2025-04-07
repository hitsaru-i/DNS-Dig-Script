# DNS Dig script in PowerShell
# AI GENERATED, UMA (Upwork AI) based on original python script, Ian Hill- 2025
$digflags = @('a', 'cname')
$tldlist = Get-Content 'sampleinput.csv'
$outputfile = 'tlddigdata.csv'

Function DigCall {
    param (
        [string]$domain,
        [string]$flag
    )

    try {
        if ($flag -eq 'a') {
            $result = & dig $flag $domain +noall +answer
        } elseif ($flag -eq 'cname') {
            $result = & dig $flag $domain +noall +authority
        } else {
            $result = & dig $flag $domain +short
        }
        return $result
    } catch {
        Write-Output $_.Exception.Message
        return $_.Exception.Message
    }
}

Write-Host "..Start.."

foreach ($line in $tldlist) {
    $domainslist = $line -split ','
    foreach ($tld in $domainslist) {
        $tld = $tld.Trim()
        Write-Host "[>] TLD: $tld"
        foreach ($flag in $digflags) {
            $output = DigCall -domain $tld -flag $flag
            $recordslist = $output -split '`n'
            foreach ($record in $recordslist) {
                if ($record -ne '') {
                    $finalline = "$tld,$flag,$record`n"
                    Write-Host "[....]LINE TO WRITE to csv output:"
                    Write-Host $finalline
                    Add-Content -Path $outputfile -Value $finalline
                    Write-Host "[!] Written."
                }
            }
        }
    }
}

Write-Host "[!!!] End of Process"

