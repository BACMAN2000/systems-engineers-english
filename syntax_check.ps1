# Use MSHTML (IE's JS engine) to parse the JS and detect syntax errors
Add-Type -AssemblyName Microsoft.JScript

$js = Get-Content 'E:\CLAUDE\PAOLO BACA MANRIQUE\be-curriculum-data.js' -Raw

try {
    $result = [Microsoft.JScript.Eval]::JScriptEvaluate(
        $js + "; 'OK:' + Object.keys(BE_CURRICULUM).length + ' levels'",
        [Microsoft.JScript.Vsa.VsaEngine]::CreateEngine()
    )
    Write-Host "PARSE OK: $result"
} catch {
    Write-Host "PARSE ERROR: $($_.Exception.Message)"
    if ($_.Exception.InnerException) {
        Write-Host "Inner: $($_.Exception.InnerException.Message)"
    }
}
