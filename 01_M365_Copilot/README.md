# 📘 01. Microsoft 365 Copilot 통신 엔지니어링 과정

이 폴더는 KT 코어/전송망 엔지니어를 위한 **Microsoft 365 Copilot 실무 마스터 교육 과정**의 실습 리소스(실습 데이터셋, 이미지, 빌드/검증 스크립트)를 관리합니다.

---

## 🖥️ 메인 슬라이드 포털 & 마스터 교재 (Single Source of Truth)
슬라이드 포털과 마스터 교재 텍스트는 프로젝트 **루트 1곳에서만** 관리합니다. 이 폴더에는 중복 사본을 두지 않습니다.

- **메인 슬라이드 포털**: [`../AX_CA_Edu_GHLEE.html`](../AX_CA_Edu_GHLEE.html) / [`../index.html`](../index.html)
- **강의 마스터 기획서**: [`../Copilot_Lecture_Master_Plan.md`](../Copilot_Lecture_Master_Plan.md)
- **52개 유닛 전체 마스터 텍스트**: [`../curriculum_content_master_v2.md`](../curriculum_content_master_v2.md)

---

## 📂 이 폴더의 구성

1. **`curriculum_content_readable.md`** : 52개 유닛 마스터 텍스트의 읽기 편한 축약/정리 버전
2. **`practice_files/`** : 실습 예제 6종 데이터셋 (CSV, MD, Log) — 루트 `practice_files/`와 동일 파일이 동기화되어 있습니다
3. **`scripts/`** : 슬라이드 빌드·검증·텍스트 동기화용 파이썬 유틸리티 모음
4. **`assets/` & `images/`** : 공식 오피스 브랜드 아이콘, 3D Copilot 이미지, 아키텍처 다이어그램

---

## ⌨️ 슬라이드 뷰어 단축키
| 단축키 | 동작 설명 |
| :--- | :--- |
| **`Space` / `→`** | 다음 슬라이드로 이동 |
| **`Shift+Space` / `←` / `Backspace`** | 이전 슬라이드로 이동 |
| **`B`** | 좌측 슬라이드 목록 사이드바 열기 / 닫기 |
| **`V`** | 단일 슬라이드 뷰 ↔ 전체 연속 포털 뷰 전환 |
| **`F`** | 전체화면 모드 토글 |

---

## 🛡️ 엔터프라이즈 보안 원칙
- **Enterprise Data Protection (EDP)** 준수: 모든 실습 및 프롬프트는 사내 데이터 보안 격리 환경에서 진행되며 AI 모델 학습에 사용되지 않습니다.
