# Mermaid Gantt Chart Studio (Hybrid Editor)

A modern, offline Gantt chart maker that combines the power of **Mermaid.js** with a user-friendly GUI. This application allows you to create professional Gantt charts by either writing Mermaid code or using a visual interface, with real-time synchronization between both modes.

## Features
- **Dual-Mode Editing**:
  - **Code Editor**: Write raw Mermaid Gantt code with instant preview.
  - **GUI Editor**: Add sections and tasks using a visual form; changes are automatically converted to Mermaid code.
- **Real-Time Rendering**: See your chart update instantly as you type or edit.
- **Mermaid.js Power**: Use standard Mermaid syntax for dependencies, milestones, and styling.
- **Persistence**: Save and load your projects as JSON files.
- **Export**: Export your Mermaid code as a `.mmd` file for use in other tools (like GitHub or Notion).
- **Offline & Zero-Admin**: Runs as a local desktop app using `pywebview`, requiring no admin privileges for system DLLs.

## How to Run Locally
1.  **Install Python**: Ensure you have Python 3.11+ installed.
2.  **Install Dependencies**:
    ```bash
    pip install pywebview pyinstaller
    ```
3.  **Run the App**:
    ```bash
    python app.py
    ```

## How to Build the Windows .exe
To create a standalone executable for Windows:
1.  **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```
2.  **Run the Build Script**:
    ```bash
    python build_exe.py
    ```
3.  **Find the Executable**: After the build finishes, you will find `MermaidGanttStudio.exe` in the `dist/` folder.

## Project Structure
- `app.py`: Python backend and `pywebview` bridge.
- `index.html`: Hybrid HTML/JS/CSS frontend with Mermaid.js integration.
- `requirements.txt`: List of required Python packages.
- `build_exe.py`: Script to package the application into an `.exe`.
