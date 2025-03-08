#!/bin/bash

# Get script name dynamically
SCRIPT_NAME="$(basename "$0")"

# Get absolute paths
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd -P)"
APP_DIR="$PROJECT_DIR/app"
LOG_DIR="$PROJECT_DIR/log"
PID_DIR="$PROJECT_DIR/pid"
VENV_DIR="$PROJECT_DIR/venv"
GOOGLE_CREDENTIALS="$PROJECT_DIR/f1-driver-registry-b91545d3ebfc.json"  # Firebase Admin SDK credentials

# Ensure log and pid directories exist
mkdir -p "$LOG_DIR"
mkdir -p "$PID_DIR"

# File paths
APP_MAIN="$APP_DIR/app_main.py"
UI_MAIN="$APP_DIR/ui_main.py"
REQUIREMENTS="$PROJECT_DIR/requirements.txt"

APP_LOG="$LOG_DIR/app_main.log"
UI_LOG="$LOG_DIR/ui_main.log"
APP_PID_FILE="$PID_DIR/app_main.pid"
UI_PID_FILE="$PID_DIR/ui_main.pid"

# Firebase Project ID
FIREBASE_PROJECT_ID="f1-driver-registry"

# Function to check Google Cloud authentication
check_gcloud_auth() {
    echo "[$SCRIPT_NAME] Checking Google Cloud authentication..."

    if ! gcloud auth list --format="value(account)" | grep -q "@"; then
        echo "[$SCRIPT_NAME] Google Cloud authentication required. Logging in..."
        gcloud auth login
    else
        echo "✅ [$SCRIPT_NAME] Google Cloud is already authenticated."
    fi

    # Set Firebase project
    echo "[$SCRIPT_NAME] Setting Firebase project to $FIREBASE_PROJECT_ID..."
    gcloud config set project "$FIREBASE_PROJECT_ID"

    # Ensure Firebase CLI is installed
    if ! command -v firebase &> /dev/null; then
        echo "[$SCRIPT_NAME] Installing Firebase CLI..."
        npm install -g firebase-tools
    else
        echo "✅ [$SCRIPT_NAME] Firebase CLI is installed."
    fi

    # Authenticate Firebase
    if ! firebase login --no-localhost --check; then
        echo "[$SCRIPT_NAME] Logging into Firebase..."
        firebase login --no-localhost
    else
        echo "✅ [$SCRIPT_NAME] Firebase is already authenticated."
    fi

    # Ensure Firebase Admin SDK credentials are set
    if [ -f "$GOOGLE_CREDENTIALS" ]; then
        export GOOGLE_APPLICATION_CREDENTIALS="$GOOGLE_CREDENTIALS"
        echo "✅ [$SCRIPT_NAME] Using Firebase Admin SDK credentials from $GOOGLE_CREDENTIALS"
    else
        echo "⚠️ [$SCRIPT_NAME] WARNING: Firebase Admin SDK credentials file not found: $GOOGLE_CREDENTIALS"
        echo "Please ensure that $GOOGLE_CREDENTIALS exists in the project root."
        exit 1
    fi
}

# Create and activate virtual environment
setup_venv() {
    if [ ! -d "$VENV_DIR" ]; then
        echo "[$SCRIPT_NAME] Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
        echo "[$SCRIPT_NAME] Installing dependencies..."
        "$VENV_DIR/bin/pip3" install --upgrade pip
        "$VENV_DIR/bin/pip3" install -r "$REQUIREMENTS"
    else
        echo "✅ [$SCRIPT_NAME] Virtual environment already exists."
    fi
}

# Start servers
start_servers() {
    echo "[$SCRIPT_NAME] Starting FastAPI server..."
    PYTHONPATH="$PROJECT_DIR" nohup "$VENV_DIR/bin/python3" "$APP_MAIN" > "$APP_LOG" 2>&1 & echo $! > "$APP_PID_FILE"

    echo "[$SCRIPT_NAME] Starting NiceGUI server..."
    PYTHONPATH="$PROJECT_DIR" nohup "$VENV_DIR/bin/python3" "$UI_MAIN" > "$UI_LOG" 2>&1 & echo $! > "$UI_PID_FILE"

    sleep 2  # Allow servers to start
    status_servers  # Verify servers are running
}

# Stop servers
stop_servers() {
    if [ -f "$APP_PID_FILE" ]; then
        kill "$(cat "$APP_PID_FILE")" 2>/dev/null
        rm -f "$APP_PID_FILE"
        echo "✅ [$SCRIPT_NAME] FastAPI server stopped."
    else
        echo "[$SCRIPT_NAME] FastAPI server is not running."
    fi

    if [ -f "$UI_PID_FILE" ]; then
        kill "$(cat "$UI_PID_FILE")" 2>/dev/null
        rm -f "$UI_PID_FILE"
        echo "✅ [$SCRIPT_NAME] NiceGUI server stopped."
    else
        echo "[$SCRIPT_NAME] NiceGUI server is not running."
    fi
}

# Restart servers
restart_servers() {
    echo "[$SCRIPT_NAME] Restarting both servers..."
    stop_servers
    sleep 2
    start_servers
}

# Check server status
status_servers() {
    if [ -f "$APP_PID_FILE" ] && kill -0 "$(cat "$APP_PID_FILE")" 2>/dev/null; then
        echo "✅ [$SCRIPT_NAME] FastAPI server is running (PID: $(cat "$APP_PID_FILE"))."
    else
        echo "❌ [$SCRIPT_NAME] FastAPI server is NOT running. Check logs: $APP_LOG"
    fi

    if [ -f "$UI_PID_FILE" ] && kill -0 "$(cat "$UI_PID_FILE")" 2>/dev/null; then
        echo "✅ [$SCRIPT_NAME] NiceGUI server is running (PID: $(cat "$UI_PID_FILE"))."
    else
        echo "❌ [$SCRIPT_NAME] NiceGUI server is NOT running. Check logs: $UI_LOG"
    fi
}

# Run Google Cloud & Firebase authentication (ONLY ONCE)
check_gcloud_auth

# Run setup
setup_venv

# Start servers initially
start_servers

# Display menu and wait for user input
echo -e "\n[$SCRIPT_NAME] Server Control Menu"
echo "===================================="
echo "s - Check server status"
echo "r - Restart both servers"
echo "q - Quit and stop both servers"
echo ""

while true; do
    read -p "[$SCRIPT_NAME] Enter command (s/r/q): " cmd
    case "$cmd" in
        s) status_servers ;;
        r) restart_servers ;;
        q) stop_servers; exit 0 ;;
        *) echo "[$SCRIPT_NAME] Invalid command. Use s, r, or q." ;;
    esac
done
