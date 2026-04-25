# =============================================================================
# SETUP-TOEFL-PREMIUM.ps1
# Extracts XYSTPO2.0_2.zip, converts Tpo.db to JSON, and stages everything
# under toefl-premium-assets/ for the premium runner.
#
# Run once (first time): PowerShell -ExecutionPolicy Bypass -File .\SETUP-TOEFL-PREMIUM.ps1
# Requires: Python 3.8+ on PATH (for Tpo.db -> JSON conversion).
# =============================================================================

$ErrorActionPreference = "Stop"
$root  = "E:\CLAUDE\PAOLO BACA MANRIQUE"
$zip   = "C:\Users\Paolo\OneDrive\1.2 ETS_Exams\TOEFL\TOEFL\XYSTPO2.0_2.zip"
$dest  = Join-Path $root "toefl-premium-assets"
$media = Join-Path $dest "media"
$data  = Join-Path $dest "data"
$tmp   = Join-Path $env:TEMP "xystpo_extract"

function Section($s) { Write-Host ""; Write-Host "==> $s" -ForegroundColor Cyan }

if (-not (Test-Path $zip)) { Write-Host "ZIP not found: $zip" -ForegroundColor Red; exit 1 }

Section "Preparing folders"
New-Item -ItemType Directory -Force -Path $dest  | Out-Null
New-Item -ItemType Directory -Force -Path $media | Out-Null
New-Item -ItemType Directory -Force -Path $data  | Out-Null
New-Item -ItemType Directory -Force -Path $tmp   | Out-Null
Write-Host "  dest:  $dest"
Write-Host "  tmp:   $tmp"

Section "Extracting ZIP (only Resources/, skipping Qt5 DLLs & executables)"
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zipObj = [System.IO.Compression.ZipFile]::OpenRead($zip)
$total = 0; $done = 0; $skipped = 0
foreach ($e in $zipObj.Entries) {
    $name = $e.FullName
    # Only Resources/
    if (-not $name.StartsWith("XYSTPO2.0/Resources/")) { $skipped++; continue }
    # Skip trailing / (directories)
    if ($name.EndsWith("/")) { continue }
    $total++
}
Write-Host "  Entries to extract: $total (skipped $skipped non-Resources entries)"

$zipObj.Dispose()
$zipObj = [System.IO.Compression.ZipFile]::OpenRead($zip)
$lastPct = -1
foreach ($e in $zipObj.Entries) {
    $name = $e.FullName
    if (-not $name.StartsWith("XYSTPO2.0/Resources/")) { continue }
    if ($name.EndsWith("/")) { continue }
    $rel = $name.Substring("XYSTPO2.0/Resources/".Length)
    $out = Join-Path $tmp $rel
    $outDir = Split-Path $out -Parent
    if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($e, $out, $true)
    $done++
    $pct = [int](($done / $total) * 100)
    if ($pct -ne $lastPct -and ($pct % 5) -eq 0) {
        Write-Progress -Activity "Extracting" -Status "$done / $total files" -PercentComplete $pct
        $lastPct = $pct
    }
}
$zipObj.Dispose()
Write-Progress -Activity "Extracting" -Completed
Write-Host "  Extracted $done files to $tmp" -ForegroundColor Green

Section "Copying Tpo.db and media folders to toefl-premium-assets/"
# Copy the database aside for the Python converter
Copy-Item -Path (Join-Path $tmp "Tpo.db") -Destination (Join-Path $dest "Tpo.db") -Force
# Move/copy each TpoN folder into media/
$tpoDirs = Get-ChildItem -Path $tmp -Directory -Filter "Tpo*" | Where-Object { $_.Name -match "^Tpo\d+$" }
Write-Host "  Found $($tpoDirs.Count) TPO folders"
foreach ($d in $tpoDirs) {
    $target = Join-Path $media $d.Name.ToLower()  # tpo1, tpo2, ...
    if (Test-Path $target) { Remove-Item -Recurse -Force $target }
    Copy-Item -Path $d.FullName -Destination $target -Recurse -Force
    Write-Host "    copied $($d.Name) -> media/$($d.Name.ToLower())"
}
# Optional: also copy data/ (HTML explanations) if present
if (Test-Path (Join-Path $tmp "data")) {
    Copy-Item -Path (Join-Path $tmp "data") -Destination (Join-Path $dest "exp-html") -Recurse -Force
    Write-Host "  Copied explanation HTML pack"
}

Section "Converting Tpo.db -> JSON per TPO (Python)"
$pyScript = Join-Path $dest "convert_tpo_db.py"
if (-not (Test-Path $pyScript)) {
    Write-Host "  convert_tpo_db.py missing at $pyScript" -ForegroundColor Red
    Write-Host "  Make sure it was generated beside this script." -ForegroundColor Red
    exit 1
}
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command py -ErrorAction SilentlyContinue }
if (-not $python) { $python = Get-Command python3 -ErrorAction SilentlyContinue }
if (-not $python) {
    Write-Host "  Python not found on PATH. Install Python 3.8+ and re-run this script." -ForegroundColor Red
    Write-Host "  (Or manually run: py `"$pyScript`")" -ForegroundColor Yellow
    exit 1
}
Write-Host "  Using Python: $($python.Source)"
& $python.Source $pyScript "$dest"
if ($LASTEXITCODE -ne 0) { Write-Host "  Python converter failed." -ForegroundColor Red; exit 1 }

Section "Cleanup temp extraction folder"
Remove-Item -Recurse -Force $tmp
Write-Host "  Removed $tmp"

Section "DONE"
Write-Host "  Premium assets ready at: $dest" -ForegroundColor Green
Write-Host "  Open: $root\toefl-premium-runner.html (use LAUNCH-TOEFL-PREMIUM.bat)" -ForegroundColor Yellow
