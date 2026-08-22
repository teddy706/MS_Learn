import json
import re

loc = {}
with open("generate_m365_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
modules = loc["modules"]

md_lines = []
md_lines.append("# 📘 Microsoft 365 Copilot 통신·네트워크 엔지니어링 실무 마스터 커리큘럼")
md_lines.append("\n> **안내**: 이 마크다운 파일의 제목, 부제, 본문 설명 및 실무 프롬프트 내용을 자유롭게 편집/수정하실 수 있습니다.")
md_lines.append("> 수정을 마치신 후 **'마크다운 내용 반영해줘'**라고 말씀하시면 HTML 웹 포털에 즉시 자동 빌드됩니다.\n")
md_lines.append("---\n")

unit_counter = 1

for p_idx, part in enumerate(modules):
    md_lines.append(f"## 🌐 {part['part_num']}: {part['title']}")
    md_lines.append(f"- **솔루션/앱**: {part['app_name']}")
    md_lines.append(f"- **앱 키워드**: `{part['app']}`\n")
    
    for s_idx, slide in enumerate(part["slides"]):
        num_str = f"{unit_counter:02d}"
        t = slide["title"].replace("<br>", " ").strip()
        st = slide["subtitle"].replace("<br>", " ").strip()
        
        md_lines.append(f"### [Unit {num_str}] {t}")
        md_lines.append(f"- **배지(태그)**: {slide['badge']}")
        md_lines.append(f"- **부제목**: {st}\n")
        md_lines.append("#### 📝 본문 및 프롬프트 내용")
        
        # Simple HTML tag cleanup for easy reading in markdown while preserving structural intent
        raw_body = slide["body"]
        
        md_lines.append("```html")
        md_lines.append(raw_body.strip())
        md_lines.append("```\n")
        md_lines.append("---\n")
        
        unit_counter += 1

output_md_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/curriculum_content.md"

with open(output_md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Successfully generated master markdown file at: {output_md_path}")
