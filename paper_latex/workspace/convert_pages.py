#!/usr/bin/env python3
"""Convert all pages of paper.pdf to PNG at 150 DPI using pymupdf."""
import fitz  # pymupdf
import os

pdf_path = "paper.pdf"
output_dir = "page_images"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
dpi = 150
zoom = dpi / 72  # 72 DPI is the base
matrix = fitz.Matrix(zoom, zoom)

print(f"PDF has {len(doc)} pages")

for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=matrix)
    out_path = os.path.join(output_dir, f"page_{i+1:02d}.png")
    pix.save(out_path)
    print(f"  Page {i+1}: {pix.width}x{pix.height} -> {out_path}")

doc.close()
print(f"\nDone. {len(doc)} pages converted to {output_dir}/")
