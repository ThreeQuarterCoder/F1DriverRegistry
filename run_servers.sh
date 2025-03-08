#!/bin/bash

APP_MAIN="app/app_main.py"
UI_MAIN="app/ui_main.py"
APP_LOG="log/app_main.log"
UI_LOG="log/ui_main.log"
APP_PID_FILE="pid/app_main.pid"
UI_PID_FILE="pid/ui_main.pid"

start_servers() {
    echo "Starting FastAPI server..."
    nohup python3 $APP_MAIN > $APP_LOG 2>&1 &
    echo $! > $APP_PID_FILE

    echo "Starting NiceGUI server..."
    nohup python3 $UI_MAIN > $UI_LOG 2>&1 &
    echo $! > $UI_PID_FILE

    echo "Servers started successfully."
}

stop_servers() {
    if [ -f $APP_PID_FILE ]; then
        kill $(cat $APP_PID_FILE)
        rm $APP_PID_FILE
        echo "FastAPI server stopped."
    else
        echo "FastAPI server is not running."
    fi

    if [ -f $UI_PID_FILE ]; then
        kill $(cat $UI_PID_FILE)
        rm $UI_PID_FILE
        echo "NiceGUI server stopped."
    else
        echo "NiceGUI server is not running."
    fi
}

restart_servers() {
    stop_servers
    sleep 2
    start_servers
}

status_servers() {
    if [ -f $APP_PID_FILE ] && kill -0 $(cat $APP_PID_FILE) 2>/dev/null; then
        echo "FastAPI server is running (PID: $(cat $APP_PID_FILE))."
    else
        echo "FastAPI server is NOT running."
    fi

    if [ -f $UI_PID_FILE ] && kill -0 $(cat $UI_PID_FILE) 2>/dev/null; then
        echo "NiceGUI server is running (PID: $(cat $UI_PID_FILE))."
    else
        echo "NiceGUI server is NOT running."
    fi
}

menu() {
    echo "Server Control Menu"
    echo "==================="
    echo "s - Check server status"
    echo "r - Restart both servers"
    echo "q - Quit and stop both servers"
    echo ""

    while true; do
        read -p "Enter command: " cmd
        case $cmd in
            s) status_servers ;;
            r) restart_servers ;;
            q) stop_servers; exit 0 ;;
            *) echo "Invalid command. Use s, r, or q." ;;
        esac
    done
}

start_servers
menu
