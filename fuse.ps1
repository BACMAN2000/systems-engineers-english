$root = 'E:\CLAUDE\PAOLO BACA MANRIQUE'
$html = Get-Content -Raw -Path "$root\business-course-platform.html" -Encoding UTF8
$curr = Get-Content -Raw -Path "$root\be-curriculum-data.js" -Encoding UTF8
$mats = Get-Content -Raw -Path "$root\be-materials.js" -Encoding UTF8
$ext  = Get-Content -Raw -Path "$root\be-materials-ext.js" -Encoding UTF8

$html = $html.Replace('<script src="be-curriculum-data.js"></script>', "<script>`n" + $curr + "`n</script>")
$html = $html.Replace('<script src="be-materials.js"></script>',        "<script>`n" + $mats + "`n</script>")
$html = $html.Replace('<script src="be-materials-ext.js"></script>',    "<script>`n" + $ext  + "`n</script>")

# Cambridge exam data files
$camFiles = @('cambridge-ket.js','cambridge-pet.js','cambridge-fce.js','cambridge-cae.js','cambridge-cpe.js')
foreach($f in $camFiles){
    $path = "$root\$f"
    if(Test-Path $path){
        $data = Get-Content -Raw -Path $path -Encoding UTF8
        $html = $html.Replace("<script src=`"$f`"></script>", "<script>`n" + $data + "`n</script>")
        Write-Host "Fused: $f"
    } else {
        Write-Host "WARNING: $f not found, replacing with empty script"
        $html = $html.Replace("<script src=`"$f`"></script>", "<script>/* $f not yet available */</script>")
    }
}

$outPath = "$root\COHASSET-platform-standalone.html"
$utf8NoBOM = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($outPath, $html, $utf8NoBOM)

$size = (Get-Item $outPath).Length
$kb = [math]::Round($size/1024,1)
Write-Host "Created: $outPath"
Write-Host "Size: $kb KB"
