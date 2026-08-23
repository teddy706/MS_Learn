# -*- coding: utf-8 -*-
import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')

# Read slidesData from AX_CA_Edu_GHLEE.html
with open('AX_CA_Edu_GHLEE.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const slidesData = (\[.*?\]);\s*let currentSlideIndex', content, re.DOTALL)
if not match:
    print('Failed to load slides')
    sys.exit(1)

slides = json.loads(match.group(1), strict=False)

md_lines = [
    '# KT AX | Microsoft 365 Copilot 통신 엔지니어링 표준 교재 (마스터 텍스트 & 실습 가이드)',
    '',
    '> **문서 버전:** 2026 Final Master Edition (52 Units Complete)  ',
    '> **작성자:** 이광희  ',
    '> **목적:** 52개 슬라이드 전체의 세부 텍스트 검토/수정 및 실습 예제 파일(Sample Dataset) 연계 가이드',
    '',
    '---',
    '',
    '## 📂 실습 예제 파일 디렉토리 안내 (`practice_files/`)',
    '',
    '| 파일명 | 형식 | 설명 및 용도 | 연계 유닛 |',
    '|---|---|---|---|',
    '| `KT_5G_수도권_기지국_품질지표_2026.csv` | CSV/Excel | 수도권 주요 50개 국사 트래픽, PRB 사용률, 드롭률 | Unit 07, 20, 24, 25, 29, 30 |',
    '| `KT_코어망_백본_트래픽_이상로그_2026.csv` | CSV/Excel | 라우터별 대역폭, 패킷 손실, 지연시간 통계 | Unit 26, 35 |',
    '| `KT_5G_설비투자_CAPEX_예산안_2026.csv` | CSV/Excel | 코어망/무선망 증설 비용, 운용비 절감액, ROI | Unit 27, 36, 48 |',
    '| `KT_2026_5G망_현대화_기술보고서.md` | Word/MD | 15페이지 분량의 5G 네트워크 고도화 보고서 초안 | Unit 07, 30, 39, 42, 47 |',
    '| `KT_L3스위치_비상점검_표준작업절차서_SOP.md` | Word/MD | L3 스위치 과부하 시 단계별 비상 복구 절차서 | Unit 30, 31, 35 |',
    '| `KT_Cisco_Nokia_TAC_장애로그.txt` | Text/Log | BGP 플래핑 및 ASIC 라인 에러 시스로그 원본 | Unit 17 |',
    '',
    '---',
    '',
    '## 📑 52개 슬라이드 마스터 텍스트 & 실습 가이드 전수 목록',
    ''
]

current_chap = None
for i, s in enumerate(slides):
    chap = s['full_chapter_name']
    if chap != current_chap:
        current_chap = chap
        md_lines.append(f'## 🌐 {chap}\n')
    
    md_lines.append(f'### [Unit {s["num"]}] {s["title"]}')
    md_lines.append(f'- **소속 챕터:** {s["full_chapter_name"]}')
    md_lines.append(f'- **도구 / 영역:** `{s["app_name"]}`')
    md_lines.append(f'- **핵심 배지:** `{s["badge"]}`')
    md_lines.append(f'- **부제목(Subtitle):** {s["subtitle"]}')
    md_lines.append('')
    md_lines.append('#### 📝 슬라이드 본문 구조 및 핵심 내용')
    
    # Clean tags from body for markdown view
    clean_body = re.sub(r'<button.*?</button>', '', s['body'], flags=re.DOTALL)
    clean_body = re.sub(r'<svg.*?</svg>', '', clean_body, flags=re.DOTALL)
    clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
    clean_body = re.sub(r'\s+', ' ', clean_body).strip()
    md_lines.append(clean_body)
    md_lines.append('')
    md_lines.append('---')
    md_lines.append('')

full_md = '\n'.join(md_lines)

with open('curriculum_content_master_v2.md', 'w', encoding='utf-8') as f:
    f.write(full_md)

with open('01_M365_Copilot/curriculum_content_master_v2.md', 'w', encoding='utf-8') as f:
    f.write(full_md)

print('curriculum_content_master_v2.md successfully synced!')
