#!/usr/bin/env python3
"""
Utility to convert old schedule.yaml format to new CSV format
Run this once if you have existing YAML schedule data
"""

import yaml
import csv
import os


def convert_yaml_to_csv(yaml_file='schedule.yaml', csv_file='schedule.csv', config_file='config.yaml'):
    """Convert old YAML schedule to new CSV + config format."""
    
    if not os.path.exists(yaml_file):
        print(f"❌ {yaml_file} not found. This converter is for migrating old YAML schedules.")
        return
    
    print(f"🔄 Converting {yaml_file} to CSV format...")
    
    # Load old YAML format
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    # Extract config data
    config_data = {
        'conference': data.get('conference', {}),
        'website': {
            'title_suffix': 'Schedule',
            'footer_text': 'Schedule generated with ❤️ using Python'
        },
        'branding': {
            'primary_color': '#0f62fe',
            'secondary_color': '#ff6e6e',
            'font_family': 'IBM Plex Sans',
            'logo_url': ''
        }
    }
    
    # Write config file
    with open(config_file, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    print(f"✅ Created {config_file}")
    
    # Extract schedule data and write CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow([
            'date', 'day_name', 'time', 'duration', 'title', 
            'presenter', 'presenter_title', 'company', 'abstract', 
            'speaker_image', 'speaker_links'
        ])
        
        # Write data rows
        for day in data.get('days', []):
            date = day.get('date', '')
            day_name = day.get('day_name', '')
            
            for talk in day.get('talks', []):
                # Format speaker links
                links_str = ""
                if 'speaker_links' in talk:
                    link_parts = []
                    for link in talk['speaker_links']:
                        link_parts.append(f"{link['name']}:{link['url']}")
                    links_str = ','.join(link_parts)
                
                writer.writerow([
                    date,
                    day_name,
                    talk.get('time', ''),
                    talk.get('duration', ''),
                    talk.get('title', ''),
                    talk.get('presenter', ''),
                    talk.get('presenter_title', ''),
                    talk.get('company', ''),
                    talk.get('abstract', ''),
                    talk.get('speaker_image', ''),
                    links_str
                ])
    
    print(f"✅ Created {csv_file}")
    print(f"📁 Old file {yaml_file} preserved (you can delete it manually)")
    print("🎉 Conversion complete! You can now edit your schedule in Excel/Google Sheets!")


if __name__ == "__main__":
    convert_yaml_to_csv() 