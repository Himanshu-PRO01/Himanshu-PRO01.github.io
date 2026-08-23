import os
import re

base_dir = r"c:\Users\Ram Kesh\Downloads\notes-main"
hello_dir = os.path.join(base_dir, "hello")

# Define subjects and their corresponding HTML files and folder names
subjects = {
    "Physics": {"folder": "Physics", "file": "physics.html", "title": "Physics Notes"},
    "Chemistry": {"folder": "Chemistry", "file": "chemistry.html", "title": "Chemistry Notes"},
    "EE": {"folder": "Electrical", "file": "ee.html", "title": "Basic of Electrical Engineering"},
    "Electronics": {"folder": "Electronics", "file": "electronics.html", "title": "Basic of Electronics Engineering"},
    "Mechanical": {"folder": "Mechanical", "file": "mechanical.html", "title": "Basic of Mechanical Engineering"},
    "Soft Skills": {"folder": "Soft Skills", "file": "soft_skills.html", "title": "Soft Skills"},
    "PPS": {"folder": "PPS", "file": "pps.html", "title": "PPS Notes"},
    "EVs": {"folder": "EVS", "file": "evs.html", "title": "Environment & Ecology (EVS)"},
}

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | EngiNotes</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="style.css">
    <style>
        .notes-page {{
            background-color: var(--bg-dark);
            min-height: 100vh;
            padding-top: 100px;
        }}
        .notes-content-wrapper {{
            max-width: 900px;
            margin: 0 auto;
            background: var(--bg-card);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 3rem;
            color: var(--text-main);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            margin-bottom: 4rem;
        }}
        .header-actions {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--glass-border);
            padding-bottom: 1rem;
        }}
        .header-actions h1 {{
            color: var(--accent-cyan);
            font-size: 2rem;
        }}
        .pdf-list {{
            list-style: none;
            padding: 0;
        }}
        .pdf-list li {{
            margin-bottom: 1rem;
            background: rgba(255, 255, 255, 0.05);
            padding: 1rem;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        .pdf-list li:hover {{
            background: rgba(255, 255, 255, 0.1);
            border-color: var(--accent-cyan);
        }}
        .pdf-name {{
            font-size: 1.1rem;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .pdf-actions a {{
            color: var(--bg-dark);
            background: var(--accent-cyan);
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.3s ease;
        }}
        .pdf-actions a:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 240, 255, 0.3);
        }}
        .empty-state {{
            text-align: center;
            padding: 3rem;
            color: var(--text-muted);
        }}
    </style>
</head>
<body class="notes-page">
    <nav class="navbar scrolled">
        <div class="nav-container">
            <div class="nav-brand">
                <i data-lucide="book-open" class="brand-icon"></i> EngiNotes
            </div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="notes.html" class="active">Notes</a></li>
            </ul>
        </div>
    </nav>

    <div class="section-container">
        <div class="notes-content-wrapper">
            <div class="header-actions">
                <h1>{title}</h1>
            </div>
            <div id="pdf-content">
                {content}
            </div>
        </div>
    </div>

    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

for subj, data in subjects.items():
    subj_folder = os.path.join(hello_dir, data["folder"])
    pdfs = []
    if os.path.exists(subj_folder):
        for f in os.listdir(subj_folder):
            if f.lower().endswith('.pdf'):
                pdfs.append(f)
    
    content = ""
    if pdfs:
        content += '<ul class="pdf-list">\n'
        for pdf in pdfs:
            pdf_path = f"hello/{data['folder']}/{pdf}"
            # URL encode the path to handle spaces
            import urllib.parse
            pdf_url = urllib.parse.quote(pdf_path)
            content += f'                    <li>\n'
            content += f'                        <div class="pdf-name"><i data-lucide="file-text"></i> {pdf}</div>\n'
            content += f'                        <div class="pdf-actions">\n'
            content += f'                            <a href="{pdf_url}" target="_blank"><i data-lucide="external-link"></i> View</a>\n'
            content += f'                            <a href="{pdf_url}" download><i data-lucide="download"></i> Download</a>\n'
            content += f'                        </div>\n'
            content += f'                    </li>\n'
        content += '                </ul>'
    else:
        content = '<div class="empty-state">No PDF notes available yet for this subject.</div>'
        
    html_content = html_template.format(title=data["title"], content=content)
    
    with open(os.path.join(base_dir, data["file"]), "w", encoding="utf-8") as f:
        f.write(html_content)

print("HTML pages generated successfully.")
