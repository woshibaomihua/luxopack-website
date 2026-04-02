@echo off
cd /d "C:\Users\Jacken\.accio\accounts\1751506088\agents\DID-F456DA-2B0D4C\project\luxopack_website"
git add -A
git commit -m "update"
git push origin main
echo.
echo ========================================
echo   Success! Website updated on GitHub.
echo   Cloudflare will refresh in ~1 minute.
echo ========================================
pause
