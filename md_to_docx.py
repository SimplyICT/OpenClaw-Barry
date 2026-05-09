import os
import sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def md_to_docx(md_filename):
    if not os.path.exists(md_filename): return
    doc_filename = md_filename.replace('.md', '.docx')
    doc = Document()
    
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    with open(md_filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line: continue
        
        if line.startswith('# '):
            h = doc.add_heading(line[2:], level=0)
            h.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in h.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(22)
                run.font.color.rgb = RGBColor(31, 73, 125) # Navy Blue
        
        elif line.startswith('## '):
            h = doc.add_heading(line[3:], level=1)
            for run in h.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(16)
                run.font.bold = True
                run.font.color.rgb = RGBColor(31, 73, 125) # Navy Blue
        
        elif line.startswith('### '):
            h = doc.add_heading(line[4:], level=2)
            for run in h.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(13)
                run.font.color.rgb = RGBColor(31, 73, 125) # Navy Blue
        
        elif line.startswith('• ') or line.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            parts = line[2:].split('**')
            for i, part in enumerate(parts):
                r = p.add_run(part)
                if i % 2 != 0: r.bold = True
        else:
            p = doc.add_paragraph()
            parts = line.split('**')
            for i, part in enumerate(parts):
                r = p.add_run(part)
                if i % 2 != 0: r.bold = True

    doc.save(doc_filename)
    return doc_filename

if __name__ == "__main__":
    if len(sys.argv) > 1: md_to_docx(sys.argv[1])
