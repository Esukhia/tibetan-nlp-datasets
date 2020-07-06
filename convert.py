import pyewts
from pathlib import Path

converter = pyewts.pyewts()

file = "42-Sera-Textbook-Definitions.txt"

in_path = Path(f"dictionaries/{file}" )
out_path = in_path.parent / f'{in_path.stem}_uni{in_path.suffix}'
out_path.touch()

orig = in_path.read_text(encoding="utf-8")

res = converter.toUnicode(orig)

out_path.write_text(res, encoding="utf-8")