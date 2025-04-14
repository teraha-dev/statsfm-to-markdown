# statsfm-to-markdown 🎵

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-statsfm--to--markdown-green?style=flat-square&logo=github)](https://github.com/marketplace/actions/statsfm-to-markdown)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://github.com/teraha-dev/statsfm-to-markdown/blob/main/LICENSE)
[![Action Build Status](https://github.com/teraha-dev/statsfm-to-markdown/actions/workflows/statsfm.yml/badge.svg)](https://github.com/teraha-dev/statsfm-to-markdown/actions/workflows/statsfm.yml)

A GitHub Action that fetches your top albums from [stats.fm](https://stats.fm/) (formerly Spotistats) for a specified time range and displays them beautifully on your GitHub profile README. Inspired by the [lastfm-to-markdown](https://github.com/lastfm-to-markdown/lastfm-to-markdown) project.

---

## ✨ Example Output Section

This action will find the following markers in your README file and automatically insert the generated list of your top albums between them:

<!-- STATSFM START -->
<div style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: flex-start; padding: 10px 0;">
  <a href="https://open.spotify.com/album/5K4YFkTizFoMOyN5Khfp7G" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit;">
    <div style="width: 145px; border-radius: 6px; padding: 10px; box-sizing: border-box; text-align: left; display: flex; flex-direction: column; position: relative; background-color: #ffffff; transition: transform 0.2s ease-in-out;" title="Fishmans - 98.12.28 男達の別れ (Live)">
      <span style="position: absolute; top: 6px; left: 6px; background-color: rgba(0, 0, 0, 0.6); color: white; font-size: 9px; font-weight: bold; padding: 1px 4px; border-radius: 3px; z-index: 1;">1</span>
      <img src="https://i.scdn.co/image/ab67616d0000b273b8b2f65e2dfa733439974801" alt="Fishmans - 98.12.28 男達の別れ (Live)" style="width: 100%; display: block; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 4px; margin-bottom: 8px;">
      <div style="height: 75px; display: flex; flex-direction: column; justify-content: flex-start; overflow: hidden;">
        <div style="font-size: 13px; font-weight: 600; line-height: 1.35; color: #24292e; margin-bottom: 3px; height: calc(1.35em * 2); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; word-break: break-word;">98.12.28 男達の別れ (Live)</div>
        <div style="font-size: 11px; color: #586069; line-height: 1.3; margin-bottom: 5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; width: 100%;">Fishmans</div>
        <div style="font-size: 10px; color: #586069; line-height: 1.3; font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace; margin-top: auto;">⏱️ 16h 27m</div>
      </div>
    </div>
  </a>
  <a href="https://open.spotify.com/album/5ZGzGGNAB6U7QlKpdaMu0d" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit;">
    <div style="width: 145px; border-radius: 6px; padding: 10px; box-sizing: border-box; text-align: left; display: flex; flex-direction: column; position: relative; background-color: #ffffff; transition: transform 0.2s ease-in-out;" title="結束バンド - 結束バンド">
      <span style="position: absolute; top: 6px; left: 6px; background-color: rgba(0, 0, 0, 0.6); color: white; font-size: 9px; font-weight: bold; padding: 1px 4px; border-radius: 3px; z-index: 1;">2</span>
      <img src="https://i.scdn.co/image/ab67616d0000b27309ca036917527fa198ead7b1" alt="結束バンド - 結束バンド" style="width: 100%; display: block; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 4px; margin-bottom: 8px;">
      <div style="height: 75px; display: flex; flex-direction: column; justify-content: flex-start; overflow: hidden;">
        <div style="font-size: 13px; font-weight: 600; line-height: 1.35; color: #24292e; margin-bottom: 3px; height: calc(1.35em * 2); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; word-break: break-word;">結束バンド</div>
        <div style="font-size: 11px; color: #586069; line-height: 1.3; margin-bottom: 5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; width: 100%;">結束バンド</div>
        <div style="font-size: 10px; color: #586069; line-height: 1.3; font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace; margin-top: auto;">⏱️ 9h 9m</div>
      </div>
    </div>
  </a>
  <a href="https://open.spotify.com/album/3GH4IiI6jQAIvnHVdb5FB6" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit;">
    <div style="width: 145px; border-radius: 6px; padding: 10px; box-sizing: border-box; text-align: left; display: flex; flex-direction: column; position: relative; background-color: #ffffff; transition: transform 0.2s ease-in-out;" title="my bloody valentine - Loveless">
      <span style="position: absolute; top: 6px; left: 6px; background-color: rgba(0, 0, 0, 0.6); color: white; font-size: 9px; font-weight: bold; padding: 1px 4px; border-radius: 3px; z-index: 1;">3</span>
      <img src="https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/d8/9c/a2/d89ca2ad-3191-d877-4c2f-13fb3e619a7b/887830015998.png/768x768bb.jpg" alt="my bloody valentine - Loveless" style="width: 100%; display: block; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 4px; margin-bottom: 8px;">
      <div style="height: 75px; display: flex; flex-direction: column; justify-content: flex-start; overflow: hidden;">
        <div style="font-size: 13px; font-weight: 600; line-height: 1.35; color: #24292e; margin-bottom: 3px; height: calc(1.35em * 2); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; word-break: break-word;">Loveless</div>
        <div style="font-size: 11px; color: #586069; line-height: 1.3; margin-bottom: 5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; width: 100%;">my bloody valentine</div>
        <div style="font-size: 10px; color: #586069; line-height: 1.3; font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace; margin-top: auto;">⏱️ 6h 49m</div>
      </div>
    </div>
  </a>
  <a href="https://open.spotify.com/album/4i21O3uVh5palcfFhCjlT7" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit;">
    <div style="width: 145px; border-radius: 6px; padding: 10px; box-sizing: border-box; text-align: left; display: flex; flex-direction: column; position: relative; background-color: #ffffff; transition: transform 0.2s ease-in-out;" title="Slowdive - Souvlaki">
      <span style="position: absolute; top: 6px; left: 6px; background-color: rgba(0, 0, 0, 0.6); color: white; font-size: 9px; font-weight: bold; padding: 1px 4px; border-radius: 3px; z-index: 1;">4</span>
      <img src="https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/c2/a0/a4/c2a0a495-ec33-27f1-c6db-0dff1c3ba15d/dj.pzrqoswp.jpg/768x768bb.jpg" alt="Slowdive - Souvlaki" style="width: 100%; display: block; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 4px; margin-bottom: 8px;">
      <div style="height: 75px; display: flex; flex-direction: column; justify-content: flex-start; overflow: hidden;">
        <div style="font-size: 13px; font-weight: 600; line-height: 1.35; color: #24292e; margin-bottom: 3px; height: calc(1.35em * 2); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; word-break: break-word;">Souvlaki</div>
        <div style="font-size: 11px; color: #586069; line-height: 1.3; margin-bottom: 5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; width: 100%;">Slowdive</div>
        <div style="font-size: 10px; color: #586069; line-height: 1.3; font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace; margin-top: auto;">⏱️ 3h 17m</div>
      </div>
    </div>
  </a>
  <a href="#" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit;">
    <div style="width: 145px; border-radius: 6px; padding: 10px; box-sizing: border-box; text-align: left; display: flex; flex-direction: column; position: relative; background-color: #ffffff; transition: transform 0.2s ease-in-out;" title="Camel - Mirage (Remastered)">
      <span style="position: absolute; top: 6px; left: 6px; background-color: rgba(0, 0, 0, 0.6); color: white; font-size: 9px; font-weight: bold; padding: 1px 4px; border-radius: 3px; z-index: 1;">5</span>
      <img src="https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/36/c0/15/36c015db-fa1b-c65c-67dc-302040ee3874/00042288292920.rgb.jpg/768x768bb.jpg" alt="Camel - Mirage (Remastered)" style="width: 100%; display: block; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 4px; margin-bottom: 8px;">
      <div style="height: 75px; display: flex; flex-direction: column; justify-content: flex-start; overflow: hidden;">
        <div style="font-size: 13px; font-weight: 600; line-height: 1.35; color: #24292e; margin-bottom: 3px; height: calc(1.35em * 2); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; word-break: break-word;">Mirage (Remastered)</div>
        <div style="font-size: 11px; color: #586069; line-height: 1.3; margin-bottom: 5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; width: 100%;">Camel</div>
        <div style="font-size: 10px; color: #586069; line-height: 1.3; font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace; margin-top: auto;">⏱️ 3h 17m</div>
      </div>
    </div>
  </a>
</div>

<!-- STATSFM END -->

*(The actual content generated by the workflow will appear between these markers, displaying album covers, titles, artists, and optionally rank and playtime.)*

## 🚀 Usage

Follow these steps to set up the action:

1.  **Add Markers to your README:**
    Add the following comment markers to your `README.md` file where you want the stats.fm top albums section to appear. The content between these markers will be automatically generated and updated by the action.

    ```markdown
    <!-- STATSFM START -->
    <!-- STATSFM END -->
    ```

2.  **Create a Workflow File:**
    Create a new file in your repository at the path `.github/workflows/statsfm.yml` (or choose a different name). Paste the following YAML content into the file:

    ```yaml
    name: Update stats.fm Top Albums

    on:
      # Schedule updates (e.g., runs every day at midnight UTC)
      schedule:
        - cron: '0 0 * * *'
      # Allow manual triggering
      workflow_dispatch:

    jobs:
      update-readme:
        runs-on: ubuntu-latest
        permissions:
          contents: write
        steps:
          # Check out the repository code
          - name: Checkout code
            uses: actions/checkout@v4

          # Run the statsfm-to-markdown action
          - name: Update stats.fm top albums
            uses: teraha-dev/statsfm-to-markdown@v1 # Use the latest release tag (e.g., @v1, @v1.0.0)
            with:
              # REQUIRED: Your stats.fm username
              statsfm_username: 'YOUR_STATSFM_USERNAME' # Replace with your actual username

              # OPTIONAL: Customize the display (see Inputs below)
              display_limit: '10'        # Number of albums to show (max 50)
              time_range: 'weeks'       # Data period: weeks, months, lifetime
              theme: 'light'            # Appearance: light, dark
              show_rank: 'true'         # Show rank number: true, false
              show_duration: 'true'     # Show playtime: true, false
              readme_path: 'README.md'  # Path to your README file

          # Commit and push the updated README file
          - name: Commit and push changes
            run: |
              git config --local user.email "action@github.com"
              git config --local user.name "statsfm-to-markdown Action"
              git add README.md # Or use the specific path from 'readme_path' if changed
              # Commit only if README.md has changed
              if git diff --staged --quiet; then
                echo "No changes in README.md. Skipping commit."
              else
                git commit -m "docs: Update stats.fm top albums"
                echo "Pushing changes..."
                git push
              fi
            env:
              GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} # Required for pushing changes
    ```

3.  **Replace Placeholders:**
    *   In the workflow file (`.github/workflows/statsfm.yml`), find the line `statsfm_username: 'YOUR_STATSFM_USERNAME'` and replace `'YOUR_STATSFM_USERNAME'` with your actual stats.fm username.

4.  **Commit and Push:**
    Commit the new workflow file (`.github/workflows/statsfm.yml`) and your updated `README.md` (containing the markers) to your repository's main branch.

The action will now run according to the schedule you defined (`cron`) or when you manually trigger it from the Actions tab in your GitHub repository.

## ⚙️ Inputs

The following inputs can be configured using the `with` keyword in your workflow file:

| Input             | Description                                                      | Required | Default    | Options                     |
| :---------------- | :--------------------------------------------------------------- | :------- | :--------- | :-------------------------- |
| `statsfm_username`| Your username on stats.fm.                                       | **`true`** | `N/A`      |                             |
| `display_limit`   | The maximum number of albums to display.                         | `false`  | `10`       | `1` to `50`                 |
| `show_duration`   | Whether to show the total playtime for each album.               | `false`  | `true`     | `true`, `false`             |
| `show_rank`       | Whether to show the ranking number (1, 2, 3...) for each album. | `false`  | `true`     | `true`, `false`             |
| `theme`           | The visual theme for the displayed albums section.               | `false`  | `light`    | `light`, `dark`             |
| `time_range`      | The time period for fetching top albums data.                    | `false`  | `weeks`    | `weeks`, `months`, `lifetime` |
| `readme_path`     | The path to the README file that needs to be updated.            | `false`  | `README.md`|                             |

## 🛠️ Configuration Examples

**Basic Setup (Default Settings):**
Shows the top 10 albums from the last few weeks using the light theme, including rank and duration.

```yaml
- name: Update stats.fm top albums
  uses: teraha-dev/statsfm-to-markdown@v1
  with:
    statsfm_username: 'your_username'
```

**Customized Setup (Dark Theme, 5 Albums, Lifetime):**
Shows the top 5 albums from all time using the dark theme, hiding the rank and duration.

```yaml
- name: Update stats.fm top albums
  uses: teraha-dev/statsfm-to-markdown@v1
  with:
    statsfm_username: 'your_username'
    display_limit: '5'
    time_range: 'lifetime'
    theme: 'dark'
    show_rank: 'false'
    show_duration: 'false'
```

**Updating a Different File:**
Updates a file named `PROFILE.md` instead of the default `README.md`.

```yaml
- name: Update stats.fm top albums in PROFILE.md
  uses: teraha-dev/statsfm-to-markdown@v1
  with:
    statsfm_username: 'your_username'
    readme_path: 'PROFILE.md' # Don't forget to add the markers in PROFILE.md too!
```

## 🤔 Troubleshooting

*   **Workflow Not Running:** Ensure the workflow file (`.github/workflows/statsfm.yml`) is correctly placed in the `.github/workflows/` directory and has been pushed to your default branch (usually `main` or `master`). Check the Actions tab in your repository for run logs.
*   **Markers Not Found Error:** Double-check that `<!-- STATSFM START -->` and `<!-- STATSFM END -->` markers exist exactly as shown (case-sensitive) on separate lines within your `README.md` file (or the file specified in `readme_path`). The START marker must appear before the END marker.
*   **Invalid Username Error:** Verify that the `statsfm_username` provided in the workflow file is your correct stats.fm username.
*   **API Errors / No Albums Displayed:**
    *   The stats.fm API might be temporarily unavailable. Check the workflow logs for specific error messages (like HTTP status codes).
    *   Ensure you have listening history on stats.fm for the selected `time_range`. If `time_range` is `weeks` or `months`, you need recent plays.
    *   The action filters out albums if they lack essential data from the API (e.g., image URL). Try increasing the `display_limit` slightly, as the API might return items that cannot be displayed.
    *   **Note:** This action relies on stats.fm's public-facing interfaces which could change without notice, potentially affecting the action's stability or causing errors.
*   **Changes Not Committed/Pushed:** Ensure the `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}` line is present in the commit step. This token is automatically provided by GitHub Actions and is necessary for the action to push changes back to your repository. Verify your repository settings allow Actions to create commits/pull requests if you have specific branch protection rules.
## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, please feel free to:

1.  Open an issue to discuss the change or report the bug.
2.  Fork the repository (`https://github.com/teraha-dev/statsfm-to-markdown/fork`).
3.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
4.  Make your changes.
5.  Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`).
6.  Push to the branch (`git push origin feature/AmazingFeature`).
7.  Open a Pull Request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

*   Inspired by the [lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) project.
