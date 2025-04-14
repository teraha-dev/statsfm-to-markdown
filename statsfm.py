import requests
import json
import logging
import time
import os
import sys
import html

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
        'show_duration': os.getenv('INPUT_SHOW_DURATION', 'true').lower() == 'true',
        'show_rank': os.getenv('INPUT_SHOW_RANK', 'true').lower() == 'true',
        'theme': os.getenv('INPUT_THEME', 'light').lower(),
        'time_range': os.getenv('INPUT_TIME_RANGE', 'weeks').lower(),
        'readme_path': os.getenv('INPUT_README_PATH', README_PATH)
    }

    if not config['username']:
        logger.error("Error: 'statsfm_username' input is required.")
        sys.exit(1)

    if config['display_limit'] <= 0:
        logger.warning(f"'display_limit' must be greater than 0. Using default value 10.")
        config['display_limit'] = 10
    if config['theme'] not in ['light', 'dark']:
        logger.warning(f"Unsupported theme '{config['theme']}'. Using 'light' theme.")
        config['theme'] = 'light'
    if config['time_range'] not in ['weeks', 'months', 'lifetime']:
        logger.warning(f"Unsupported time range '{config['time_range']}'. Using 'weeks'.")
        config['time_range'] = 'weeks'

    logger.info(f"Configuration loaded: User={config['username']}, Limit={config['display_limit']}, Range={config['time_range']}, Theme={config['theme']}, ShowRank={config['show_rank']}, ShowDuration={config['show_duration']}")
    return config

# --- Duration Formatting Function ---
def format_duration(milliseconds) -> str | None:
    """Formats milliseconds into a human-readable string (Xh Ym or Zm)."""
    if milliseconds is None or milliseconds < 60000:
        return None
    total_seconds = int(milliseconds / 1000)
    total_minutes = total_seconds // 60
    hours = total_minutes // 60
    minutes = total_minutes % 60
    if hours > 0: return f"{hours}h {minutes}m"
    else: return f"{minutes}m"

# --- API Call Function ---
def get_top_albums(username, time_range, limit) -> list | None:
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

