import json
import re

loc = {}
with open("rebuild_standard_curriculum_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
standard_chapters = loc["standard_chapters"]

def html_to_clean(html_str):
    html_str = re.sub(r'<blockquote>\s*<p[^>]*>(.*?)</p>\s*</blockquote>', r'\n> 💬 **[실전 Copilot 프롬프트]**\n> \1\n', html_str, flags=re.DOTALL)
    html_str = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n##### \1\n', html_str)
    clean = re.sub(r'<[^>]+>', ' ', html_str)
    clean = re.sub(r'[ \t]+', ' ', clean)
    clean = re.sub(r'\n\s*\n+', '\n\n', clean)
    return clean.strip()

md_lines = []
md_lines.append("# 📘 Microsoft 365 Copilot 표준 교육과정 커리큘럼")
md_lines.append("\n> **표준 4대 챕터 구성**: 실제 표준 교안에 맞추어 4개 핵심 챕터 및 학습 도구별 실무 플레이북으로 재구성된 공식 마스터 문서입니다.\n")
md_lines.append("---\n")

unit_counter = 1

for c_idx, chap in enumerate(standard_chapters):
    md_lines.append(f"## 🌐 {chap['chapter_num']}. {chap['title']}")
    md_lines.append(f"- **학습 도구/내용**: `{chap['tools']}`\n")
    
    for u_idx, u in enumerate(chap["units"]):
        num_str = f"{unit_counter:02d}"
        md_lines.append(f"### [Unit {num_str}] {u['title']}")
        md_lines.append(f"- **배지(태그)**: `{u['badge']}`")
        md_lines.append(f"- **핵심 부제**: {u['subtitle']}\n")
        
        readable_text = html_to_clean(u["body"])
        md_lines.append("#### 📋 세부 학습 내용 및 실전 프롬프트")
        md_lines.append(readable_text)
        md_lines.append("\n" + ("=" * 60) + "\n")
        
        unit_counter += 1

output_clean_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/curriculum_content_readable.md"
with open(output_clean_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Successfully updated {output_clean_path}")
