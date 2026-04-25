$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://127.0.0.1:9123/")
$listener.Prefixes.Add("http://localhost:9123/")
$listener.Start()
Write-Host "Serving on http://127.0.0.1:9123/"
$root = "E:\CLAUDE\PAOLO BACA MANRIQUE"
while ($listener.IsListening) {
    try {
        $ctx = $listener.GetContext()
        $req = $ctx.Request
        $res = $ctx.Response
        $path = [System.Uri]::UnescapeDataString($req.Url.AbsolutePath)
        if ($path -eq "/") { $path = "/inject.html" }
        $file = Join-Path $root $path.TrimStart("/")
        if (Test-Path $file -PathType Leaf) {
            $bytes = [System.IO.File]::ReadAllBytes($file)
            $ext = [System.IO.Path]::GetExtension($file).ToLower()
            $ct = switch ($ext) {
                ".html" {"text/html; charset=utf-8"}
                ".js" {"application/javascript; charset=utf-8"}
                ".css" {"text/css; charset=utf-8"}
                default {"application/octet-stream"}
            }
            $res.ContentType = $ct
            $res.ContentLength64 = $bytes.Length
            $res.OutputStream.Write($bytes, 0, $bytes.Length)
            Write-Host "$($req.HttpMethod) $path -> 200 ($($bytes.Length) bytes)"
        } else {
            $res.StatusCode = 404
            Write-Host "$($req.HttpMethod) $path -> 404"
        }
        $res.Close()
    } catch { Write-Host "Error: $_" }
}
