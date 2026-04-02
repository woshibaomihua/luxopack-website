@echo off
echo ================================================
echo  LuxoPack Website - Full Push to GitHub
echo ================================================
echo.
cd /d "C:\Users\Jacken\.accio\accounts\1751506088\agents\DID-F456DA-2B0D4C\project\luxopack_website"
git add -A
git commit -m "v5: 8 products, craft showcase, price anchors, upgraded 4-step process, quote.html, support.html"
git push origin main
echo.
echo ================================================
echo  Done! Visit https://luxopack-website.pages.dev
echo  (Cloudflare deploys in ~1 minute after push)
echo ================================================
pause
