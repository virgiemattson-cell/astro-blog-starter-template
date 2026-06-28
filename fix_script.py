import pathlib
p = pathlib.Path("src/components/LocalSEOBanner.astro")
c = p.read_text(encoding="utf-8")
c = c.replace("ویب ڈویلپمنٹ", "ویب ڈیولپمنٹ")
p.write_text(c, encoding="utf-8")
print("Fixed: Urdu spelling corrected")
