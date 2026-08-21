import fitz  # PyMuPDF
import os

pdf_path = "paper.pdf"
output_dir = "page_images"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
dpi = 150
zoom = dpi / 72  # 72 is the base DPI for PDF

for i, page in enumerate(doc):
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(output_dir, f"page_{i+1:02d}.png")
    pix.save(out_path)
    print(f"Page {i+1}: {pix.width}x{pix.height} -> {out_path}")

doc.close()
print(f"\nDone. {len(doc)} pages converted.")
