# TOEFL Runner local HTTP server
# Serves from project root with full MIME type support (json, mp3, png, etc.)
$port = 9124
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://127.0.0.1:$port/")
$listener.Prefixes.Add("http://localhost:$port/")
try { $listener.Start() } catch {
    Write-Host "Could not start on port $port. Is another instance running?" -ForegroundColor Red
    Write-Host $_
    exit 1
}
$root = "E:\CLAUDE\PAOLO BACA MANRIQUE"
Write-Host ""
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "  TOEFL Runner server" -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "  Root:   $root" -ForegroundColor Gray
Write-Host "  URL:    http://127.0.0.1:$port/toefl-runner.html" -ForegroundColor Yellow
Write-Host "  Cohasset: http://127.0.0.1:$port/COHASSET-platform-standalone.html" -ForegroundColor Yellow
Write-Host "  (Ctrl+C to stop)" -ForegroundColor Gray
Write-Host ""

while ($listener.IsListening) {
    try {
        $ctx = $listener.GetContext()
        $req = $ctx.Request
        $res = $ctx.Response
        $path = [System.Uri]::UnescapeDataString($req.Url.AbsolutePath)
        if ($path -eq "/") { $path = "/toefl-runner.html" }
        $file = Join-Path $root $path.TrimStart("/")
        if (Test-Path $file -PathType Leaf) {
            $bytes = [System.IO.File]::ReadAllBytes($file)
            $ext = [System.IO.Path]::GetExtension($file).ToLower()
            $ct = switch ($ext) {
                ".html" {"text/html; charset=utf-8"}
                ".htm"  {"text/html; charset=utf-8"}
                ".js"   {"application/javascript; charset=utf-8"}
                ".mjs"  {"application/javascript; charset=utf-8"}
                ".css"  {"text/css; charset=utf-8"}
                ".json" {"application/json; charset=utf-8"}
                ".mp3"  {"audio/mpeg"}
                ".wav"  {"audio/wav"}
                ".ogg"  {"audio/ogg"}
                ".m4a"  {"audio/mp4"}
                ".png"  {"image/png"}
                ".jpg"  {"image/jpeg"}
                ".jpeg" {"image/jpeg"}
                ".gif"  {"image/gif"}
                ".svg"  {"image/svg+xml"}
                ".webp" {"image/webp"}
                ".ico"  {"image/x-icon"}
                ".woff" {"font/woff"}
                ".woff2"{"font/woff2"}
                ".ttf"  {"font/ttf"}
                ".pdf"  {"application/pdf"}
                ".txt"  {"text/plain; charset=utf-8"}
                default {"application/octet-stream"}
            }
            $res.Headers.Add("Cache-Control","no-cache")
            $res.Headers.Add("Access-Control-Allow-Origin","*")
            $res.ContentType = $ct
            $res.ContentLength64 = $bytes.Length
            $res.OutputStream.Write($bytes, 0, $bytes.Length)
            Write-Host ("{0,-5} {1,-50} -> 200  ({2:N0} bytes)" -f $req.HttpMethod, $path, $bytes.Length) -ForegroundColor DarkGray
        } else {
            $res.StatusCode = 404
            $msg = [System.Text.Encoding]::UTF8.GetBytes("404 Not Found: $path")
            $res.OutputStream.Write($msg, 0, $msg.Length)
            Write-Host ("{0,-5} {1,-50} -> 404" -f $req.HttpMethod, $path) -ForegroundColor Red
        }
        $res.Close()
    } catch { Write-Host "Error: $_" -ForegroundColor Red }
}
