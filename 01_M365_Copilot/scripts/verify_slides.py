# -*- coding: utf-8 -*-
import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('AX_CA_Edu_GHLEE.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
articles = soup.find_all('article')
print(f'Portal View articles: {len(articles)}')

match = re.search(r'const slidesData = (\[.*?\]);\s*let currentSlideIndex', content, re.DOTALL)
if match:
    slides = json.loads(match.group(1), strict=False)
    print(f'JS slidesData items: {len(slides)}')
    
    # Check chapters
    chapters = sorted(list(set(s['full_chapter_name'] for s in slides)))
    print(f'Total distinct chapters ({len(chapters)}):')
    for ch in chapters:
        count = sum(1 for s in slides if s['full_chapter_name'] == ch)
        print(f'  - {ch} (Total {count} units)')
    
    # Check prompt cards count
    prompt_count = sum(1 for s in slides if 'copilot-prompt-card' in s['body'])
    print(f'Slides with Copilot Prompt Cards: {prompt_count} / {len(slides)}')
    
    def get_slide_by_num(num):
        for s in slides:
            if s['num'] == num:
                return s
        return None

    print('\nChecking Chapter Divider & TOC Slides:')
    for num in ['COVER', 'INDEX', 'CH 01', 'CH 02', 'CH 03', 'CH 04']:
        s = get_slide_by_num(num)
        print(f'  - {num:7s}: Title="{s["title"][:35]}...", Badge="{s["badge"]}"')

    print('\nChecking Key Hands-on Units:')
    for num in ['24', '26', '30', '31', '35', '36', '42', '47', '48', '50']:
        s = get_slide_by_num(num)
        if s:
            has_prompt = 'copilot-prompt-card' in s['body']
            print(f'  - Unit {num:2s}: {s["title"][:35]}... (Prompt Card: {has_prompt})')
