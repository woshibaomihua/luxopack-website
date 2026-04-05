files = ['magnetic-rigid-gift-box.html','sliding-drawer-gift-box.html','custom-mailer-box.html']
for f in files:
    with open(f,'r',encoding='utf-8') as fp:
        content = fp.read()
    content = content.replace('href="/quote/"','href="/quote.html"')
    with open(f,'w',encoding='utf-8') as fp:
        fp.write(content)
    print('Fixed: ' + f)
