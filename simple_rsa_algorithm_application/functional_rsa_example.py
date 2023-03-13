from typing import List, Tuple


def gcd(a: int, b: int) -> int:
    """
    Retorna o maior divisor comum entre a e b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inv(a: int, m: int) -> int:
    """
    Retorna o inverso multiplicativo de a mod m
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("O inverso multiplicativo não existe")


def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Gera um par de chaves público/privado a partir de dois primos p e q
    """
    n = p * q
    phi = (p - 1) * (q - 1)

    # Escolha um inteiro e tal que e e phi(n) são primos entre si
    e = 65537
    while gcd(e, phi) != 1:
        e += 1

    # Calcule o inverso multiplicativo de e mod phi(n)
    d = mod_inv(e, phi)

    # Retorne o par de chaves
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


def encrypt(public_key: Tuple[int, int], message: str) -> int:
    """
    Criptografa a mensagem usando a chave pública
    """
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


def decrypt(private_key: Tuple[int, int], cipher: List[int]) -> str:
    """
    Descriptografa a mensagem usando a chave privada
    """
    d, n = private_key
    message = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(message)


# Exemplo de uso:
public_key, private_key = generate_keypair(61, 53)
cipher = encrypt(public_key, "Meu nome é Antonio!")
message = decrypt(private_key, cipher)
print(cipher)
print(message)
