import requests
import json
import logging
import time
import os
import sys
import html
import base64
import io
from urllib.parse import urlparse
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ET

# --- Basic Setup ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
start_time = time.time()

README_PATH = "README.md"
START_MARKER = "<!-- STATSFM START -->"
END_MARKER = "<!-- STATSFM END -->"

BASE_API_URL_FORMAT = "https://api.stats.fm/api/v1/users/{username}/top/albums?range={range}&limit={limit}"
HEADERS = {
    'User-Agent': 'statsfm-to-markdown GitHub Action (github.com/teraha-dev/statsfm-to-markdown)'
}

# --- Configuration Reading and Validation ---
def get_config() -> dict:
    """Reads configuration from environment variables set by the action."""
    config = {
        'username': os.getenv('INPUT_STATSFM_USERNAME'),
        'display_limit': min(int(os.getenv('INPUT_DISPLAY_LIMIT', '10')), 50),
        'items_per_row': int(os.getenv('INPUT_ITEMS_PER_ROW', '5')),
        'show_duration': os.getenv('INPUT_SHOW_DURATION', 'true').lower() == 'true',
        'show_rank': os.getenv('INPUT_SHOW_RANK', 'true').lower() == 'true',
        'time_range': os.getenv('INPUT_TIME_RANGE', 'weeks').lower(),
        'readme_path': os.getenv('INPUT_README_PATH', README_PATH)
    }

    if not config['username']:
        logger.error("Error: 'statsfm_username' input is required.")
        sys.exit(1)

    if config['display_limit'] <= 0:
        logger.warning(f"'display_limit' must be greater than 0. Using default value 10.")
        config['display_limit'] = 10

    if config['time_range'] not in ['weeks', 'months', 'lifetime']:
        logger.warning(f"Unsupported time range '{config['time_range']}'. Using 'weeks'.")
        config['time_range'] = 'weeks'

    logger.info(f"Configuration loaded: User={config['username']}, Limit={config['display_limit']}, Range={config['time_range']}, ShowRank={config['show_rank']}, ShowDuration={config['show_duration']}")
    return config

# --- Duration Formatting Function ---
def format_duration(milliseconds: int | None) -> str | None:
    """Formats milliseconds into a human-readable string (Xh Ym or Zm)."""
    if milliseconds is None or milliseconds < 60000: return None
    total_seconds = int(milliseconds / 1000)
    total_minutes = total_seconds // 60
    hours = total_minutes // 60
    minutes = total_minutes % 60
    if hours > 0: return f"{hours}h {minutes}m"
    else: return f"{minutes}m"

