import re

loc = {}
with open("generate_m365_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
modules = loc["modules"]

def html_to_readable_text(html_str):
    # Convert blockquotes to markdown blockquotes
    html_str = re.sub(r'<blockquote>\s*<p[^>]*>(.*?)</p>\s*</blockquote>', r'\n> 💬 **[실전 Copilot 프롬프트]**\n> \1\n', html_str, flags=re.DOTALL)
    
    # Convert spans / divs with headers
    html_str = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n##### \1\n', html_str)
    
    # Strip remaining HTML tags for clean text reading
    clean = re.sub(r'<[^>]+>', ' ', html_str)
    clean = re.sub(r'[ \t]+', ' ', clean)
    clean = re.sub(r'\n\s*\n+', '\n\n', clean)
    return clean.strip()

md_lines = []
md_lines.append("# 📘 Microsoft 365 Copilot 통신·네트워크 엔지니어링 실무 마스터 커리큘럼")
md_lines.append("\n> **설명**: 33개 전체 유닛의 교육 내용, 실무 시나리오, 실전 프롬프트가 읽기 편한 마크다운 형식으로 정리되어 있습니다.\n")
md_lines.append("---\n")

unit_counter = 1

for p_idx, part in enumerate(modules):
    md_lines.append(f"## 🌐 {part['part_num']}: {part['title']}")
    md_lines.append(f"- **담당 솔루션**: {part['app_name']}\n")
    
    for s_idx, slide in enumerate(part["slides"]):
        num_str = f"{unit_counter:02d}"
        t = slide["title"].replace("<br>", " ").strip()
        st = slide["subtitle"].replace("<br>", " ").strip()
        
        md_lines.append(f"### [Unit {num_str}] {t}")
        md_lines.append(f"- **분류 태그**: `{slide['badge']}`")
        md_lines.append(f"- **핵심 부제**: {st}\n")
        
        # Read readable content
        readable_text = html_to_readable_text(slide["body"])
        md_lines.append("#### 📋 세부 학습 내용 및 실무 시나리오")
        md_lines.append(readable_text)
        md_lines.append("\n" + ("=" * 60) + "\n")
        
        unit_counter += 1

output_clean_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/curriculum_content_readable.md"

with open(output_clean_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Successfully generated clean readable markdown at: {output_clean_path}")
