#!/usr/bin/env python3
"""Programmatic review of paper.pdf for layout issues."""
import fitz  # pymupdf

doc = fitz.open("paper.pdf")
print(f"Total pages: {len(doc)}")
print(f"Page size: {doc[0].rect}")
print()

# Check each page
for i, page in enumerate(doc):
    print(f"=== Page {i+1} ===")
    
    # Get text
    text = page.get_text()
    lines = text.strip().split('\n')
    print(f"  Lines of text: {len(lines)}")
    
    # First 3 lines
    for line in lines[:3]:
        print(f"  > {line[:100]}")
    
    # Check for figures
    images = page.get_images(full=True)
    if images:
        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            img_ext = base_image["ext"]
            print(f"  IMAGE: {len(img_bytes)} bytes, {img_ext}, {base_image['width']}x{base_image['height']}")
    
    # Check for ?? (uncited references)
    if "??" in text:
        print(f"  WARNING: Found '??' - uncited references!")
    
    # Check for [FIGURE: markers
    if "[FIGURE:" in text:
        print(f"  WARNING: Found '[FIGURE:' marker - not replaced!")
    
    # Check for overfull hbox
    # (can't check this from pymupdf, need to check log)
    
    print()

doc.close()

# Check log for overfull boxes
print("=== Checking log for overfull boxes ===")
with open("paper.log", "r") as f:
    log = f.read()
    
overfull = [line for line in log.split('\n') if 'Overfull' in line]
if overfull:
    print(f"Found {len(overfull)} overfull warnings:")
    for line in overfull[:10]:
        print(f"  {line.strip()}")
else:
    print("No overfull box warnings.")

# Check for undefined references
undef = [line for line in log.split('\n') if 'undefined' in line.lower()]
if undef:
    print(f"\nFound {len(undef)} undefined reference warnings:")
    for line in undef[:10]:
        print(f"  {line.strip()}")
else:
    print("\nNo undefined reference warnings.")

# Check for bad box warnings
badbox = [line for line in log.split('\n') if 'Bad box' in line]
if badbox:
    print(f"\nFound {len(badbox)} bad box warnings")
else:
    print("\nNo bad box warnings.")

print("\n=== Summary ===")
print(f"Pages: {len(doc)}")
print(f"Images in PDF: {sum(len(page.get_images()) for page in doc)}")
