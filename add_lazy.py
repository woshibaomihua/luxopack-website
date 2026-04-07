import os, re

base = r'C:\Users\Jacken\.accio\accounts\1751506088\agents\DID-F456DA-2B0D4C\project\luxopack_website'

files = [
    'index.html',
    'about.html',
    'products/magnetic-rigid-gift-box.html',
    'products/custom-mailer-box.html',
    'products/sliding-drawer-gift-box.html',
    'products/modular-presentation-insert-box.html',
    'products/eco-corrugated-presentation-box.html',
    'products/gable-top-gift-box.html',
    'products/gable-top-gift-box-with-handle.html',
]

def add_lazy(tag):
    # Skip if already has loading attribute
    if 'loading=' in tag:
        return tag
    # Insert loading="lazy" before the closing >
    return tag.rstrip('>').rstrip('/').rstrip() + ' loading="lazy">'

pattern = re.compile(r'<img\b[^>]*>', re.IGNORECASE)

total = 0
for rel in files:
    path = os.path.join(base, rel)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = 0
    def replacer(m):
        global count
        tag = m.group(0)
        if 'loading=' not in tag:
            count += 1
            return add_lazy(tag)
        return tag
    
    new_content = pattern.sub(replacer, content)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)
    print(f'{rel}: +{count} lazy tags')
    total += count

print(f'\nTotal: {total} images updated')
