#import modules.fast_api_module.fast_api_module
import subprocess

#def run_another_script(script_path, *args):
#    try:
#        result = subprocess.run(['python', script_path] + list(args), capture_output=True, text=True, check=True)
#        print(f"Результат выполнения скрипта {script_path}:")
#        print(result.stdout)
#        if result.stderr:
#            print(f"Ошибки: {result.stderr}")
#    except subprocess.CalledProcessError as e:
#        print(f"Ошибка при выполнении скрипта {script_path}: {e}")
#        print(f"Статус ошибки: {e.returncode}")
#        print(f"Вывод ошибок: {e.stderr}")
#    except FileNotFoundError:
#        print(f"Ошибка: Скрипт не найден: {script_path}")
#
#app = run_another_script('modules/fast_api_module/fast_api_module.py')

import uvicorn
from modules.fast_api_module.fast_api_module import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1:8000")