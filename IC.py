import math
from collections import Counter

# =======================================================
# MÓDULO 1: GEMATRIA E ESTATÍSTICA (IC)
# =======================================================
class GematriaEngine:
    GEMATRIA = {
        'ᚠ': 0, 'ᚢ': 1, 'ᚦ': 2, 'ᚩ': 3, 'ᚱ': 4, 'ᚳ': 5, 'ᚷ': 6, 'ᚹ': 7,
        'ᚻ': 8, 'ᚾ': 9, 'ᛁ': 10, 'ᚼ': 11, 'ᛇ': 12, 'ᛈ': 13, 'ᛉ': 14, 'ᛋ': 15,
        'ᛏ': 16, 'ᛒ': 17, 'ᛖ': 18, 'ᛗ': 19, 'ᛚ': 20, 'ᛝ': 21, 'ᛟ': 22, 'ᛞ': 23,
        'ᚪ': 24, 'ᚫ': 25, 'ᚣ': 26, 'ᛡ': 27, 'ᛠ': 28
    }
    
    INVERSE_GEMATRIA = {v: k for k, v in GEMATRIA.items()}

    @staticmethod
    def text_to_values(text):
        return [GematriaEngine.GEMATRIA[c] for c in text if c in GematriaEngine.GEMATRIA]

    @staticmethod
    def calculate_ic(values):
        N = len(values)
        if N <= 1: return 0.0
        freq = Counter(values)
        return sum(f * (f - 1) for f in freq.values()) / (N * (N - 1))

    @staticmethod
    def generate_pisano_sequence(mod=29, length=300):
        seq = [0, 1]
        for _ in range(length - 2):
            seq.append((seq[-1] + seq[-2]) % mod)
        return seq

# =======================================================
# MÓDULO 2: MOTOR DE TRANSFORMAÇÃO E TESTE DE IC
# =======================================================
class CipherBreaker:
    @staticmethod
    def apply_shift(values, shifts):
        """Aplica o deslocamento (subtração) e retorna os novos valores."""
        return [(v - s) % 29 for v, s in zip(values, shifts)]

    @staticmethod
    def run_tests(text):
        values = GematriaEngine.text_to_values(text)
        base_ic = GematriaEngine.calculate_ic(values)
        pisano = GematriaEngine.generate_pisano_sequence(29, len(values))
        
        print("\n" + "="*60)
        print(" MOTOR DE TRANSFORMAÇÃO LIBUS PRIME - TESTE DE IC ")
        print("="*60)
        print(f"IC Original (Cifrado): {base_ic:.4f}")
        if base_ic < 0.055:
            print("[*] IC baixo confirmado. O texto está sob cifra polialfabética.")
        print("-" * 60)

        # TESTE 1: Deslocamento Linear com Sequência de Pisano
        shifted_vals = CipherBreaker.apply_shift(values, pisano)
        ic1 = GematriaEngine.calculate_ic(shifted_vals)
        print(f"TESTE 1: Deslocamento Linear (Fibonacci mod 29)")
        print(f"IC Obtido: {ic1:.4f} {'<-- PICO ESTATÍSTICO!' if ic1 > 0.060 else ''}")
        
        # TESTE 2: Matriz 14x14 (Coordenadas)
        cols = 14
        rows = math.ceil(len(values) / cols)
        r_shifts = []
        c_shifts = []
        rc_shifts = []
        
        for r in range(rows):
            for c in range(cols):
                if r * cols + c < len(values):
                    r_shifts.append(r % 29)
                    c_shifts.append(c % 29)
                    rc_shifts.append((r + c) % 29)
                    
        ic2 = GematriaEngine.calculate_ic(CipherBreaker.apply_shift(values, r_shifts))
        print(f"\nTESTE 2: Deslocamento por Linha da Matriz 14x14")
        print(f"IC Obtido: {ic2:.4f} {'<-- PICO ESTATÍSTICO!' if ic2 > 0.060 else ''}")
        
        ic3 = GematriaEngine.calculate_ic(CipherBreaker.apply_shift(values, c_shifts))
        print(f"\nTESTE 3: Deslocamento por Coluna da Matriz 14x14")
        print(f"IC Obtido: {ic3:.4f} {'<-- PICO ESTATÍSTICO!' if ic3 > 0.060 else ''}")
        
        ic4 = GematriaEngine.calculate_ic(CipherBreaker.apply_shift(values, rc_shifts))
        print(f"\nTESTE 4: Deslocamento por (Linha + Coluna) Matriz 14x14")
        print(f"IC Obtido: {ic4:.4f} {'<-- PICO ESTATÍSTICO!' if ic4 > 0.060 else ''}")

        # TESTE 5: Função Não-Linear (MDC entre Posição i e Valor)
        nl_shifts = []
        for i, v in enumerate(values):
            g = math.gcd(i+1, v+1) # +1 para evitar MDC com 0
            nl_shifts.append((g * 2) % 29) # Multiplicador experimental
        ic5 = GematriaEngine.calculate_ic(CipherBreaker.apply_shift(values, nl_shifts))
        print(f"\nTESTE 5: Deslocamento Não-Linear (MDC Posição x Valor)")
        print(f"IC Obtido: {ic5:.4f} {'<-- PICO ESTATÍSTICO!' if ic5 > 0.060 else ''}")
        
        print("="*60)

# =======================================================
# EXECUÇÃO
# =======================================================
if __name__ == "__main__":
    REAL_TEXT = """ᚠᛠ•ᛗ•ᚫᛉᚻᛖᚾ•ᚳᚳᚣᚾᚾ•ᛋᛏᛖᛗ•ᛏᛉ
ᚣ•ᚾᛁᛏᛈᛖ•ᛗᚳᛚᛗ•:•ᚦᛚ•ᛏᚱᛉᛏᚣ
ᚠᛒᚾᛗᛒᚾ•ᛈᚠᚱ•ᛉᚻᚱ•ᛁᚳ•ᚱᚣᚻᛒ•ᛈᛟᛒ
ᚾᚾᛏ•ᚱᛁᚾᛞᚩ•ᛁ•ᛗᚱ•ᚱᚣᚣᛉ•:•"•ᛏᛖᚱ•
ᚻᛖᚾᛏᛏᛉᛗᚱ"•ᛏᚳᛗᛈᛉ•ᛁᛏᛞ•:•ᛋᚳᚻ
ᛏᛉ•ᚾᛁᛋᛖ•ᛗᛏᚠᛟᛚᛞ•ᛒ•ᚱᚳ•ᛒᚻᛟ•ᛁᛞᛗᛗ
ᛚ•ᛟᛞᛗ•ᛉᚠᚱ•ᛈᚠᚱᛞ•ᚱ•ᛗᚠ•ᛁᛚ
ᛁ•ᚠᛁᛋ•ᛉᚱ•ᛋᚠᚠᚠ•ᚠᚱᚠ•ᛗᚱ•ᛗᛖ•ᛁ•ᛏ
ᛁᛏ•"•ᚠᚱᛏᛉ•ᚳᛋᚠᛗᛏᛒ•ᛟᛉ•ᛋᚻᚠ•ᛏ
ᚠᚠᚠ•ᛉᛚᚻᛉᛏ•ᚠᛚᛞ•ᚳᛈᛏ•ᛉᛚ•ᛋᛉᛈ•
ᚠᚠᛏ•ᛚᛏᛉ•ᛉᚠᛁᛗ•ᛒᛏᛏᛉ"•:•ᛉᛉ"""

    CipherBreaker.run_tests(REAL_TEXT)