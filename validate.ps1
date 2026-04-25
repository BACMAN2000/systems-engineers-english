$js = Get-Content 'E:\CLAUDE\PAOLO BACA MANRIQUE\be-curriculum-data.js' -Raw

Write-Host "=== Lessons per level ==="
$levels = @('a1','a2','b1','b2','c1','c2')
foreach ($lv in $levels) {
    $pattern = 'id:"be-' + $lv + '-\d+"'
    $count = ([regex]::Matches($js, $pattern)).Count
    Write-Host "  $($lv.ToUpper()): $count lessons"
}

Write-Host ""
Write-Host "=== Exercise types ==="
$types = [ordered]@{
    'rd'='Reading'; 'ls'='Listening'; 'mt'='Matching'; 'dd'='Drag&Drop';
    'fl'='OpenCloze'; 'wf'='WordForm'; 'kt'='KeyTrans'; 'wr'='Writing'
}
foreach ($t in $types.Keys) {
    $pattern = 'type:"' + $t + '"'
    $count = ([regex]::Matches($js, $pattern)).Count
    $name = $types[$t]
    Write-Host "  $name`: $count"
}

Write-Host ""
Write-Host "=== Structural balance ==="
$open = ($js.ToCharArray() | Where-Object {$_ -eq '{'}).Count
$close = ($js.ToCharArray() | Where-Object {$_ -eq '}'}).Count
$bopen = ($js.ToCharArray() | Where-Object {$_ -eq '['}).Count
$bclose = ($js.ToCharArray() | Where-Object {$_ -eq ']'}).Count
$popen = ($js.ToCharArray() | Where-Object {$_ -eq '('}).Count
$pclose = ($js.ToCharArray() | Where-Object {$_ -eq ')'}).Count
$diff1 = $open - $close
$diff2 = $bopen - $bclose
$diff3 = $popen - $pclose
Write-Host "  Curly {} : $open / $close (diff: $diff1)"
Write-Host "  Square [] : $bopen / $bclose (diff: $diff2)"
Write-Host "  Parens () : $popen / $pclose (diff: $diff3)"

Write-Host ""
Write-Host "=== File stats ==="
$lines = (Get-Content 'E:\CLAUDE\PAOLO BACA MANRIQUE\be-curriculum-data.js').Count
$size = $js.Length
Write-Host "  Lines: $lines"
Write-Host "  Chars: $size"

Write-Host ""
Write-Host "=== Try JavaScript parse via JScript ==="
try {
    Add-Type -AssemblyName Microsoft.JScript
    $engine = New-Object Microsoft.JScript.Vsa.VsaEngine
    # Just check file parses by syntax-only evaluation is not straightforward
    Write-Host "  JScript engine available"
} catch {
    Write-Host "  Could not load JScript: $_"
}
