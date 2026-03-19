import PyInstaller.__main__
import os
import sys

def build():
    # Define the main script
    main_script = "app.py"
    
    # Define the icon file
    icon_file = "app_icon.ico"
    
    # Determine the separator for --add-data based on the OS
    # Windows uses ';', Linux/macOS uses ':'
    separator = ';' if sys.platform == 'win32' else ':'
    
    # Define PyInstaller arguments
    args = [
        main_script,
        "--onefile",                              # Single executable
        "--windowed",                             # No console window
        "--name=GanttChartStudio",                # Executable name
        f"--add-data=index.html{separator}.",     # Bundle HTML
        f"--add-data={icon_file}{separator}.",    # Bundle icon for runtime
        f"--icon={icon_file}",                    # Executable icon
        "--clean",                                # Clean cache before build
        # pywebview Windows dependencies (EdgeChromium / WebView2 backend)
        "--hidden-import=webview.platforms.winforms",
        "--hidden-import=webview.platforms.edgechromium",
        "--hidden-import=clr",
        "--collect-all=webview",
    ]
    
    print(f"Building executable with icon: {icon_file}...")
    
    # Run PyInstaller
    PyInstaller.__main__.run(args)

if __name__ == "__main__":
    build()
