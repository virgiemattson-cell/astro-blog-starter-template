import pathlib,json
d={"a":1}
pathlib.Path("src/components/test3.txt").write_text(json.dumps(d))
