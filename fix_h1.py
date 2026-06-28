import pathlib, re
p = pathlib.Path("src/components/Hero.astro")
c = p.read_text(encoding="utf-8")
c = c.replace("<h1 set:html={content.h1}></h1>", "<h2 set:html={content.h1}></h2>")
c = re.sub(r'\.hero h1', '.hero h2', c)
p.write_text(c, encoding="utf-8")
print("Fixed: Hero H1 -> H2")
