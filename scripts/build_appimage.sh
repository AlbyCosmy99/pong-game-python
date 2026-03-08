#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/build"
DIST_DIR="$ROOT_DIR/dist"
APPDIR="$BUILD_DIR/AppDir"
APPIMAGE_TOOL="$BUILD_DIR/tools/appimagetool.AppImage"
OUTPUT_FILE="$ROOT_DIR/Pong-x86_64.AppImage"
ICON_FILE="$BUILD_DIR/pong.png"

mkdir -p "$BUILD_DIR/tools"

if ! command -v pyinstaller >/dev/null 2>&1; then
  echo "pyinstaller non trovato nel PATH."
  exit 1
fi

if [[ ! -f "$APPIMAGE_TOOL" ]]; then
  echo "Scarico appimagetool..."
  curl -sS -L \
    "https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-x86_64.AppImage" \
    -o "$APPIMAGE_TOOL"
  chmod +x "$APPIMAGE_TOOL"
fi

echo "Genero icona..."
python3 "$ROOT_DIR/scripts/make_icon.py" "$ICON_FILE"

echo "Pulisco build precedenti..."
rm -rf "$BUILD_DIR/pyinstaller" "$APPDIR" "$DIST_DIR/Pong"
rm -f "$OUTPUT_FILE"

echo "Creo bundle PyInstaller..."
pyinstaller \
  --noconfirm \
  --clean \
  --distpath "$DIST_DIR" \
  --workpath "$BUILD_DIR/pyinstaller" \
  --specpath "$BUILD_DIR/pyinstaller" \
  --name "Pong" \
  --windowed \
  --onedir \
  --add-data "$ROOT_DIR/assets:assets" \
  "$ROOT_DIR/pong.py"

echo "Assemblo AppDir..."
mkdir -p "$APPDIR/usr/bin" "$APPDIR/usr/share/applications" "$APPDIR/usr/share/icons/hicolor/256x256/apps"
cp -a "$DIST_DIR/Pong/." "$APPDIR/usr/bin/"
cp "$ICON_FILE" "$APPDIR/usr/share/icons/hicolor/256x256/apps/pong.png"
cp "$ICON_FILE" "$APPDIR/pong.png"
ln -sf "pong.png" "$APPDIR/.DirIcon"

cat > "$APPDIR/AppRun" <<'EOF'
#!/bin/sh
HERE="$(dirname "$(readlink -f "$0")")"
exec "$HERE/usr/bin/Pong" "$@"
EOF
chmod +x "$APPDIR/AppRun"

cat > "$APPDIR/usr/share/applications/pong.desktop" <<'EOF'
[Desktop Entry]
Name=Pong
Exec=Pong
Icon=pong
Type=Application
Categories=Game;ArcadeGame;
Comment=Classic Pong built with Python and Pygame
Terminal=false
EOF

cp "$APPDIR/usr/share/applications/pong.desktop" "$APPDIR/pong.desktop"

echo "Genero AppImage..."
ARCH=x86_64 "$APPIMAGE_TOOL" --no-appstream "$APPDIR" "$OUTPUT_FILE"

rm -rf "$APPDIR" "$BUILD_DIR/pyinstaller" "$DIST_DIR/Pong"

echo "Creato: $OUTPUT_FILE"
