# Gantt Chart Studio

A desktop application for creating, editing, and exporting professional Gantt charts — built with Python and Mermaid.js. No internet connection required after install.

![Gantt Chart Studio](https://raw.githubusercontent.com/vinaybhaskarla/gantt-chart-studio/main/screenshot.png)

---

## Features

- **Visual Editor** — Add sections and tasks through a point-and-click interface, no code required
- **Live Code Editor** — Edit Mermaid Gantt syntax directly and see changes in real time
- **Milestone Support** — Mark key events as diamond milestones on the timeline
- **Chart Settings** — Control title, date format, axis format, theme, font size, weekends, and today marker
- **Drag-to-Resize Panes** — Adjust the editor, code, and preview pane widths freely
- **Export Options**
  - **SVG** — Vector format, imports correctly into Excel, PowerPoint, and Illustrator (milestones render as diamonds)
  - **PNG** — High-resolution 2× retina-quality image
  - **.mmd** — Raw Mermaid source file
- **Save / Load** — Save your project as a JSON file and reload it anytime
- **5 Themes** — Default, Neutral, Dark, Forest, Base
- **Dependency Syntax** — Set task start as a date (`2026-03-01`) or a dependency (`after taskId`)

---

## Quick Start (Run from Source)

### Requirements

- Python 3.9 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/vinayanand3/gantt-chart-studio.git
cd gantt-chart-studio

# Install dependencies
pip install pywebview

# Run the app
python app.py
```

The app window will open automatically.

---

## Build a Windows Executable (.exe)

Follow these steps on your **Windows machine** to produce a standalone `GanttChartStudio.exe` that anyone can run without installing Python.

### Step 1 — Install build dependencies

```bash
pip install pywebview pyinstaller pyinstaller-hooks-contrib
```

### Step 2 — Run the build script

```bash
python build_exe.py
```

The build will take a minute. When it finishes, the executable is at:

```
dist/GanttChartStudio.exe
```

### Step 3 — Distribute

Share `GanttChartStudio.exe` directly. No installer needed.

> **Note:** The target Windows machine must have the **Microsoft WebView2 Runtime** installed.
> - It comes pre-installed on **Windows 11** and most updated **Windows 10** machines.
> - If missing, download the Evergreen installer from:
>   https://developer.microsoft.com/en-us/microsoft-edge/webview2/

---

## Project Structure

```
gantt-chart-studio/
├── app.py          # Python backend (pywebview, file save/load/export)
├── index.html      # Entire frontend (HTML + CSS + JavaScript)
├── build_exe.py    # PyInstaller build script for Windows
├── app_icon.ico    # Application icon
└── README.md
```

---

## How to Use

### Creating a Chart

1. **Chart Settings** (top of the left panel) — Set the chart title, date format, axis format, font size, and theme
2. **Add a Section** — Click **+ Add Section** at the bottom of the Sections & Tasks panel
3. **Add Tasks** — Click **+ Add Task** inside any section; fill in the task name, status, ID, start date or dependency, and duration
4. **Milestones** — Set the task type to **Milestone** in the status dropdown

### Editing Directly in Code

Click **Code** in the top tab bar to switch to the raw Mermaid editor. Changes sync back to the visual editor when you click **Sync**.

### Exporting

Use the buttons in the top-right corner:
| Button | Output |
|--------|--------|
| SVG | Vector file — best for Excel / PowerPoint |
| PNG | High-resolution image |
| .mmd | Mermaid source file |
| Save | Save project as JSON |
| Load | Reload a previously saved JSON |

### Axis Format Options

| Display | Format Code |
|---------|-------------|
| 01/26 — MM/YY | `%m/%y` |
| Jan 26 — Mon/YY | `%b/%y` |
| Jan 15 — Mon DD | `%b %d` |
| 15/01 — DD/MM | `%d/%m` |
| Jan 2026 — Month Year | `%b %Y` |
| 2026-01-15 — Full ISO | `%Y-%m-%d` |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| [pywebview](https://pywebview.flowrl.com/) | Desktop window with embedded browser |
| [Mermaid.js](https://mermaid.js.org/) | Gantt chart rendering (loaded via CDN) |
| [Flatpickr](https://flatpickr.js.org/) | Date picker for task start dates |

---

## License

MIT — free to use, modify, and distribute.

---

*Created by Vinay Bhaskarla*
