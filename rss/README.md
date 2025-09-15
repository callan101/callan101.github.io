# RSS Post System (Simplified)

This directory contains the automated RSS post system for Callan's website.

## How it works

1. **Write posts in Markdown** in the `source/` folder
2. **Run the script** to convert to HTML and update everything
3. **Everything is automated** - no more manual XML editing!

## File Structure

```
rss/
├── source/                    # Write your markdown posts here
│   ├── 2025-08-29_simple_test.md
│   └── your_new_post.md
├── generate_post_simple.py    # The simplified automation script
├── index.html               # RSS posts index (auto-updated)
├── README.md               # This file
└── *.html                  # Generated HTML posts
```

## Creating a New Post

### 1. Create a Markdown file

Create a new `.md` file in the `source/` folder with this format:

**Filename format**: `YYYY-MM-DD_title.md`
**Example**: `2025-08-29_my_post.md`

```markdown
# My Post Title

Your content here in Markdown format.

## Features

- **Bold text** and *italic text*
- [Links](https://example.com)
- `Code snippets`
- Lists and more!

## Code blocks

```python
def hello_world():
    print("Hello, world!")
```

That's it! No YAML frontmatter needed.
```

### 2. Run the script

```bash
cd rss
python3 generate_post_simple.py your_post_filename.md
```

### 3. That's it!

The script will automatically:
- ✅ Extract title from first `#` heading
- ✅ Extract date from filename
- ✅ Convert Markdown to HTML
- ✅ Create the HTML file in the `rss/` folder
- ✅ Update the RSS posts index page
- ✅ Update the main RSS feed (`feed.xml`)

## Features

- **No YAML required**: Just write markdown normally
- **Simple filename format**: `YYYY-MM-DD_title.md`
- **Automatic title extraction**: From first `#` heading
- **Automatic date extraction**: From filename
- **Markdown support**: Write in Markdown, get beautiful HTML
- **Automatic styling**: Posts use your site's CSS theme
- **RSS integration**: Updates both the index and feed automatically
- **Code highlighting**: Syntax highlighting for code blocks
- **Responsive design**: Works on desktop and mobile

## Requirements

Install the required Python packages:

```bash
pip3 install --break-system-packages markdown
```

**Note**: No YAML package needed anymore!

## Example

1. Create `source/2025-08-30_my_post.md`:
```markdown
# My New Post

This is the content of my post...
```

2. Run: `python3 generate_post_simple.py 2025-08-30_my_post.md`

3. Visit: `https://callan101.com/rss/` to see your post!

## File Naming Convention

- **Date**: `YYYY-MM-DD` (required)
- **Title**: Use underscores for spaces
- **Examples**:
  - `2025-08-29_my_post.md` → Title: "My Post", Date: 2025-08-29
  - `2025-08-30_another_post.md` → Title: "Another Post", Date: 2025-08-30
  - `2025-08-31_this_is_a_long_title.md` → Title: "This Is A Long Title", Date: 2025-08-31

## Troubleshooting

- **Script not found**: Make sure you're in the `rss/` directory
- **Import errors**: Install markdown package with pip
- **File not found**: Check that your markdown file exists in `source/`
- **Permission errors**: Make sure the script is executable: `chmod +x generate_post_simple.py`
- **Title not found**: Make sure your markdown file starts with a `#` heading
- **Date not found**: Make sure filename starts with `YYYY-MM-DD_`
