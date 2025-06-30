# 🎤 Booth Scheduler

A beautiful, responsive conference booth scheduling system that automatically generates a static website from CSV and YAML files. Perfect for tech conferences, meetups, and events!

## ✨ Features

- 📱 **Responsive Design**: Looks great on phones, tablets, and laptops
- 🗓️ **Day Navigation**: Sticky navigation bar to jump between conference days
- 🔄 **Auto-Deploy**: Changes to schedule automatically update the website
- 📊 **QR Codes**: Generate QR codes for speaker links on-the-fly
- 🎨 **Modern UI**: Clean, professional design with smooth animations
- 🚀 **GitHub Pages**: Free hosting with custom domain support
- 📝 **CSV Editing**: Edit schedule in Excel/Google Sheets (non-technical friendly)
- 🖼️ **Logo Support**: Add your organization's logo to the header
- 🔧 **Configurable**: Show/hide features like duration badges and format info

## 🚀 Quick Start

### 1. Setup Your Repository

1. **Fork or clone this repository**
2. **Enable GitHub Pages**:
   - Go to your repository settings
   - Scroll to "Pages" section
   - Set source to "GitHub Actions"

### 2. Edit Your Configuration & Schedule

**Configuration**: Edit `config.yaml` with your conference details:
```yaml
conference:
  name: "Your Conference Name"
  booth_name: "Your Booth Name"
  location: "Hall A, Booth 123"
  description: "Your booth description"
```

**Schedule**: Edit `schedule.csv` with your talks (use Excel/Google Sheets!):
```csv
date,day_name,time,duration,title,presenter,presenter_title,company,abstract,speaker_image,speaker_links
2024-03-15,Day 1,09:00,20 min,Your Talk Title,Speaker Name,Job Title,Company,...
```

### 3. Automatic Deployment

🎉 **That's it!** When you commit changes to `config.yaml` or `schedule.csv`, GitHub Actions will automatically:
- Generate a new version of your website
- Deploy it to GitHub Pages
- Your site will be live at: `https://yourusername.github.io/your-repo-name`

## 📝 Editing Your Schedule

### 🎯 **Two-File System**
- **`config.yaml`** - Conference settings (edit once)
- **`schedule.csv`** - Talk schedule (edit frequently in Excel/Sheets)

### Conference Information (`config.yaml`)

```yaml
conference:
  name: "Tech Conference 2024"           # Conference name
  booth_name: "Innovation Booth"         # Your booth name
  location: "Hall A, Booth 123"          # Physical location
  description: "Brief description"       # Optional description

# Website settings
website:
  title_suffix: "Schedule"
  footer_text: "Schedule generated with ❤️ using Python"
  show_duration_badges: true             # Show duration badges next to times
  show_format_info: true                 # Show format info section

# Styling options
branding:
  primary_color: "#0f62fe"               # Main theme color
  secondary_color: "#ff6e6e"             # Accent color
  font_family: "IBM Plex Sans"           # Font family
  logo_url: "https://example.com/logo.png"  # Optional logo URL
```

### Adding Talks (`schedule.csv`)

**🚀 Use Excel, Google Sheets, or any spreadsheet app!**

| date | day_name | time | duration | title | presenter | presenter_title | company | abstract | speaker_image | speaker_links |
|------|----------|------|----------|-------|-----------|-----------------|---------|----------|---------------|---------------|
| 2024-03-15 | Day 1 - Friday | 09:00 | 20 min | Talk Title | John Doe | Senior Developer | Tech Corp | Talk description... | image-url | LinkedIn:https://linkedin.com/in/johndoe |

**💡 Pro Tip:** The CSV format is much easier for non-technical users!

### Speaker Images

You can use:
- **Placeholder images**: `https://via.placeholder.com/150x150/0f62fe/white?text=JD`
- **Direct image URLs**: `https://example.com/speaker-photo.jpg`
- **GitHub avatars**: `https://github.com/username.png`

### Speaker Links

Supported link types (with automatic icons):
- `LinkedIn` - LinkedIn profile
- `GitHub` - GitHub profile  
- `Twitter` - Twitter profile
- `Blog` - Personal blog/website
- `Portfolio` - Portfolio website
- `Research` - Research profile
- Any other name - Generic link icon

## 🛠️ Customization

### Visual Options (`config.yaml`)

Control what information is displayed:

```yaml
website:
  show_duration_badges: true     # Show "20 min" badges next to talk times
  show_format_info: true         # Show the info section with location/duration/format

branding:
  primary_color: "#0f62fe"       # Main theme color (IBM Blue)
  secondary_color: "#ff6e6e"     # Accent color
  logo_url: "your-logo-url"      # Optional: Conference/company logo
```

### Logo Setup

Add your organization's logo:
- **Direct URLs**: `https://yoursite.com/logo.png`
- **GitHub avatars**: `https://github.com/yourorg.png`
- **Placeholder**: `https://via.placeholder.com/120x40/0f62fe/ffffff?text=YOUR+LOGO`
- **Disable**: Leave empty `logo_url: ""`

### Advanced Styling

For deeper customization, edit `templates/index.html`:
- Modify CSS variables for colors
- Add custom styling in the `<style>` section
- Adjust Bootstrap layout structure

## 🔧 Local Development

To test changes locally:

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate the site
python generate_site.py

# Option 1: Open docs/index.html in your browser
# Option 2: Run local server
cd docs
python -m http.server 8000
# Then visit http://localhost:8000
```

## 📱 QR Codes

QR codes are automatically generated for all speaker links. Visitors can:
- Click the "QR" button next to any link
- Scan the QR code with their phone
- Instantly access speaker profiles/content

## 🎨 Mobile-First Design

The site is built mobile-first and includes:
- Touch-friendly buttons and links
- Optimized font sizes for mobile reading
- Responsive card layouts
- Fast loading times
- Offline-friendly (static files)

## 🔒 Security & Privacy

- **No tracking**: No analytics or tracking cookies
- **Static files**: No server-side code or databases
- **HTTPS**: Served securely via GitHub Pages
- **No data collection**: Completely privacy-friendly

## 🆘 Troubleshooting

### Site Not Updating?
1. Check the "Actions" tab in your GitHub repository
2. Look for failed builds (red X marks)
3. Click on the failed action to see error details

### CSV/YAML Syntax Errors?
- **CSV**: Check for missing commas, extra quotes, or line breaks in fields
- **YAML**: Use a validator like [yamllint.com](https://yamllint.com)
- Check indentation (use spaces, not tabs) in YAML files
- Ensure quotes around special characters

### Missing Speaker Images?
- Verify image URLs are accessible
- Use HTTPS URLs when possible
- Consider using placeholder images for testing

## 📁 Additional Files

This project also includes:
- **`CSV_INSTRUCTIONS.md`** - Detailed guide for editing the CSV schedule
- **`schedule_template.csv`** - Template for creating new schedules
- **`csv_to_yaml_converter.py`** - Utility to migrate old YAML schedules
- **`run_local.py`** - Local development server with auto-reload

## 🤝 Support

Need help? Here are your options:

1. **Check `CSV_INSTRUCTIONS.md`** - Comprehensive CSV editing guide
2. **Check the Issues**: Look at existing GitHub issues
3. **Create an Issue**: Describe your problem with examples
4. **Community Help**: Ask in discussions section

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Made with ❤️ for conference organizers who want beautiful, simple scheduling solutions.** 