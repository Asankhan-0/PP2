import json
import os

SETTINGS_FILE = "settings.json"

# Настройки по умолчанию
DEFAULT_SETTINGS = {
    "snake_color": [0, 255, 0],   # зелёный
    "grid_overlay": False,
    "sound": False
}


def load_settings():
    """Загрузить настройки из файла"""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                settings = json.load(f)
                # Если каких-то ключей нет - добавляем дефолтные
                for key, value in DEFAULT_SETTINGS.items():
                    if key not in settings:
                        settings[key] = value
                return settings
        except Exception as e:
            print(f"Ошибка загрузки настроек: {e}")
    return DEFAULT_SETTINGS.copy()


def save_settings(settings):
    """Сохранить настройки в файл"""
    try:
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=4)
    except Exception as e:
        print(f"Ошибка сохранения настроек: {e}")
