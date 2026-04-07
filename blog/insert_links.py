import os

base = os.path.dirname(os.path.abspath(__file__))

# eco-friendly blog: insert product link after line 131
eco_path = os.path.join(base, 'eco-friendly-packaging-boxes-wholesale.html')
with open(eco_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

insert_eco = '  <p>Looking for a concrete example? Our <a href="/products/eco-corrugated-presentation-box.html" style="color:var(--gold);font-weight:600;">Eco Corrugated Presentation Box</a> is FSC-certified, soy-ink printed, and designed to deliver premium aesthetics with a minimal environmental footprint.</p>\n'
lines.insert(132, '\n')
lines.insert(133, insert_eco)

with open(eco_path, 'w', encoding='utf-8', newline='\n') as f:
    f.writelines(lines)
print('Done: eco-friendly')

# candle blog: insert product link after line 157
candle_path = os.path.join(base, 'luxury-candle-packaging-wholesale.html')
with open(candle_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

old_line = '  <p>A modern, sleek option. It\'s often used for "travel" size candles or gift sets. Ensure the drawer has a ribbon pull for easy access. This style is excellent for social media "slide-out" videos.</p>\n'
new_line = '  <p>A modern, sleek option. It\'s often used for "travel" size candles or gift sets. Ensure the drawer has a ribbon pull for easy access. This style is excellent for social media "slide-out" videos. See our <a href="/products/sliding-drawer-gift-box.html" style="color:var(--gold);font-weight:600;">Sliding Drawer Gift Box</a> &mdash; a top pick for premium candle brands.</p>\n'

for i, line in enumerate(lines):
    if 'slide-out' in line and 'sliding-drawer' not in line:
        lines[i] = new_line
        break

with open(candle_path, 'w', encoding='utf-8', newline='\n') as f:
    f.writelines(lines)
print('Done: candle')