# --- Image Download and Processing Function ---
def download_and_encode_image(image_url: str) -> str | None:
    """Downloads an image and converts it to base64 for SVG embedding."""
    try:
        response = requests.get(image_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        # Get content type
        content_type = response.headers.get('content-type', '').lower()
        if not content_type.startswith('image/'):
            logger.warning(f"Invalid content type for image: {content_type}")
            return generate_placeholder_image()
            
        # Convert to base64
        image_data = base64.b64encode(response.content).decode('utf-8')
        return f"data:{content_type};base64,{image_data}"
        
    except Exception as e:
        logger.warning(f"Failed to download image {image_url}: {e}")
        return generate_placeholder_image()

def generate_placeholder_image() -> str:
    """Generates a minimal placeholder image as base64 data URI."""
    # Create a minimal SVG placeholder (140x140)
    placeholder_svg = """<svg width="140" height="140" xmlns="http://www.w3.org/2000/svg">
        <rect width="140" height="140" fill="#fafafa" stroke="#f4f4f5" stroke-width="1" rx="6"/>
        <g transform="translate(70,70)">
            <circle cx="0" cy="0" r="20" fill="#f4f4f5" stroke="#e4e4e7" stroke-width="1"/>
            <path d="M-6,-10 L6,-10 L6,3 C6,7 3,10 0,10 S-6,7 -6,3 Z" fill="#a1a1aa"/>
            <circle cx="0" cy="5" r="4" fill="#a1a1aa"/>
        </g>
    </svg>"""
    
    placeholder_b64 = base64.b64encode(placeholder_svg.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{placeholder_b64}"

# --- Text Truncation Function ---
def truncate_text(text: str, max_length: int) -> str:
    """Truncates text to a maximum length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length-1].rstrip() + "…"

# --- SVG Generation Function ---
def generate_premium_svg(items: list[dict], config: dict) -> str:
    """Generates a premium quality SVG with beautiful design."""
    if not items:
        logger.warning("No album data available to generate SVG content.")
        return None
    
    items_per_row = config['items_per_row']
    display_limit = config['display_limit']
    
    # Design constants
    card_width = 180
    card_height = 220
    gap_x = 20
    gap_y = 25
    padding = 30
    image_size = 140
    
    # Calculate total rows needed
    total_items = min(len(items), display_limit)
    total_rows = (total_items + items_per_row - 1) // items_per_row
    
    # Calculate SVG dimensions
    svg_width = (card_width * items_per_row) + (gap_x * (items_per_row - 1)) + (padding * 2)
    svg_height = (card_height * total_rows) + (gap_y * (total_rows - 1)) + (padding * 2)
    
    # Create SVG root element
    svg = Element('svg', {
        'width': str(svg_width),
        'height': str(svg_height),
        'xmlns': 'http://www.w3.org/2000/svg',
        'xmlns:xlink': 'http://www.w3.org/1999/xlink',
        'viewBox': f'0 0 {svg_width} {svg_height}'
    })
    
    # Add styles - Minimal & Modern Design
    style = SubElement(svg, 'style')
    style.text = """
    .card {
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .card:hover {
        transform: translateY(-1px);
    }
    .album-image {
        border-radius: 6px;
    }
    .rank-badge {
        filter: drop-shadow(0 1px 3px rgba(0,0,0,0.1));
    }
    .artist-text {
        fill: #71717a;
        font-family: ui-sans-serif, system-ui, -apple-system, sans-serif;
        font-size: 10px;
        font-weight: 400;
        letter-spacing: 0.025em;
    }
    .album-text {
        fill: #18181b;
        font-family: ui-sans-serif, system-ui, -apple-system, sans-serif;
        font-size: 11px;
        font-weight: 500;
        letter-spacing: -0.015em;
    }
    .duration-text {
        fill: #a1a1aa;
        font-family: ui-mono, monospace;
        font-size: 9px;
        font-weight: 400;
        letter-spacing: 0.05em;
    }
    .rank-text {
        fill: white;
        font-family: ui-mono, monospace;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.1em;
    }
    """
    
    # Minimal design - no gradients needed
    
    valid_items_count = 0
    
    for item in items:
        if valid_items_count >= display_limit:
            break
            
        album_info = item.get("album")
        duration_ms = item.get("playedMs")
        
        if not album_info:
            continue
            
        image_url = album_info.get("image")
        if not image_url:
            continue
            
        # Download and encode image
        encoded_image = download_and_encode_image(image_url)
        if not encoded_image:
            continue
            
        valid_items_count += 1
        rank = valid_items_count
        
        # Calculate position
        row = (valid_items_count - 1) // items_per_row
        col = (valid_items_count - 1) % items_per_row
        x = padding + col * (card_width + gap_x)
        y = padding + row * (card_height + gap_y)
        
        # Get album data
        album_name = album_info.get("name", "Unknown Album")
        artists = album_info.get("artists", [])
        artist_name = artists[0].get("name", "Unknown Artist") if artists else "Unknown Artist"
        formatted_duration = format_duration(duration_ms)
        
        # Truncate text to fit
        album_display = truncate_text(album_name, 20)
        artist_display = truncate_text(artist_name, 22)
        
        # Create album URL
        album_url = "#"
        spotify_id = None
        external_ids = album_info.get("externalIds", {})
        spotify_ids = external_ids.get("spotify", [])
        if spotify_ids:
            spotify_id = spotify_ids[0]
            album_url = f"https://open.spotify.com/album/{spotify_id}"
        elif album_info.get("url"):
            album_url = album_info.get("url")
        
        # Create card group with link
        card_group = SubElement(svg, 'a', {
            'href': album_url,
            'target': '_blank',
            'rel': 'noopener noreferrer'
        })
        
        card = SubElement(card_group, 'g', {'class': 'card'})
        
        # Card background
        SubElement(card, 'rect', {
            'x': str(x),
            'y': str(y),
            'width': str(card_width),
            'height': str(card_height),
            'fill': '#ffffff',
            'rx': '8',
            'ry': '8',
            'stroke': '#f4f4f5',
            'stroke-width': '1'
        })
        
        # Album image
        image_x = x + (card_width - image_size) // 2
        image_y = y + 15
        
        SubElement(card, 'image', {
            'x': str(image_x),
            'y': str(image_y),
            'width': str(image_size),
            'height': str(image_size),
            'href': encoded_image,
            'class': 'album-image'
        })
        
        # Rank badge (if enabled) - Margiela style rounded rectangle
        if config['show_rank']:
            # Calculate badge dimensions
            badge_width = 24 if rank < 10 else 30
            badge_height = 16
            badge_x = x + card_width - badge_width - 8
            badge_y = y + 12
            
            # Margiela-inspired rounded rectangle with transparency
            SubElement(card, 'rect', {
                'x': str(badge_x),
                'y': str(badge_y),
                'width': str(badge_width),
                'height': str(badge_height),
                'rx': '6',
                'ry': '6',
                'fill': 'rgba(107, 114, 128, 0.75)',
                'class': 'rank-badge'
            })
            
            SubElement(card, 'text', {
                'x': str(badge_x + badge_width // 2),
                'y': str(badge_y + badge_height // 2 + 4),
                'text-anchor': 'middle',
                'class': 'rank-text'
            }).text = str(rank)
        
        # Album title
        text_y = image_y + image_size + 15
        SubElement(card, 'text', {
            'x': str(x + card_width // 2),
            'y': str(text_y),
            'text-anchor': 'middle',
            'class': 'album-text'
        }).text = album_display
        
        # Artist name
        text_y += 15
        SubElement(card, 'text', {
            'x': str(x + card_width // 2),
            'y': str(text_y),
            'text-anchor': 'middle',
            'class': 'artist-text'
        }).text = artist_display
        
        # Duration (if enabled and available)
        if config['show_duration'] and formatted_duration:
            text_y += 14
            SubElement(card, 'text', {
                'x': str(x + card_width // 2),
                'y': str(text_y),
                'text-anchor': 'middle',
                'class': 'duration-text'
            }).text = formatted_duration
    
    if valid_items_count == 0:
        logger.warning("No valid album data found to display.")
        return None
    
    # Convert to string
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
    
    return ET.tostring(svg, encoding='unicode')

# --- Individual Album SVG Generation Function ---
def generate_individual_album_svg(item: dict, rank: int, config: dict) -> tuple[str, str] | None:
    """Generates a single album SVG card and returns (svg_content, album_url)."""
    album_info = item.get("album")
    duration_ms = item.get("playedMs")
    
    if not album_info:
        return None
        
    image_url = album_info.get("image")
    if not image_url:
        return None
        
    # Download and encode image
    encoded_image = download_and_encode_image(image_url)
    if not encoded_image:
        return None
    
    # Get album data
    album_name = album_info.get("name", "Unknown Album")
    artists = album_info.get("artists", [])
    artist_name = artists[0].get("name", "Unknown Artist") if artists else "Unknown Artist"
    formatted_duration = format_duration(duration_ms)
    
    # Truncate text to fit
    album_display = truncate_text(album_name, 20)
    artist_display = truncate_text(artist_name, 22)
    
    # Create album URL
    album_url = "#"
    spotify_id = None
    external_ids = album_info.get("externalIds", {})
    spotify_ids = external_ids.get("spotify", [])
    if spotify_ids:
        spotify_id = spotify_ids[0]
        album_url = f"https://open.spotify.com/album/{spotify_id}"
    elif album_info.get("url"):
        album_url = album_info.get("url")
    
    # Design constants for individual card
    card_width = 180
    card_height = 220
    padding = 15
    image_size = 140
    
    # Calculate SVG dimensions (single card with padding)
    svg_width = card_width + (padding * 2)
    svg_height = card_height + (padding * 2)
    
    # Create SVG root element
    svg = Element('svg', {
        'width': str(svg_width),
        'height': str(svg_height),
        'xmlns': 'http://www.w3.org/2000/svg',
        'xmlns:xlink': 'http://www.w3.org/1999/xlink',
        'viewBox': f'0 0 {svg_width} {svg_height}'
    })
    
    # Add styles - Minimal & Modern Design
    style = SubElement(svg, 'style')
    style.text = """
    .card {
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .card:hover {
        transform: translateY(-1px);
    }
    .album-image {
        border-radius: 6px;
    }
    .rank-badge {
        filter: drop-shadow(0 1px 3px rgba(0,0,0,0.1));
    }
    .artist-text {
        fill: #71717a;
        font-family: ui-sans-serif, system-ui, -apple-system, sans-serif;
        font-size: 10px;
        font-weight: 400;
        letter-spacing: 0.025em;
    }
    .album-text {
        fill: #18181b;
        font-family: ui-sans-serif, system-ui, -apple-system, sans-serif;
        font-size: 11px;
        font-weight: 500;
        letter-spacing: -0.015em;
    }
    .duration-text {
        fill: #a1a1aa;
        font-family: ui-mono, monospace;
        font-size: 9px;
        font-weight: 400;
        letter-spacing: 0.05em;
    }
    .rank-text {
        fill: white;
        font-family: ui-mono, monospace;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.1em;
    }
    """
    
    # Card position (centered)
    x = padding
    y = padding
    
    # Create card group
    card = SubElement(svg, 'g', {'class': 'card'})
    
    # Card background - Minimal design
    SubElement(card, 'rect', {
        'x': str(x),
        'y': str(y),
        'width': str(card_width),
        'height': str(card_height),
        'fill': '#ffffff',
        'rx': '8',
        'ry': '8',
        'stroke': '#f4f4f5',
        'stroke-width': '1'
    })
    
    # Album image
    image_x = x + (card_width - image_size) // 2
    image_y = y + 15
    
    SubElement(card, 'image', {
        'x': str(image_x),
        'y': str(image_y),
        'width': str(image_size),
        'height': str(image_size),
        'href': encoded_image,
        'class': 'album-image'
    })
    
    # Rank badge (if enabled) - Margiela style rounded rectangle
    if config['show_rank']:
        # Calculate badge dimensions
        badge_width = 24 if rank < 10 else 30
        badge_height = 16
        badge_x = x + card_width - badge_width - 8
        badge_y = y + 12
        
        # Margiela-inspired rounded rectangle with transparency
        SubElement(card, 'rect', {
            'x': str(badge_x),
            'y': str(badge_y),
            'width': str(badge_width),
            'height': str(badge_height),
            'rx': '6',
            'ry': '6',
            'fill': 'rgba(107, 114, 128, 0.75)',
            'class': 'rank-badge'
        })
        
        SubElement(card, 'text', {
            'x': str(badge_x + badge_width // 2),
            'y': str(badge_y + badge_height // 2 + 4),
            'text-anchor': 'middle',
            'class': 'rank-text'
        }).text = str(rank)
    
    # Album title
    text_y = image_y + image_size + 15
    SubElement(card, 'text', {
        'x': str(x + card_width // 2),
        'y': str(text_y),
        'text-anchor': 'middle',
        'class': 'album-text'
    }).text = album_display
    
    # Artist name
    text_y += 15
    SubElement(card, 'text', {
        'x': str(x + card_width // 2),
        'y': str(text_y),
        'text-anchor': 'middle',
        'class': 'artist-text'
    }).text = artist_display
    
    # Duration (if enabled and available)
    if config['show_duration'] and formatted_duration:
        text_y += 14
        SubElement(card, 'text', {
            'x': str(x + card_width // 2),
            'y': str(text_y),
            'text-anchor': 'middle',
            'class': 'duration-text'
        }).text = formatted_duration
    
    # Convert to string
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
    
    svg_content = ET.tostring(svg, encoding='unicode')
    return (svg_content, album_url)

# --- API Call Function ---
def get_top_albums(username: str, time_range: str, limit: int) -> list[dict] | None:
    """Fetches Top Album data from the stats.fm API."""
    api_limit = min(limit + 5, 50)
    api_url = BASE_API_URL_FORMAT.format(username=username, range=time_range, limit=api_limit)
    logger.info(f"Requesting API URL: {api_url}")
    try:
        response = requests.get(api_url, headers=HEADERS, timeout=20)
        response.raise_for_status()
        data = response.json()
        if "items" not in data:
            logger.error("API response missing 'items' key.")
            return None
        return data["items"]
    except requests.exceptions.Timeout:
        logger.error("API request timed out.")
        return None
    except requests.exceptions.HTTPError as e:
        logger.error(f"API HTTP Error: {e.response.status_code} {e.response.reason}")
        logger.error(f"Response content snippet: {e.response.text[:500]}")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"API Request failed: {e}")
        return None
    except json.JSONDecodeError:
        logger.error("Failed to parse API response JSON.")
        return None

# --- Individual SVG File Management Function ---
def save_individual_svg_files(items: list[dict], config: dict) -> list[tuple[str, str]]:
    """Saves individual SVG files and returns list of (filepath, album_url) tuples."""
    # Create directory if it doesn't exist
    svg_dir = "statsfm_svgs"
    os.makedirs(svg_dir, exist_ok=True)
    
    # Clear existing SVG files to avoid stale files
    import glob
    existing_svgs = glob.glob(os.path.join(svg_dir, "*.svg"))
    for svg_file in existing_svgs:
        try:
            os.remove(svg_file)
            logger.info(f"Removed old SVG: {svg_file}")
        except OSError:
            pass
    
    saved_files = []
    valid_items_count = 0
    
    for item in items:
        if valid_items_count >= config['display_limit']:
            break
            
        album_info = item.get("album")
        if not album_info or not album_info.get("image"):
            continue
            
        valid_items_count += 1
        rank = valid_items_count
        
        # Generate individual SVG
        svg_result = generate_individual_album_svg(item, rank, config)
        if not svg_result:
            continue
            
        svg_content, album_url = svg_result
        
        # Generate filename
        filename = f"{rank}.svg"
        filepath = os.path.join(svg_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            logger.info(f"Successfully saved SVG #{rank} to '{filepath}'")
            saved_files.append((filepath, album_url))
        except IOError as e:
            logger.error(f"Error saving SVG file '{filepath}': {e}")
            continue
    
    return saved_files

# --- Generate Individual SVG Content for README ---
def generate_statsfm_content(items: list[dict], config: dict) -> str:
    """Generates individual SVGs and returns markdown content for README."""
    if not items:
        logger.warning("No album data available to generate SVG content.")
        return "\n\nNo recent albums found or unable to fetch data.\n\n"
    
    # Save individual SVG files
    saved_files = save_individual_svg_files(items, config)
    
    if not saved_files:
        logger.error("Failed to save any SVG files.")
        return "\n\nError generating album display.\n\n"
    
    # Create markdown content with clickable individual SVGs
    markdown_lines = []
    items_per_row = config['items_per_row']
    
    # Group SVGs by rows
    for i in range(0, len(saved_files), items_per_row):
        row_files = saved_files[i:i + items_per_row]
        row_images = []
        
        for filepath, album_url in row_files:
            # Create clickable SVG image
            img_tag = f'<a href="{album_url}" target="_blank" rel="noopener noreferrer"><img src="{filepath}" alt="Album #{i + len(row_images) + 1}" width="210" height="250" /></a>'
            row_images.append(img_tag)
        
        # Join images in the row with some spacing
        row_content = "    ".join(row_images)
        markdown_lines.append(f'<p align="center">{row_content}</p>')
    
    # Combine all rows
    markdown_content = "\n" + "\n".join(markdown_lines) + "\n"
    
    logger.info(f"Generated {len(saved_files)} individual SVG files with clickable links")
    return markdown_content

# --- README Update Function ---
def update_readme(content_to_insert: str, readme_path: str) -> None:
    """Replaces content between the START and END markers in the README file."""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_lines = f.readlines()
    except FileNotFoundError:
        logger.error(f"Error: README file not found at '{readme_path}'.")
        sys.exit(1)
    except IOError as e:
        logger.error(f"Error reading README file '{readme_path}': {e}")
        sys.exit(1)

    start_index = -1
    end_index = -1

    for i, line in enumerate(readme_lines):
        if line.strip() == START_MARKER:
            start_index = i
        elif line.strip() == END_MARKER:
            end_index = i
            break

    if start_index == -1 or end_index == -1 or start_index >= end_index:
        logger.error(f"Error: Could not find markers '{START_MARKER}' and '{END_MARKER}' in '{readme_path}'.")
        logger.error("Please ensure both markers exist on separate lines and the start marker appears before the end marker.")
        sys.exit(1)


    new_readme_content = readme_lines[:start_index+1]
    new_readme_content.append(content_to_insert)
    new_readme_content.extend(readme_lines[end_index:])

    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.writelines(new_readme_content)
        logger.info(f"Successfully updated '{readme_path}'.")
    except IOError as e:
        logger.error(f"Error writing to README file '{readme_path}': {e}")
        sys.exit(1)

# --- Main Execution Logic ---
def main() -> None:
    """Main script execution function."""
    config = get_config()
    readme_file_path = config['readme_path']

    top_albums_items = get_top_albums(config['username'], config['time_range'], config['display_limit'])

    if top_albums_items is not None:
        svg_content = generate_statsfm_content(top_albums_items, config)
        update_readme(svg_content, readme_file_path)
    else:
        logger.error("Failed to fetch album data from API. README file will not be updated.")
        sys.exit(1)

    logger.info("Script finished successfully. Total execution time: %.2f seconds." % (time.time() - start_time))

if __name__ == "__main__":
    main()
