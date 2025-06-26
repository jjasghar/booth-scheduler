#!/usr/bin/env python3
"""
Local development server for testing the booth scheduler website.
Generates the site and serves it locally with auto-reload on file changes.
"""

import os
import sys
import time
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ScheduleWatcher(FileSystemEventHandler):
    """Watch for changes to schedule.yaml and regenerate site."""
    
    def on_modified(self, event):
        if event.src_path.endswith('schedule.yaml') or event.src_path.endswith('.html'):
            print("📝 Detected changes, regenerating site...")
            generate_site()


def generate_site():
    """Generate the static site."""
    from generate_site import generate_site
    generate_site()


class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Custom handler to serve from docs directory."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='docs', **kwargs)


def start_server(port=8000):
    """Start local HTTP server."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f"🌐 Server running at http://localhost:{port}")
    print("📱 Test on mobile by using your computer's IP address")
    print("🔄 The site will auto-regenerate when you edit schedule.yaml")
    print("⏹️  Press Ctrl+C to stop the server")
    httpd.serve_forever()


def main():
    # Initial site generation
    print("🚀 Starting local development server...")
    generate_site()
    
    # Setup file watcher
    event_handler = ScheduleWatcher()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    try:
        # Start server in a separate thread
        port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
        start_server(port)
    except KeyboardInterrupt:
        print("\n👋 Shutting down server...")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    # Check if watchdog is installed
    try:
        import watchdog
    except ImportError:
        print("⚠️  For auto-reload functionality, install watchdog:")
        print("   pip install watchdog")
        print("   For now, you'll need to manually regenerate after changes.")
        
        # Just generate once and serve
        generate_site()
        try:
            port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
            start_server(port)
        except KeyboardInterrupt:
            print("\n👋 Shutting down server...")
    else:
        main() 