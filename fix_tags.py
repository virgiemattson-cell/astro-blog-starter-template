import pathlib
p = pathlib.Path('C:/Users/waqas/Downloads/skyvisible-site/src/components/LocalSEOBanner.astro')
c = p.read_text(encoding='utf-8')
c = c.replace('"Web Development"', '"Website Development"')
# Urdu: ویب ڈیولپمنٹ -> ویب سائٹ ڈیولپمنٹ
old_urdu = 'ویب ڈیولپمنٹ'
new_urdu = 'ویب سائٹ ڈیولپمنٹ'
c = c.replace(old_urdu, new_urdu)
p.write_text(c, encoding='utf-8')
print('Fixed!')
