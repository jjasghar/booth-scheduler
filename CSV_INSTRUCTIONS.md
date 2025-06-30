# 📊 How to Edit Your Conference Schedule (CSV Format)

The schedule is now stored in a simple CSV file that you can edit with Excel, Google Sheets, or any spreadsheet application!

## 🚀 Quick Start

1. **Open `schedule.csv`** in your preferred spreadsheet app
2. **Edit the data** - add, remove, or modify talks
3. **Save as CSV** - make sure to keep the CSV format
4. **Regenerate** - run `python generate_site.py` to update your website

## 📋 CSV Columns Explained

| Column | Description | Example |
|--------|-------------|---------|
| `date` | Date in YYYY-MM-DD format | `2024-03-15` |
| `day_name` | Display name for the day | `Day 1 - Friday` |
| `time` | Talk start time (24-hour) | `09:00` |
| `duration` | How long the talk lasts | `20 min` |
| `title` | Talk title | `IBM Watson AI in Enterprise` |
| `presenter` | Speaker name(s) | `Sarah Johnson` or `John & Jane` |
| `presenter_title` | Speaker job title | `Senior AI Engineer` |
| `company` | Speaker's company | `IBM Research` |
| `abstract` | Brief talk description | `Learn about Watson AI...` |
| `speaker_image` | URL to speaker photo | `https://example.com/photo.jpg` |
| `speaker_links` | Social/professional links | See format below |

## 🔗 Speaker Links Format

The `speaker_links` column uses this format:
```
Name1:URL1,Name2:URL2,Name3:URL3
```

**Examples:**
- `LinkedIn:https://linkedin.com/in/username`
- `GitHub:https://github.com/username,Blog:https://myblog.com`
- `Portfolio:https://mysite.dev,Twitter:https://twitter.com/handle`

**Supported link types** (get special icons):
- `LinkedIn`, `GitHub`, `Twitter`, `Blog`, `Portfolio`, `Research`

## 🖼️ Speaker Images

You can use:
- **Placeholder images**: `https://via.placeholder.com/150x150/0f62fe/white?text=AB`
- **Direct URLs**: `https://example.com/speaker.jpg`
- **GitHub avatars**: `https://github.com/username.png`

## 📅 Adding Multiple Days

Just add more rows with different dates:
```csv
2024-03-15,Day 1 - Friday,09:00,20 min,...
2024-03-15,Day 1 - Friday,10:00,15 min,...
2024-03-16,Day 2 - Saturday,09:00,20 min,...
```

## ✅ Best Practices

### ✨ **Do This:**
- Keep talk titles concise but descriptive
- Write abstracts that explain value to attendees
- Use consistent time formats (09:00, not 9am)
- Test speaker links before adding them
- Use high-quality speaker photos

### ❌ **Avoid This:**
- Don't use commas in individual fields (breaks CSV format)
- Don't leave required columns empty
- Don't use special characters in URLs without encoding

## 🔧 Common Tasks

### Adding a New Talk
1. Insert a new row in your spreadsheet
2. Fill in all columns
3. Save as CSV
4. Regenerate the site

### Changing Talk Order
- Talks are automatically sorted by date and time
- Just change the time values to reorder

### Removing a Talk
1. Delete the entire row
2. Save as CSV
3. Regenerate the site

## 🆘 Troubleshooting

**Site not updating?**
- Make sure you saved as CSV format
- Check for missing commas or quotes in the CSV
- Run `python generate_site.py` after changes

**Links not working?**
- Verify URLs are complete (include `https://`)
- Check the speaker_links format: `Name:URL,Name:URL`

**Images not showing?**
- Test image URLs in your browser first
- Use placeholder images for testing: 
  `https://via.placeholder.com/150x150/0f62fe/white?text=XY`

## 🎯 Example Row

```csv
2024-03-15,Day 1 - Friday,09:00,20 min,IBM Watson AI in Enterprise,Sarah Johnson,Senior AI Engineer,IBM Research,Learn about Watson AI capabilities and deployment strategies.,https://via.placeholder.com/150x150/0f62fe/white?text=SJ,"LinkedIn:https://linkedin.com/in/sarahjohnson,GitHub:https://github.com/sarahjohnson"
```

---

**💡 Pro Tip:** Use Google Sheets or Excel for easy editing, then export/download as CSV when ready! 