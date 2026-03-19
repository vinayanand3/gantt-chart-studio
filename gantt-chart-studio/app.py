import webview
import json
import os
import sys
import base64

# When frozen by PyInstaller, bundled files live in sys._MEIPASS, not __file__'s dir.
def _resource(filename):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, filename)


class Api:
    def __init__(self):
        self.window = None  # set by run_app() after window creation

    def save_project(self, data):
        try:
            name = data.get("name", "project").replace(" ", "_")
            result = self.window.create_file_dialog(
                webview.SAVE_DIALOG,
                save_filename=f"{name}.json",
                file_types=('JSON Files (*.json)', 'All files (*.*)')
            )
            if not result:
                return {"status": "cancelled"}
            file_path = result[0] if isinstance(result, (list, tuple)) else result
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return {"status": "success", "path": file_path}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def load_project(self):
        try:
            result = self.window.create_file_dialog(
                webview.OPEN_DIALOG,
                file_types=('JSON Files (*.json)', 'All files (*.*)')
            )
            if not result:
                return {"status": "cancelled"}
            file_path = result[0] if isinstance(result, (list, tuple)) else result
            if not os.path.exists(file_path):
                return {"status": "error", "message": "File not found"}
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return {"status": "success", "data": data}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def export_mermaid(self, code):
        try:
            result = self.window.create_file_dialog(
                webview.SAVE_DIALOG,
                save_filename='gantt-chart.mmd',
                file_types=('Mermaid Files (*.mmd)', 'Text Files (*.txt)', 'All files (*.*)')
            )
            if not result:
                return {"status": "cancelled"}
            file_path = result[0] if isinstance(result, (list, tuple)) else result
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            return {"status": "success", "path": file_path}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def export_image(self, data_url, format_type):
        try:
            ext = f".{format_type.lower()}"
            result = self.window.create_file_dialog(
                webview.SAVE_DIALOG,
                save_filename=f"gantt-chart{ext}",
                file_types=(f'{format_type.upper()} Files (*{ext})', 'All files (*.*)')
            )
            if not result:
                return {"status": "cancelled"}
            file_path = result[0] if isinstance(result, (list, tuple)) else result
            header, encoded = data_url.split(",", 1)
            raw = base64.b64decode(encoded)
            if format_type.lower() == 'svg':
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(raw.decode('utf-8'))
            else:
                with open(file_path, 'wb') as f:
                    f.write(raw)
            return {"status": "success", "path": file_path}
        except Exception as e:
            return {"status": "error", "message": str(e)}


def run_app():
    api = Api()
    html_path  = _resource('index.html')
    icon_path  = _resource('app_icon.ico')

    window = webview.create_window(
        'Gantt Chart Studio',
        html_path,
        js_api=api,
        width=1400,
        height=900
    )
    api.window = window  # give the API a reference to call create_file_dialog

    if os.path.exists(icon_path):
        webview.start(icon=icon_path)
    else:
        webview.start()


if __name__ == '__main__':
    run_app()
