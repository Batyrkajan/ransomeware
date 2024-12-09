import base64
import pytest

class Ransomware:
    def __init__(self, key):
        self.key = key

    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            encrypted_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
            with open(file_path, 'w') as file:
                file.write(encrypted_content)
        except Exception as e:
            print(f"Failed to encrypt {file_path}: {str(e)}")

@pytest.fixture
def ransomware():
    return Ransomware("test_key")

def test_encrypt_file_base64_encoding(tmp_path, ransomware):
    # Arrange
    test_file = tmp_path / "test.txt"
    original_content = "Hello World"
    test_file.write_text(original_content)

    # Act
    ransomware.encrypt_file(str(test_file))

    # Assert
    encrypted_content = test_file.read_text()
    decrypted_content = base64.b64decode(encrypted_content).decode('utf-8')
    assert decrypted_content == original_content
    assert encrypted_content != original_content

def test_encrypt_nonexistent_file(caplog, ransomware):
    # Arrange
    non_existent_file = "does_not_exist.txt"

    # Act
    ransomware.encrypt_file(non_existent_file)

    # Assert
    assert "Failed to encrypt" in caplog.text
    assert non_existent_file in caplog.text
