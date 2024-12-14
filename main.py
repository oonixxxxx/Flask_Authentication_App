from concurrent.futures import ThreadPoolExecutor
import threading
from flask import Flask, render_template
import time

app = Flask(__name__)

# Блокировка для безопасного доступа к общим ресурсам
lock = threading.Lock()

# Класс для обработки данных
class DataProcessor:
    def __init__(self):
        self.data = []
    
    # Метод для параллельной обработки данных
    def process_chunk(self, chunk):
        """
        Обрабатывает часть данных в отдельном потоке
        :param chunk: часть данных для обработки
        :return: обработанные данные
        """
        result = []
        for item in chunk:
            # Имитация сложной обработки
            time.sleep(0.1)
            result.append(item * 2)
        return result

    # Метод для параллельной обработки всего массива данных
    def process_data_parallel(self, input_data, max_workers=4):
        """
        Параллельная обработка всего массива данных
        :param input_data: входные данные
        :param max_workers: максимальное количество потоков
        :return: обработанные данные
        """
        # Разделение данных на части для параллельной обработки
        chunk_size = len(input_data) // max_workers
        chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]
        
        # Использование пула потоков для параллельной обработки
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self.process_chunk, chunks))
        
        # Объединение результатов
        return [item for sublist in results for item in sublist]

@app.route('/')
def index():
    """
    Главная страница приложения
    """
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """
    Обработка данных с использованием многопоточности
    """
    processor = DataProcessor()
    
    # Пример данны�� для обработки
    test_data = list(range(100))
    
    # Параллельная обработка данных
    with lock:
        result = processor.process_data_parallel(test_data)
    
    return {'result': result}

if __name__ == '__main__':
    # Заменяем параметры запуска для работы в Docker
    app.run(host='0.0.0.0', port=5000, threaded=True)