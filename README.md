# statsfm-to-markdown 🎵

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-statsfm--to--markdown-green?style=flat-square&logo=github)](https://github.com/marketplace/actions/statsfm-to-markdown)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://github.com/teraha-dev/statsfm-to-markdown/blob/main/LICENSE)
[![Action Build Status](https://github.com/teraha-dev/statsfm-to-markdown/actions/workflows/statsfm.yml/badge.svg)](https://github.com/teraha-dev/statsfm-to-markdown/actions/workflows/statsfm.yml)
[![Sponsor](https://img.shields.io/github/sponsors/teraha-dev?style=flat-square)](https://github.com/sponsors/teraha-dev)

A GitHub Action that fetches your top albums from [stats.fm](https://stats.fm/) (formerly Spotistats) for a specified time range and displays them as linked images with tooltips on your GitHub profile README. Inspired by the [lastfm-to-markdown](https://github.com/lastfm-to-markdown/lastfm-to-markdown) project.

---

## ✨ Example Output Section

This action will find the following markers in your README file and automatically insert the generated list of your top albums between them:

<!-- STATSFM START -->

<p align="center"><a href="https://open.spotify.com/album/3GH4IiI6jQAIvnHVdb5FB6" target="_blank" rel="noopener noreferrer" title="#1 my bloody valentine - Loveless (8h 29m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/d8/9c/a2/d89ca2ad-3191-d877-4c2f-13fb3e619a7b/887830015998.png/768x768bb.jpg" alt="my bloody valentine - Loveless" width="100" height="100"></a>    <a href="https://open.spotify.com/album/1NRRN5RWwfuLmQdjshz0L7" target="_blank" rel="noopener noreferrer" title="#2 Kanye West - The College Dropout (Explicit) (3h 31m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/15/05/09/15050911-a2f1-9ebc-0d16-6e8faad1cf80/00602567924326.rgb.jpg/768x768bb.jpg" alt="Kanye West - The College Dropout (Explicit)" width="100" height="100"></a>    <a href="https://open.spotify.com/album/1p12OAWwudgMqfMzjMvl2a" target="_blank" rel="noopener noreferrer" title="#3 A Tribe Called Quest - The Low End Theory (3h 26m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/e0/14/c8/e014c80a-425b-e01a-1124-cee985bcb5e6/dj.qafpkddz.jpg/768x768bb.jpg" alt="A Tribe Called Quest - The Low End Theory" width="100" height="100"></a>    <a href="https://open.spotify.com/album/6r7LZXAVueS5DqdrvXJJK7" target="_blank" rel="noopener noreferrer" title="#4 Black Sabbath - Paranoid (Remaster) (3h 17m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/93/74/16/93741672-cedb-1850-dcd9-113a374336d6/4050538642872.jpg/768x768bb.jpg" alt="Black Sabbath - Paranoid (Remaster)" width="100" height="100"></a>    <a href="https://open.spotify.com/album/3539EbNgIdEDGBKkUf4wno" target="_blank" rel="noopener noreferrer" title="#5 Portishead - Dummy (3h 1m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/c1/71/93/c1719342-df7d-e9c5-c87c-53dae5afb289/00042282855329.rgb.jpg/768x768bb.jpg" alt="Portishead - Dummy" width="100" height="100"></a>    <a href="https://open.spotify.com/album/6klUp8sQyRXGuJhqZu4PG3" target="_blank" rel="noopener noreferrer" title="#6 Kanye West - My Beautiful Dark Twisted Fantasy (2h 41m)"><img src="https://i.scdn.co/image/ab67616d0000b273baf2a68126739ff553f2930a" alt="Kanye West - My Beautiful Dark Twisted Fantasy" width="100" height="100"></a></p>
<p align="center"><a href="https://open.spotify.com/album/67Yc6dfTWwuPceZRK7sluD" target="_blank" rel="noopener noreferrer" title="#7 Madvillain - Madvillainy (2h 31m)"><img src="https://i.scdn.co/image/ab67616d0000b2739c7052b4aa3ccacc215e2584" alt="Madvillain - Madvillainy" width="100" height="100"></a>    <a href="https://open.spotify.com/album/4v5x3Oo3UjQ9YmF3hRAip5" target="_blank" rel="noopener noreferrer" title="#8 A Tribe Called Quest - Midnight Marauders (2h 25m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/d1/90/11/d1901153-4595-7f2f-12d2-661be9eef883/012414149022.jpg/768x768bb.jpg" alt="A Tribe Called Quest - Midnight Marauders" width="100" height="100"></a>    <a href="https://open.spotify.com/album/6geDeresfKATEklDXuXY93" target="_blank" rel="noopener noreferrer" title="#9 Sweet Trip - Velocity:design:comfort (2h 25m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/c3/e8/4c/c3e84cec-9489-62af-2fad-4c76cc4836e7/mzi.dlnvjlfx.jpg/768x768bb.jpg" alt="Sweet Trip - Velocity:design:comfort" width="100" height="100"></a>    <a href="https://open.spotify.com/album/2udRJgUgrKM9lC89mSGE71" target="_blank" rel="noopener noreferrer" title="#10 Sheena Ringo - 無罪モラトリアム (2h 20m)"><img src="https://i.scdn.co/image/ab67616d0000b2732eec7a5b51cfdf286683dccb" alt="Sheena Ringo - 無罪モラトリアム" width="100" height="100"></a>    <a href="https://open.spotify.com/album/30zwjSQEodaUXCn11nmiVF" target="_blank" rel="noopener noreferrer" title="#11 Kanye West - VULTURES 1 (2h 18m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music122/v4/97/a9/17/97a91772-2c73-ef8c-8936-689daa2ea5ed/cover.jpg/768x768bb.jpg" alt="Kanye West - VULTURES 1" width="100" height="100"></a>    <a href="https://open.spotify.com/album/3WvQpufOsPzkZvcSuynCf3" target="_blank" rel="noopener noreferrer" title="#12 A Tribe Called Quest - We got it from Here... Thank You 4 Your service (2h 17m)"><img src="https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/68/d3/ce/68d3ce5e-9465-4c77-60a6-496417e35308/886446074757.jpg/768x768bb.jpg" alt="A Tribe Called Quest - We got it from Here... Thank You 4 Your service" width="100" height="100"></a></p>
<!-- STATSFM END -->

*(The actual content generated by the workflow will appear between these markers, displaying linked album covers. Hovering over an image will show a tooltip with the artist, album title, and optionally the rank and playtime, if configured.)*

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
          contents: write # Required to push changes back to the repository
        steps:
          # Check out the repository code
          - name: Checkout code
            uses: actions/checkout@v4

          # Run the statsfm-to-markdown action
          - name: Update stats.fm top albums
            uses: teraha-dev/statsfm-to-markdown@v1.0.1 # Use the latest release tag (e.g., @v1.0.1)
            with:
              # REQUIRED: Your stats.fm username
              statsfm_username: 'YOUR_STATSFM_USERNAME' # Replace with your actual username

              # OPTIONAL: Customize the display (see Inputs below)
              display_limit: '10'        # Number of albums to show (max 50)
              time_range: 'weeks'       # Data period: weeks, months, lifetime
              show_rank: 'true'         # Include rank number in tooltip: true, false
              show_duration: 'true'     # Include playtime in tooltip: true, false
              readme_path: 'README.md'  # Path to your README file
              items_per_row: '5'        # Number of albums to display per row

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

| Input             | Description                                                         | Required | Default    | Options                     |
| :---------------- | :------------------------------------------------------------------ | :------- | :--------- | :-------------------------- |
| `statsfm_username`| Your username on stats.fm.                                          | **`true`** | `N/A`      |                             |
| `display_limit`   | The maximum number of albums to display.                            | `false`  | `10`       | `1` to `50`                 |
| `show_duration`   | Whether to include the total playtime in the image tooltip.           | `false`  | `true`     | `true`, `false`             |
| `show_rank`       | Whether to include the ranking number (#1, #2...) in the image tooltip. | `false`  | `true`     | `true`, `false`             |
| `time_range`      | The time period for fetching top albums data.                       | `false`  | `weeks`    | `weeks`, `months`, `lifetime` |
| `readme_path`     | The path to the README file that needs to be updated.               | `false`  | `README.md`|                             |
| `items_per_row`   | The maximum number of albums to display in a single row.            | `false`  | `5`| `1 to 50` |

## 🛠️ Configuration Examples

**Basic Setup (Default Settings):**
Shows the top 10 albums from the last few weeks. Tooltips will include rank and duration.

```yaml
- name: Update stats.fm top albums
  uses: teraha-dev/statsfm-to-markdown@v1.0.1
  with:
    statsfm_username: 'your_username'
```

**Customized Setup (Top 5 Albums, Lifetime, No Rank/Duration in Tooltip):**
Shows the top 5 albums from all time, hiding the rank and duration in the tooltips.

```yaml
- name: Update stats.fm top albums
  uses: teraha-dev/statsfm-to-markdown@v1.0.1
  with:
    statsfm_username: 'your_username'
    display_limit: '5'
    time_range: 'lifetime'
    show_rank: 'false'
    show_duration: 'false'
    items_per_row: '5'
```

**Updating a Different File:**
Updates a file named `PROFILE.md` instead of the default `README.md`.

```yaml
- name: Update stats.fm top albums in PROFILE.md
  uses: teraha-dev/statsfm-to-markdown@v1.0.1
  with:
    statsfm_username: 'your_username'
    readme_path: 'PROFILE.md' # Don't forget to add the markers in PROFILE.md too!
```

## 🤔 Troubleshooting

*   **Workflow Not Running:** Ensure the workflow file (`.github/workflows/statsfm.yml`) is correctly placed in the `.github/workflows/` directory and has been pushed to your default branch (usually `main` or `master`). Check the Actions tab in your repository for run logs.
*   **Markers Not Found Error:** Double-check that `<!-- STATSFM START -->` and `<!-- STATSFM END -->` markers exist exactly as shown (case-sensitive) on separate lines within your `README.md` file (or the file specified in `readme_path`). The START marker must appear before the END marker. Ensure there are blank lines before the START marker and after the END marker if they are near other content.
*   **Invalid Username Error:** Verify that the `statsfm_username` provided in the workflow file is your correct stats.fm username.
*   **API Errors / No Albums Displayed:**
    *   The stats.fm API might be temporarily unavailable. Check the workflow logs for specific error messages (like HTTP status codes).
    *   Ensure you have listening history on stats.fm for the selected `time_range`. If `time_range` is `weeks` or `months`, you need recent plays.
    *   The action filters out albums if they lack essential data from the API (e.g., image URL). Try increasing the `display_limit` slightly, as the API might return items that cannot be displayed.
    *   **Note:** This action relies on stats.fm's public-facing interfaces which could change without notice, potentially affecting the action's stability or causing errors.
*   **Changes Not Committed/Pushed:**
    *   Ensure the `permissions: contents: write` line is present in your workflow job configuration, as shown in the usage example.
    *   Ensure the `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}` line is present in the commit step's environment variables.
    *   Verify your repository settings (Settings > Actions > General > Workflow permissions) allow Actions to create commits/pull requests if you have specific branch protection rules that might interfere.

## 🤝 Contributing

Contributions are welcome! If you find this action useful, please consider [sponsoring the developer](https://github.com/sponsors/teraha-dev)!

If you have suggestions for improvements or find a bug, please feel free to:

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
