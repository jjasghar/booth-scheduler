# 🎤 Booth Scheduler

A beautiful, responsive conference booth scheduling system that automatically generates a static website from a simple YAML file. Perfect for tech conferences, meetups, and events!

## ✨ Features

- 📱 **Responsive Design**: Looks great on phones, tablets, and laptops
- 🔄 **Auto-Deploy**: Changes to schedule automatically update the website
- 📊 **QR Codes**: Generate QR codes for speaker links on-the-fly
- 🎨 **Modern UI**: Clean, professional design with smooth animations
- 🚀 **GitHub Pages**: Free hosting with custom domain support
- 📝 **Easy Editing**: Update your entire schedule by editing one YAML file

## 🚀 Quick Start

### 1. Setup Your Repository

1. **Fork or clone this repository**
2. **Enable GitHub Pages**:
   - Go to your repository settings
   - Scroll to "Pages" section
   - Set source to "GitHub Actions"

### 2. Edit Your Schedule

Open `schedule.yaml` and customize it with your conference details:

```yaml
conference:
  name: "Your Conference Name"
  booth_name: "Your Booth Name"
  location: "Hall A, Booth 123"
  description: "Your booth description"

days:
  - date: "2024-03-15"
    day_name: "Day 1 - Friday"
    talks:
      - time: "09:00"
        duration: "20 min"
        title: "Your Talk Title"
        presenter: "Speaker Name"
        # ... more details
```

### 3. Automatic Deployment

🎉 **That's it!** When you commit changes to `schedule.yaml`, GitHub Actions will automatically:
- Generate a new version of your website
- Deploy it to GitHub Pages
- Your site will be live at: `https://yourusername.github.io/your-repo-name`

## 📝 Editing Your Schedule

### Conference Information

```yaml
conference:
  name: "Tech Conference 2024"           # Conference name
  booth_name: "Innovation Booth"         # Your booth name
  location: "Hall A, Booth 123"          # Physical location
  description: "Brief description"       # Optional description
```

### Adding Days and Talks

```yaml
days:
  - date: "2024-03-15"                   # Date in YYYY-MM-DD format
    day_name: "Day 1 - Friday"           # Display name for the day
    talks:
      - time: "09:00"                    # Time in HH:MM format (24-hour)
        duration: "20 min"               # Talk duration
        title: "Talk Title"              # Presentation title
        presenter: "John Doe"            # Speaker name(s)
        presenter_title: "Senior Developer" # Job title
        company: "Tech Corp"             # Company name
        abstract: "Talk description..."   # Brief abstract
        speaker_image: "image-url"       # Speaker photo URL
        speaker_links:                   # Social/professional links
          - name: "LinkedIn"
            url: "https://linkedin.com/in/johndoe"
          - name: "GitHub"
            url: "https://github.com/johndoe"
```

### Speaker Images

You can use:
- **Placeholder images**: `https://via.placeholder.com/150x150/4CAF50/white?text=JD`
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

### Changing Colors

Edit the CSS variables in `templates/index.html`:

```css
:root {
    --primary-color: #2563eb;    /* Main theme color */
    --secondary-color: #f59e0b;  /* Accent color */
    --success-color: #10b981;    /* Success/duration tags */
    --danger-color: #ef4444;     /* Error states */
}
```

### Adding Custom Styling

Add your custom CSS to the `<style>` section in `templates/index.html`.

### Modifying Layout

The template uses Bootstrap 5 for responsive design. You can modify the HTML structure in `templates/index.html`.

## 🔧 Local Development

To test changes locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate the site
python generate_site.py

# Open docs/index.html in your browser
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

### YAML Syntax Errors?
- Use a YAML validator like [yamllint.com](https://yamllint.com)
- Check indentation (use spaces, not tabs)
- Ensure quotes around special characters

### Missing Speaker Images?
- Verify image URLs are accessible
- Use HTTPS URLs when possible
- Consider using placeholder images for testing

## 🤝 Support

Need help? Here are your options:

1. **Check the Issues**: Look at existing GitHub issues
2. **Create an Issue**: Describe your problem with examples
3. **Community Help**: Ask in discussions section

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Made with ❤️ for conference organizers who want beautiful, simple scheduling solutions.** 