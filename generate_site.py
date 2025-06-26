#!/usr/bin/env python3
"""
Booth Scheduler Static Site Generator
Generates a responsive conference booth schedule website from YAML data.
"""

import os
import yaml
import qrcode
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import io
import base64


def load_schedule_data(yaml_file='schedule.yaml'):
    """Load schedule data from YAML file."""
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)


def generate_qr_code(url):
    """Generate QR code as base64 encoded image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"


def format_time(time_str):
    """Format time string to a more readable format."""
    try:
        time_obj = datetime.strptime(time_str, "%H:%M")
        return time_obj.strftime("%I:%M %p").lower().replace(" 0", " ")
    except:
        return time_str


def format_date(date_str):
    """Format date string to a more readable format."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%A, %B %d, %Y")
    except:
        return date_str


def generate_site():
    """Generate the complete static site."""
    print("🚀 Generating booth scheduler website...")
    
    # Load data
    data = load_schedule_data()
    
    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    
    # Add custom filters
    env.filters['format_time'] = format_time
    env.filters['format_date'] = format_date
    
    # Ensure output directory exists
    os.makedirs('docs', exist_ok=True)
    os.makedirs('docs/qr', exist_ok=True)
    
    # Process talks and generate QR codes
    for day in data['days']:
        for talk in day['talks']:
            if 'speaker_links' in talk:
                for link in talk['speaker_links']:
                    qr_data = generate_qr_code(link['url'])
                    link['qr_code'] = qr_data
    
    # Generate main index page
    template = env.get_template('index.html')
    html = template.render(data=data)
    
    with open('docs/index.html', 'w') as f:
        f.write(html)
    
    print("✅ Website generated successfully!")
    print("📁 Files created in 'docs/' directory")
    print("🌐 Ready for GitHub Pages deployment")


if __name__ == "__main__":
    generate_site() 