@echo off
echo Starting server
start cmd /k servez

echo Opening browser
start "" "http://127.0.0.1:8080"

pause >nul