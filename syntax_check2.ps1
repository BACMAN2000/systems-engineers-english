Add-Type -AssemblyName Microsoft.JScript
$full = Get-Content 'E:\CLAUDE\PAOLO BACA MANRIQUE\be-curriculum-data.js' -Raw

# Bisect: find approximate line of error
$lines = $full -split "`n"
Write-Host "Total lines: $($lines.Count)"

function TestParse($code) {
    try {
        [Microsoft.JScript.Eval]::JScriptEvaluate($code, [Microsoft.JScript.Vsa.VsaEngine]::CreateEngine()) | Out-Null
        return $true
    } catch {
        return $false
    }
}

# Try minimal test - just "var x = 1;"
Write-Host "Minimal test: $(TestParse 'var x = 1;')"
Write-Host "Template literal test: $(TestParse 'var x = `hello`;')"
Write-Host "Arrow function test: $(TestParse 'var x = () => 1;')"
Write-Host "Const test: $(TestParse 'const x = 1;')"

# Check first N lines
$top = ($lines[0..100] -join "`n")
Write-Host "First 100 lines parse: $(TestParse $top)"
$top500 = ($lines[0..500] -join "`n")
Write-Host "First 500 lines parse: $(TestParse $top500)"
$top600 = ($lines[0..600] -join "`n")
Write-Host "First 600 lines parse: $(TestParse $top600)"
$top700 = ($lines[0..700] -join "`n")
Write-Host "First 700 lines parse: $(TestParse $top700)"
$top800 = ($lines[0..800] -join "`n")
Write-Host "First 800 lines parse: $(TestParse $top800)"
