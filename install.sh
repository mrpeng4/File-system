#!/bin/bash
set -e

TARGET_DIR="$HOME/Library/Application Support/pilu"
mkdir -p "$TARGET_DIR"

RAW_BASE_URL="https://raw.githubusercontent.com/mrpeng4/File-system/main"
FILES=("main.py" "functions.py" "Root.pilu" "User_data.pilu")

echo "Downloading pilu system files..."
for FILE in "${FILES[@]}"; do
    curl -fsSL "$RAW_BASE_URL/$FILE" -o "$TARGET_DIR/$FILE"
done

WRAPPER="/usr/local/bin/pilu"
echo "#!/bin/bash" | sudo tee $WRAPPER > /dev/null
echo "cd \"$TARGET_DIR\"" | sudo tee -a $WRAPPER > /dev/null
echo "python3 main.py \"\$@\"" | sudo tee -a $WRAPPER > /dev/null
sudo chmod +x $WRAPPER

echo "✅ All files installed successfully! Type 'pilu' in your terminal to start."