# --- HTML Content Generation Function ---
def generate_statsfm_content(items, config) -> str:
    """Generates the HTML content to be injected into the README based on album data."""
    if not items:
        logger.warning("No album data available to generate HTML content.")
        return "\nNo recent albums found or unable to fetch data.\n"

    themes = { 'light': { 'item_bg': '#ffffff', 'title_color': '#24292e', 'artist_color': '#586069', 'duration_color': '#586069', 'rank_bg': 'rgba(0, 0, 0, 0.6)', 'rank_color': 'white' }, 'dark': { 'item_bg': '#2d333b', 'title_color': '#c9d1d9', 'artist_color': '#8b949e', 'duration_color': '#8b949e', 'rank_bg': 'rgba(255, 255, 255, 0.6)', 'rank_color': 'black' }}
    current_theme = themes.get(config['theme'], themes['light'])

    FIXED_ITEM_WIDTH_PX = 145
    TEXT_CONTAINER_BASE_HEIGHT_PX = 55
    TEXT_CONTAINER_DURATION_HEIGHT_PX = 20
    text_container_height_px = TEXT_CONTAINER_BASE_HEIGHT_PX + (TEXT_CONTAINER_DURATION_HEIGHT_PX if config['show_duration'] else 0)

    list_container_style = 'display: flex; flex-wrap: wrap; gap: 16px; justify-content: flex-start; padding: 10px 0;'
    item_container_style = f'width: {FIXED_ITEM_WIDTH_PX}px; border-radius: 6px; padding: 10px; box-sizing: border-box; text-align: left; display: flex; flex-direction: column; position: relative; background-color: {current_theme["item_bg"]}; transition: transform 0.2s ease-in-out;'
    rank_style = f'position: absolute; top: 6px; left: 6px; background-color: {current_theme["rank_bg"]}; color: {current_theme["rank_color"]}; font-size: 9px; font-weight: bold; padding: 1px 4px; border-radius: 3px; z-index: 1;'
    image_style = 'width: 100%; display: block; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 4px; margin-bottom: 8px;'
    text_wrapper_style = f'height: {text_container_height_px}px; display: flex; flex-direction: column; justify-content: flex-start; overflow: hidden;'
    album_title_style = f'font-size: 13px; font-weight: 600; line-height: 1.35; color: {current_theme["title_color"]}; margin-bottom: 3px; height: calc(1.35em * 2); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; word-break: break-word;'
    artist_name_style = f'font-size: 11px; color: {current_theme["artist_color"]}; line-height: 1.3; margin-bottom: 5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; width: 100%;'
    duration_style = f'font-size: 10px; color: {current_theme["duration_color"]}; line-height: 1.3; font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace; margin-top: auto;'

    content_lines = []
    content_lines.append(f'<div style="{list_container_style}">')

    valid_items_count = 0
    for item in items:
        if valid_items_count >= config['display_limit']: break

        album_info = item.get("album")
        duration_ms = item.get("playedMs")

        if not album_info: logger.warning("Skipping item due to missing album information."); continue
        image_url = album_info.get("image")
        if not image_url: logger.warning(f"Skipping album '{album_info.get('name', 'Unknown')}' due to missing image URL."); continue

        formatted_duration = format_duration(duration_ms) if config['show_duration'] else None
        valid_items_count += 1
        rank = valid_items_count

        album_name = album_info.get("name", "Unknown Album")
        artists = album_info.get("artists", [])
        artist_name = artists[0].get("name", "Unknown Artist") if artists else "Unknown Artist"

        # --- Determine Album URL (Spotify first, then stats.fm) ---
        album_url = "#"
        statsfm_url = album_info.get("url")
        spotify_id = None
        external_ids = album_info.get("externalIds", {})
        spotify_ids = external_ids.get("spotify", [])
        if spotify_ids:
            spotify_id = spotify_ids[0]
            spotify_url = f"https://open.spotify.com/album/{spotify_id}"

        if spotify_id: album_url = spotify_url
        elif statsfm_url: album_url = statsfm_url

        alt_text = html.escape(f"{artist_name} - {album_name}", quote=True)
        safe_album_name = html.escape(album_name)
        safe_artist_name = html.escape(artist_name)
        tooltip_text = html.escape(f"{artist_name} - {album_name}", quote=True)

        item_html = f'  <a href="{album_url}" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit;">\n'
        item_html += f'    <div style="{item_container_style}" title="{tooltip_text}">\n'
        if config['show_rank']: item_html += f'      <span style="{rank_style}">{rank}</span>\n'
        item_html += f'      <img src="{image_url}" alt="{alt_text}" style="{image_style}">\n'
        item_html += f'      <div style="{text_wrapper_style}">\n'
        item_html += f'        <div style="{album_title_style}">{safe_album_name}</div>\n'
        item_html += f'        <div style="{artist_name_style}">{safe_artist_name}</div>\n'
        if formatted_duration:
            safe_formatted_duration = html.escape(formatted_duration)
            item_html += f'        <div style="{duration_style}">⏱️ {safe_formatted_duration}</div>\n'
        item_html += f'      </div>\n'
        item_html += f'    </div>\n'
        item_html += f'  </a>'
        content_lines.append(item_html)

    content_lines.append('</div>')

    if valid_items_count == 0:
         logger.warning("No valid album data found to display.")
         return "\nNo displayable recent albums found.\n"

    return "\n".join(content_lines) + "\n"


# --- README Update Function ---
def update_readme(content_to_insert, readme_path) -> None:
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
    new_readme_content.append("\n")
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
        html_content = generate_statsfm_content(top_albums_items, config)
        update_readme(html_content, readme_file_path)
    else:
        logger.error("Failed to fetch album data from API. README file will not be updated.")
        sys.exit(1)

    logger.info("Script finished successfully. Total execution time: %.2f seconds." % (time.time() - start_time))

if __name__ == "__main__":
    main()
