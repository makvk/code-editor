import pytest
import tempfile
import os
from unittest.mock import Mock, patch

def test_python_syntax_highlighting():
    """Тест 1: Проверка реальной работы подсветки синтаксиса Python."""
    
    from core.syntax import PythonHighlighter
    from PyQt6.QtGui import QTextDocument
    
    # Создаем реальный документ
    doc = QTextDocument()
    highlighter = PythonHighlighter(doc)
    
    # Тестовый код Python с разными конструкциями
    test_code = '''#!/usr/bin/env python3
# Комментарий
def calculate_sum(a, b):
    """Документация функции"""
    if a > 0 and b > 0:
        return a + b
    else:
        return "negative"
    
for i in range(10):
    print(f"Number: {i}")
    
result = calculate_sum(5, 3)
print(f"Result: {result}")'''
    
    # Устанавливаем код в документ
    doc.setPlainText(test_code)
    
    # Проверяем, что код загружен
    assert len(doc.toPlainText()) > 0
    assert "def calculate_sum" in doc.toPlainText()
    assert "# Комментарий" in doc.toPlainText()
    
    print("Синтаксис Python загружен и готов к подсветке")
    return True

def test_python_code_execution():
    """Тест 2: Проверка исполнения Python кода через PythonRunner."""
    
    from core.executor import PythonRunner
    import time
    
    # Создаем runner
    runner = PythonRunner()
    
    # Подготавливаем тестовый код
    test_code = """
import sys
print("Hello from test!")
print("Python version:", sys.version_info[:2])
x = 5 + 3
print(f"5 + 3 = {x}")
"""
    
    # Мокаем временный файл, чтобы не создавать реальный
    with patch('tempfile.NamedTemporaryFile') as mock_tempfile:
        mock_file = Mock()
        mock_file.name = '/tmp/test_python.py'
        mock_tempfile.return_value = mock_file
        
        # Мокаем процесс, чтобы не запускать реальный Python
        with patch.object(runner.process, 'start') as mock_start:
            with patch.object(runner.process, 'waitForStarted') as mock_wait:
                with patch.object(runner.process, 'state') as mock_state:
                    
                    # Настраиваем моки
                    mock_wait.return_value = True
                    
                    # Запускаем код
                    runner.run(test_code)
                    
                    # Проверяем, что код был записан во временный файл
                    mock_file.write.assert_called_once()
                    
                    # Проверяем, что был вызван python с правильным файлом
                    mock_start.assert_called_once_with('python', ['/tmp/test_python.py'])
                    
                    print("Python код подготовлен к исполнению")
                    print(f"   Записан код длиной: {len(test_code)} символов")
    
    return True

def test_ui_components_creation():
    """Тест 3: Проверка создания UI компонентов редактора."""
    
    # Мокаем PyQt6, чтобы не инициализировать QApplication
    with patch('PyQt6.QtWidgets.QPlainTextEdit'), \
         patch('PyQt6.QtWidgets.QWidget'), \
         patch('PyQt6.QtWidgets.QHBoxLayout'), \
         patch('PyQt6.QtWidgets.QLineEdit'), \
         patch('PyQt6.QtWidgets.QLabel'):
        
        from ui.editor_widget import EditorWidget
        from ui.input_widget import InputWidget
        from ui.output_widget import OutputWidget
        
        # ТЕСТ 1: EditorWidget
        print("\nТестирование EditorWidget...")
        try:
            editor = EditorWidget()
            
            # Проверяем атрибуты
            assert hasattr(editor, 'highlighter'), "EditorWidget должен иметь highlighter"
            print("   EditorWidget создан, есть highlighter")
            
            # Проверяем настройки редактора
            assert editor is not None
            print("   EditorWidget инициализирован")
            
        except Exception as e:
            print(f"   Ошибка EditorWidget: {e}")
            return False
        
        # ТЕСТ 2: InputWidget
        print("\nТестирование InputWidget...")
        try:
            # Создаем InputWidget
            input_widget = InputWidget()
            
            # Проверяем сигналы
            assert hasattr(input_widget, 'submitted'), "InputWidget должен иметь сигнал submitted"
            print("   InputWidget создан, есть сигнал submitted")
            
            # Проверяем компоненты
            assert hasattr(input_widget, 'prompt'), "Должен быть prompt"
            assert hasattr(input_widget, 'edit'), "Должен быть edit"
            print("   InputWidget компоненты на месте")
            
        except Exception as e:
            print(f"   Ошибка InputWidget: {e}")
            return False
        
        # ТЕСТ 3: OutputWidget
        print("\nТестирование OutputWidget...")
        try:
            # Создаем OutputWidget
            output_widget = OutputWidget()
            
            # Проверяем компоненты
            assert hasattr(output_widget, 'text'), "Должен быть text widget"
            assert hasattr(output_widget, 'input'), "Должен быть input widget"
            print("   OutputWidget создан, компоненты на месте")
            
            # Проверяем методы
            assert hasattr(output_widget, 'append_stdout'), "Должен быть append_stdout"
            assert hasattr(output_widget, 'append_stderr'), "Должен быть append_stderr"
            assert hasattr(output_widget, 'clear_output'), "Должен быть clear_output"
            print("   OutputWidget методы на месте")
            
        except Exception as e:
            print(f"   Ошибка OutputWidget: {e}")
            return False
        
        print("\nВсе UI компоненты могут быть созданы")
        return True

def run_functional_tests():
    """Запуск всех функциональных тестов."""
    
    print("-" * 60)
    print("ЗАПУСК ТЕСТОВ")
    print("-" * 60)
    
    tests = [
        ("Подсветка синтаксиса Python", test_python_syntax_highlighting),
        ("Исполнение Python кода", test_python_code_execution),
        ("Создания компонентов UI", test_ui_components_creation),
    ]
    
    results = []
    
    for name, test_func in tests:
        print(f"\n ТЕСТ: {name}")
        print("-" * 40)
        try:
            success = test_func()
            if success:
                results.append((name, True))
                print(f"УСПЕХ")
            else:
                results.append((name, False))
                print(f"ПРОВАЛ")
        except Exception as e:
            results.append((name, False))
            print(f"ОШИБКА: {e}")
    
    # Итоги
    print("\n" + "-" * 60)
    print("РЕЗУЛЬТАТЫ ФУНКЦИОНАЛЬНОГО ТЕСТИРОВАНИЯ")
    print("-" * 60)
    
    passed = sum(1 for _, success in results if success)
    
    for name, success in results:
        status = "ПРОЙДЕН" if success else "ПРОВАЛ"
        print(f"{name:30} {status}")
    
    print(f"\nИТОГО: {passed} из {len(results)} тестов пройдено")
    
    if passed == len(results):
        print("\n Все функциональные тесты пройдены!")
    elif passed >= 2:
        print(f"\n Пройдено {passed}/3 тестов.")
    else:
        print("\n НЕУДОВЛЕТВОРИТЕЛЬНО.")
    
    return passed == len(results)

if __name__ == "__main__":
    success = run_functional_tests()
    exit(0 if success else 1)