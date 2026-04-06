import os, re

NEW_FOOTER = '''<footer>
    <div class="container">
        <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:32px;margin-bottom:28px;padding-top:8px;">
            <div>
                <div style="color:#d4a853;font-weight:700;font-size:0.8rem;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">Products</div>
                <div style="display:flex;flex-direction:column;gap:7px;">
                    <a href="/products/magnetic-rigid-gift-box.html" style="color:#aaa;font-size:0.82rem;">Magnetic Rigid Gift Box</a>
                    <a href="/products/custom-mailer-box.html" style="color:#aaa;font-size:0.82rem;">Custom Mailer Box</a>
                    <a href="/products/sliding-drawer-gift-box.html" style="color:#aaa;font-size:0.82rem;">Sliding Drawer Gift Box</a>
                    <a href="/products/modular-presentation-insert-box.html" style="color:#aaa;font-size:0.82rem;">Modular Insert Box</a>
                    <a href="/products/eco-corrugated-presentation-box.html" style="color:#aaa;font-size:0.82rem;">Eco Corrugated Box</a>
                    <a href="/products/gable-top-gift-box.html" style="color:#aaa;font-size:0.82rem;">Gable Top Gift Box</a>
                    <a href="/products/gable-top-gift-box-with-handle.html" style="color:#aaa;font-size:0.82rem;">Gable Top with Handle</a>
                </div>
            </div>
            <div>
                <div style="color:#d4a853;font-weight:700;font-size:0.8rem;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">Company</div>
                <div style="display:flex;flex-direction:column;gap:7px;">
                    <a href="/" style="color:#aaa;font-size:0.82rem;">Home</a>
                    <a href="/products.html" style="color:#aaa;font-size:0.82rem;">All Products</a>
                    <a href="/about.html" style="color:#aaa;font-size:0.82rem;">About LuxoPack</a>
                    <a href="/blog/" style="color:#aaa;font-size:0.82rem;">Packaging Blog</a>
                    <a href="/quote.html" style="color:#aaa;font-size:0.82rem;">Get Free Quote</a>
                </div>
            </div>
            <div>
                <div style="color:#d4a853;font-weight:700;font-size:0.8rem;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">Contact</div>
                <div style="display:flex;flex-direction:column;gap:7px;">
                    <span style="color:#aaa;font-size:0.82rem;">&#128231; sales@luxopack.com</span>
                    <span style="color:#aaa;font-size:0.82rem;">&#127757; MOQ from 100 pcs</span>
                    <span style="color:#aaa;font-size:0.82rem;">&#9889; Quote in 24 Hours</span>
                    <a href="/quote.html" style="display:inline-block;margin-top:8px;background:#d4a853;color:#000;font-weight:700;font-size:0.8rem;padding:8px 18px;border-radius:4px;text-decoration:none;">Request Quote &rarr;</a>
                </div>
            </div>
        </div>
        <div style="border-top:1px solid rgba(255,255,255,0.08);padding-top:20px;">
            <p>&copy; 2026 LuxoPack Packaging Co., Ltd. All Rights Reserved. | FSC Certified Factory | Global Shipping</p>
        </div>
    </div>
</footer>'''

files = [
    'magnetic-rigid-gift-box.html',
    'custom-mailer-box.html',
    'sliding-drawer-gift-box.html',
    'modular-presentation-insert-box.html',
    'eco-corrugated-presentation-box.html',
    'gable-top-gift-box.html',
    'gable-top-gift-box-with-handle.html',
]

base = os.path.dirname(os.path.abspath(__file__))
pattern = re.compile(r'<footer>.*?</footer>', re.DOTALL)

for fname in files:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = pattern.sub(NEW_FOOTER, content)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)
    print(f'Updated: {fname}')

print('All done.')
