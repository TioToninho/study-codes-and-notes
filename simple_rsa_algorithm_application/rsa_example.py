import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# função para encontrar o MDC de dois números
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# função para encontrar o inverso multiplicativo de a mod b
def find_inverse(a, b):
    if gcd(a, b) != 1:
        return None
    t, new_t = 0, 1
    r, new_r = b, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        t += b
    return t


# função para gerar as chaves públicas e privadas
def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q must be prime numbers.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # escolher um número 'e' tal que 1 < e < phi e MDC(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # calcular o inverso multiplicativo de 'e' mod phi
    d = find_inverse(e, phi)

    return ((e, n), (d, n))


# função para criptografar uma mensagem
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


# função para descriptografar uma mensagem
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)


# exemplo de uso
p = 17
q = 19
public_key, private_key = generate_keys(p, q)
print("Chave pública:", public_key)
print("Chave privada:", private_key)
mensagem = "Meu nome é Antonio!"
mensagem_criptografada = encrypt(public_key, mensagem)
print("Mensagem criptografada:", mensagem_criptografada)
mensagem_descriptografada = decrypt(private_key, mensagem_criptografada)
print("Mensagem descriptografada:", mensagem_descriptografada)
