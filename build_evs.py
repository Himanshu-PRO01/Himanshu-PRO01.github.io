import json
import re
import os

transcript_path = r"C:\Users\Ram Kesh\.gemini\antigravity-ide\brain\f6cb4223-e072-439e-938a-d4ab1e05032c\.system_generated\logs\transcript_full.jsonl"

pdf_content = ""

with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Process from the end to find the relevant user input
for line in reversed(lines):
    try:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT' and '==Start of PDF==' in data.get('content', ''):
            content = data['content']
            blocks = re.findall(r'==Start of PDF==(.*?)(?:==End of PDF==)', content, re.DOTALL)
            if blocks:
                pdf_content = "\n".join(blocks)
                break
    except Exception as e:
        continue

# Clean up OCR and screenshot markers
cleaned_content = re.sub(r'==Screenshot for page \d+==\n(\[Image.*?\]\n)?', '', pdf_content, flags=re.DOTALL)
cleaned_content = re.sub(r'==Start of OCR for page \d+==\n', '', cleaned_content, flags=re.DOTALL)
cleaned_content = re.sub(r'==End of OCR for page \d+==\n', '', cleaned_content, flags=re.DOTALL)

# HTML Template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EVS Notes | EngiNotes</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <link rel="stylesheet" href="style.css">
    <style>
        .notes-page {
            background-color: var(--bg-dark);
            min-height: 100vh;
            padding-top: 100px;
        }
        .notes-content-wrapper {
            max-width: 900px;
            margin: 0 auto;
            background: var(--bg-card);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 3rem;
            color: var(--text-main);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            margin-bottom: 4rem;
        }
        .header-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--glass-border);
            padding-bottom: 1rem;
        }
        .header-actions h1 {
            color: var(--accent-cyan);
            font-size: 2rem;
        }
        .raw-text {
            white-space: pre-wrap;
            font-family: inherit;
            line-height: 1.6;
            color: #cbd5e1;
            font-size: 0.95rem;
        }
        
        /* Loading overlay for PDF generation */
        #loading-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 9999;
            color: white;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            flex-direction: column;
            gap: 1rem;
        }
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

    <div id="loading-overlay">
        <i data-lucide="loader" class="pulse-dot" style="width: 48px; height: 48px; animation: spin 2s linear infinite;"></i>
        Generating PDF... Please wait (this may take a minute)
    </div>

    <div class="section-container">
        <div class="notes-content-wrapper">
            <div class="header-actions">
                <h1>Environment & Ecology (EVS)</h1>
                <button id="download-btn" class="primary-btn glow-btn"><i data-lucide="download"></i> Download as PDF</button>
            </div>
            <div id="pdf-content" style="padding: 20px;">
                <div class="raw-text">
""" + cleaned_content.replace('<', '&lt;').replace('>', '&gt;') + """
                </div>
            </div>
        </div>
    </div>

    <script>
        lucide.createIcons();
        
        document.getElementById('download-btn').addEventListener('click', () => {
            const element = document.getElementById('pdf-content');
            const overlay = document.getElementById('loading-overlay');
            overlay.style.display = 'flex';
            
            // Temporary styling for PDF generation
            element.style.background = '#ffffff';
            element.style.color = '#000000';
            const rawText = element.querySelector('.raw-text');
            rawText.style.color = '#000000';
            
            const opt = {
              margin:       0.5,
              filename:     'EVS_Notes.pdf',
              image:        { type: 'jpeg', quality: 0.98 },
              html2canvas:  { scale: 2 },
              jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
            };

            html2pdf().set(opt).from(element).save().then(() => {
                // Restore styles
                element.style.background = '';
                element.style.color = '';
                rawText.style.color = '#cbd5e1';
                overlay.style.display = 'none';
            });
        });
    </script>
</body>
</html>
"""

with open("evs.html", 'w', encoding='utf-8') as f:
    f.write(html_template)
    
print("evs.html created successfully!")
