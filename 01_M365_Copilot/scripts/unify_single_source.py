# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

# 1. Remove legacy duplicate files
files_to_remove = [
    'M365_Copilot_Telecom_Master.html',
    '01_M365_Copilot/M365_Copilot_Telecom_Master.html',
    '01_M365_Copilot/AX_CA_Edu_GHLEE.html'
]

for f in files_to_remove:
    if os.path.exists(f):
        os.remove(f)
        print(f'Removed redundant file: {f}')

# 2. Write lightweight index.html redirector
redirect_html = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=AX_CA_Edu_GHLEE.html">
    <title>KT AX | Microsoft 365 Copilot 보조교재</title>
    <script>
        window.location.replace('AX_CA_Edu_GHLEE.html');
    </script>
</head>
<body style="font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; background-color: #F4F6FA;">
    <div style="text-align: center; background: white; padding: 32px 48px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border: 1px solid #E4E7EC;">
        <h2 style="margin: 0 0 12px; color: #111317;">M365 Copilot 보조교재로 이동 중...</h2>
        <p style="margin: 0 0 20px; color: #525A68; font-size: 14px;">자동으로 이동하지 않으면 아래 링크를 클릭하세요.</p>
        <a href="AX_CA_Edu_GHLEE.html" style="display: inline-block; padding: 10px 24px; background: #E60000; color: white; text-decoration: none; border-radius: 8px; font-weight: bold;">슬라이드 열기 ➔</a>
    </div>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(redirect_html)

print('Root index.html replaced with clean, lightweight auto-redirector.')

# 3. Create 01_M365_Copilot/README.md linking to master
m365_readme = """# 📘 01. Microsoft 365 Copilot 통신 엔지니어링 과정

이 폴더는 KT 통신/네트워크 엔지니어를 위한 **Microsoft 365 Copilot 실무 과정**의 핵심 교재 및 실습 리소스를 관리합니다.

---

## 🖥️ 메인 슬라이드 포털 (Single Source of Truth)
- **메인 슬라이드 파일**: [`../AX_CA_Edu_GHLEE.html`](../AX_CA_Edu_GHLEE.html)
- 모든 슬라이드 수정 및 관리는 프로젝트 루트의 `AX_CA_Edu_GHLEE.html` 단 1개의 파일에서 이루어집니다.

---

## 📂 디렉토리 구성

1. **`curriculum_content_master_v2.md`** : 52개 유닛 전체 마스터 텍스트 & 실습 가이드
2. **`Copilot_Lecture_Master_Plan.md`** : 7시간 집중 과정 강의 마스터 기획서
3. **`practice_files/`** : 실습 예제 6종 데이터셋 (CSV, MD, Log)
4. **`scripts/`** : 슬라이드 검증 및 텍스트 동기화 유틸리티
5. **`assets/` & `images/`** : 공식 오피스 브랜드 아이콘 및 아키텍처 다이어그램
"""

with open('01_M365_Copilot/README.md', 'w', encoding='utf-8') as f:
    f.write(m365_readme)

print('01_M365_Copilot/README.md created.')
