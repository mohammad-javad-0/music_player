```markdown
# PyQt6 Music Player

This is a simple music player built using PyQt6, Pygame, and Mutagen. The application allows users to play, pause, and switch between music tracks stored in a specified directory. The UI is designed using PyQt6, providing an intuitive and user-friendly interface.

## Features

- **Play/Pause Music**: Start or pause the currently playing track with a single click.
- **Track Navigation**: Easily switch to the next or previous track in the playlist.
- **Track Display**: View the current track name and duration.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mohammad-javad-0/music_player.git
   cd pyqt6-music-player
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Music**:
   - Place your `.mp3` music files in the `music/` directory. The player will automatically detect and list them.

4. **Run the Application**:
   ```bash
   python main.py
   ```

## Dependencies

- **PyQt6**: For building the graphical user interface.
- **Pygame**: For handling audio playback.
- **Mutagen**: For extracting metadata from audio files (e.g., track length).

## Usage

- **Play/Pause**: Click the play/pause button to control playback.
- **Next/Previous Track**: Use the next and previous buttons to switch tracks.
- **Track Info**: The current track's name and duration are displayed at the top of the window.

## Contributing

Feel free to fork this project, submit issues, or contribute improvements. Contributions are welcome!
