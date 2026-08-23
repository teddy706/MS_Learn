file_paths = [
    "/Users/gwanghee/Documents/110_Github/MS_Learn/M365_Copilot_Telecom_Master.html",
    "/Users/gwanghee/Documents/110_Github/MS_Learn/index.html"
]

for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove Font Switcher block
    font_block = """            <!-- Font Switcher -->
            <div class="flex items-center bg-slate-100 rounded-full px-2.5 py-1 border border-slate-200 text-xs font-bold text-slate-700 space-x-1.5 shadow-2xs">
                <span>🔤</span>
                <select id="fontSelect" onchange="changeFontFamily(this.value)" class="bg-transparent text-slate-800 font-semibold focus:outline-none cursor-pointer text-xs">
                    <option value="font-pretendard" selected>Pretendard (추천 ⭐)</option>
                    <option value="font-suit">SUIT (테크 감성)</option>
                    <option value="font-noto">Noto Sans KR (본고딕)</option>
                    <option value="font-ibm">IBM Plex Sans (엔지니어링)</option>
                </select>
            </div>"""
    content = content.replace(font_block, "")

    # 2. Remove Search Trigger block
    search_block = """            <!-- Search Trigger -->
            <div class="relative hidden md:block">
                <input type="text" id="searchInput" placeholder="솔루션 / 프롬프트 검색..." class="bg-slate-100/90 border border-slate-200 rounded-full px-3.5 py-1 text-xs md:text-sm text-slate-700 placeholder-slate-400 focus:outline-none focus:border-indigo-500 focus:bg-white w-44 transition-all">
            </div>"""
    content = content.replace(search_block, "")

    # 3. Clean up JS functions changeFontFamily and searchInput event
    js_cleanup_target = """        function changeFontFamily(fontClass) {
            const root = document.getElementById('htmlRoot');
            root.classList.remove('font-pretendard', 'font-noto', 'font-suit', 'font-ibm');
            root.classList.add(fontClass);
        }"""
    content = content.replace(js_cleanup_target, "")

    search_js_target = """        // Search Filter
        document.getElementById('searchInput').addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.slide-nav-item').forEach((item, idx) => {
                const s = slidesData[idx];
                const text = (s.title + ' ' + s.subtitle + ' ' + s.badge + ' ' + s.app_name).toLowerCase();
                if (text.includes(query)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });"""
    content = content.replace(search_js_target, "")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully removed search bar and font switcher from both HTML files.")
