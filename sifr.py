###### Симетричный шифр
from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher = Fernet(key)

# Шифрование данных
data = b"Пример симметричного шифрования"
encrypted_data = cipher.encrypt(data)
print(f"Зашифрованный текст: {encrypted_data}")

# Расшифрование данных
decrypted_data = cipher.decrypt(encrypted_data)
print(f"Расшифрованный текст: {decrypted_data.decode()}")











###### Асиметричный шифр
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Генерация пары ключей
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Шифрование данных с помощью публичного ключа
data = b"Пример асимметричного шифрования"
encrypted_data = public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Зашифрованный текст: {encrypted_data}")

# Расшифрование данных с помощью приватного ключа
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Расшифрованный текст: {decrypted_data.decode()}")
