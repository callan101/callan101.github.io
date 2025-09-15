#!/usr/bin/env python3
"""
Simple RSS Post Generator
Converts markdown files to HTML, updates RSS index, and updates RSS feed.
Usage: python3 generate_post_simple.py <markdown_file>

File naming: 2025-08-29_my_post.md
Title: First # heading in markdown
Date: From filename (YYYY-MM-DD)
"""

import sys
import re
import markdown
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom

def parse_markdown_file(md_file_path):
    """Parse markdown file - title from first # heading, date from filename"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from first # heading
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else 'Untitled'
    
    # Extract date from filename (YYYY-MM-DD)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', md_file_path.name)
    date = date_match.group(1) if date_match else datetime.now().strftime('%Y-%m-%d')
    
    # Convert markdown to HTML
    html_content = markdown.markdown(content, extensions=['fenced_code'])
    
    return {
        'title': title,
        'date': date,
        'content': html_content,
        'filename': Path(md_file_path).stem
    }

def create_html_file(post_data, output_dir):
    """Create HTML file from post data"""
    html_filename = f"{post_data['filename']}.html"
    html_path = output_dir / html_filename
    
    html_template = f"""<!DOCTYPE html>

<head>
    <title>{post_data['title']}</title>
    <meta charset="UTF-8">
    <link rel="icon" href="../favicon.png" />
    <meta name="description" content="{post_data['title']}">
    <meta name="author" content="Callan Sheldon">
    <link rel="stylesheet" href="../style.css">
    <style>
        .content {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2em;
            line-height: 1.6;
        }}
        .content h1 {{
            border-bottom: 1px solid #444;
            padding-bottom: 0.5em;
        }}
        .content h2 {{
            margin-top: 2em;
            color: #aaa;
        }}
        .content code {{
            background: #222;
            padding: 0.2em 0.4em;
            border-radius: 3px;
        }}
        .content pre {{
            background: #222;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
        }}
        .content pre code {{
            background: none;
            padding: 0;
        }}
        .content ul, .content ol {{
            padding-left: 2em;
        }}
        .content blockquote {{
            border-left: 3px solid #444;
            margin: 1em 0;
            padding-left: 1em;
            color: #aaa;
        }}
    </style>
</head>

<body>
    <div class="container">
        <div class="right-side">
            <div class="content">
                <h1>{post_data['title']}</h1>
                <p><em>{post_data['date']}</em></p>
                <hr>
                {post_data['content']}
            </div>
        </div>
    </div>
    <script src="../main.js"></script>
</body>

</html>"""
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"Created HTML file: {html_path}")
    return html_filename

def update_rss_index(post_data, html_filename, index_path):
    """Update the RSS index page with new post"""
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the table body
    table_body_match = re.search(r'(<tbody>)(.*?)(</tbody>)', content, re.DOTALL)
    if not table_body_match:
        print("Could not find table body in index.html")
        return
    
    # Create new row
    new_row = f"""
							<tr>
								<td>
									<a href="{html_filename}">{post_data['title']}</a>
									<em>{post_data['date']}</em>
								</td>
							</tr>"""
    
    # Add new row at the beginning (newest first)
    new_content = re.sub(r'(<tbody>)(.*?)(</tbody>)', r'\1' + new_row + r'\2' + r'\3', content, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated RSS index: {index_path}")

def update_rss_feed(post_data, html_filename, feed_path):
    """Update the RSS feed with new post"""
    try:
        tree = ET.parse(feed_path)
        root = tree.getroot()
    except FileNotFoundError:
        # Create new feed if it doesn't exist
        root = ET.Element('feed', xmlns="http://www.w3.org/2005/Atom")
        ET.SubElement(root, 'id').text = 'https://callan101.com/feed.xml'
        ET.SubElement(root, 'title').text = "Callan's cool blog"
        ET.SubElement(root, 'generator').text = "Callan's Simple RSS Generator"
        
        # Add author
        author = ET.SubElement(root, 'author')
        ET.SubElement(author, 'name').text = 'Callan'
        ET.SubElement(author, 'email').text = 'hello@callan101.com'
        ET.SubElement(author, 'uri').text = 'https://callan101.com'
        
        # Add feed links
        ET.SubElement(root, 'link', rel="alternate", href="https://callan101.com/")
        ET.SubElement(root, 'subtitle').text = "Callan's cool blog"
        ET.SubElement(root, 'rights').text = "All rights reserved 2024, Callan."
    
    # Update feed timestamp
    for updated_elem in root.findall('updated'):
        updated_elem.text = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
        break
    
    # Create new entry
    entry = ET.SubElement(root, 'entry')
    ET.SubElement(entry, 'title', type="html").text = f"<![CDATA[{post_data['title']}]]>"
    ET.SubElement(entry, 'id').text = f"https://callan101.com/rss/{html_filename}"
    ET.SubElement(entry, 'link', href=f"https://callan101.com/rss/{html_filename}")
    ET.SubElement(entry, 'updated').text = f"{post_data['date']}T00:00:00.000Z"
    ET.SubElement(entry, 'summary', type="html").text = f"<![CDATA[{post_data['title']}]]>"
    ET.SubElement(entry, 'content', type="html").text = f"<![CDATA[{post_data['content']}]]>"
    
    # Add entry author
    entry_author = ET.SubElement(entry, 'author')
    ET.SubElement(entry_author, 'name').text = 'Callan'
    ET.SubElement(entry_author, 'email').text = 'hello@callan101.com'
    ET.SubElement(entry_author, 'uri').text = 'https://callan101.com/'
    
    # Write updated feed
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
    with open(feed_path, 'w', encoding='utf-8') as f:
        f.write(xml_str)
    
    print(f"Updated RSS feed: {feed_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_post_simple.py <markdown_file>")
        print("Example: python3 generate_post_simple.py 2025-08-29_my_post.md")
        print("\nFile naming: YYYY-MM-DD_title.md")
        print("Title: First # heading in markdown")
        print("Date: From filename")
        sys.exit(1)
    
    md_filename = sys.argv[1]
    md_path = Path('source') / md_filename
    
    if not md_path.exists():
        print(f"Error: Markdown file '{md_path}' not found")
        sys.exit(1)
    
    # Parse markdown file
    print(f"Processing {md_path}...")
    post_data = parse_markdown_file(md_path)
    
    # Create HTML file in rss directory
    output_dir = Path('.')
    html_filename = create_html_file(post_data, output_dir)
    
    # Update RSS index
    index_path = Path('index.html')
    update_rss_index(post_data, html_filename, index_path)
    
    # Update RSS feed
    feed_path = Path('../feed.xml')
    update_rss_feed(post_data, html_filename, feed_path)
    
    print(f"\n✅ Successfully processed '{md_filename}'")
    print(f"📄 HTML file: {html_filename}")
    print(f"📝 Updated RSS index and feed")

if __name__ == "__main__":
    main()
