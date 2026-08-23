file_paths = [
    "/Users/gwanghee/Documents/110_Github/MS_Learn/M365_Copilot_Telecom_Master.html",
    "/Users/gwanghee/Documents/110_Github/MS_Learn/index.html"
]

for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove the subtext and separator
    target_subtext_1 = '<span class="text-slate-300 text-xs">|</span>'
    target_subtext_2 = '<span class="text-xs md:text-sm text-slate-600 font-bold hidden sm:inline uppercase tracking-wider">공식 솔루션 시스템 (초고화질 벡터)</span>'
    
    content = content.replace(target_subtext_1, "")
    content = content.replace(target_subtext_2, "")

    # Also clean up any variation
    content = content.replace("공식 솔루션 시스템 (초고화질 벡터)", "")
    content = content.replace("공식 솔루션 브랜드 시스템", "")
    content = content.replace("통신·네트워크 실무 마스터 포털", "")

    # Ensure whitespace-nowrap on all header elements
    content = content.replace(
        '<header class="no-print h-14 bg-white/95 backdrop-blur-md border-b border-slate-200 text-slate-800 flex items-center justify-between px-4 z-40 shrink-0 shadow-xs">',
        '<header class="no-print h-14 bg-white/95 backdrop-blur-md border-b border-slate-200 text-slate-800 flex items-center justify-between px-4 z-40 shrink-0 shadow-xs whitespace-nowrap select-none">'
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully cleaned up header subtext and prevented text wrapping.")
