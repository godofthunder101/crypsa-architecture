@echo off
setlocal
cd /d "%~dp0"

py -m mint.mint_catalog_editor %*
if %errorlevel% equ 0 goto :eof

python -m mint.mint_catalog_editor %*
