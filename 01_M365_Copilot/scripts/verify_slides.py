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
    
    print('Checking specific enhanced slides:')
    print('  - Unit 30 (Multi-Ref):', 'Multi-File Reference' in slides[29]['body'])
    print('  - Unit 31 (Rewrite & Table):', 'Rewrite & Table' in slides[30]['body'])
    print('  - Unit 32 (Summary & Q&A):', 'Executive Summary' in slides[31]['body'])
    print('  - Unit 33 (DALL-E 3):', 'DALL-E 3' in slides[32]['body'])
    print('  - Unit 34 (Mobile Audio):', 'Mobile Voice' in slides[33]['body'])
    print('  - Unit 37 (5G SA Topology):', '5G Standalone (SA) Core' in slides[36]['body'])
    print('  - Unit 40 (Brand Template):', 'Brand Template Recognition' in slides[39]['body'])
    print('  - Unit 41 (Agent Mode):', 'Agent Mode Presentation Builder' in slides[40]['body'])
    print('  - Unit 42 (Word to Slide):', 'Word Document to Slide' in slides[41]['body'])
    print('  - Unit 43 (4 Rewrite):', 'Slide Text Refinement' in slides[42]['body'])
    print('  - Unit 44 (Image Laws):', 'BAD CASE' in slides[43]['body'] and 'GOOD CASE' in slides[43]['body'])
    print('  - Unit 45 (40K Words):', 'Large Deck Selective Extraction' in slides[44]['body'])
    print('  - Unit 46 (Mobile Q&A):', 'Mobile Slide Voice Query' in slides[45]['body'])
    print('  - Unit 48 (1-Page ROI):', 'CAPEX' in slides[47]['body'] and '1-Page Executive Summary' in slides[47]['body'])
