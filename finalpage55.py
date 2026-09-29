import math


# MÓDULO 1: GEMATRIA

class GematriaEngine:
    GEMATRIA = {
        'ᚠ': 0, 'ᚢ': 1, 'ᚦ': 2, 'ᚩ': 3, 'ᚱ': 4, 'ᚳ': 5, 'ᚷ': 6, 'ᚹ': 7,
        'ᚻ': 8, 'ᚾ': 9, 'ᛁ': 10, 'ᚼ': 11, 'ᛇ': 12, 'ᛈ': 13, 'ᛉ': 14, 'ᛋ': 15,
        'ᛏ': 16, 'ᛒ': 17, 'ᛖ': 18, 'ᛗ': 19, 'ᛚ': 20, 'ᛝ': 21, 'ᛟ': 22, 'ᛞ': 23,
        'ᚪ': 24, 'ᚫ': 25, 'ᚣ': 26, 'ᛡ': 27, 'ᛠ': 28, 'ᛳ': 2, 'ᛄ': 5
    }
    LETTERS = ['F','U','TH','O','R','C','G','W','H','N','I','J','EO','P','X','S','T','B','E','M','L','NG','OE','D','A','AE','Y','IA','EA']

    @staticmethod
    def clean_text(text):
        return "".join([c for c in text if c in GematriaEngine.GEMATRIA])

    @staticmethod
    def text_to_values(text):
        return [GematriaEngine.GEMATRIA[c] for c in GematriaEngine.clean_text(text)]

    @staticmethod
    def values_to_text(values):
        return "".join([GematriaEngine.LETTERS[v] for v in values])


# MÓDULO 2: CALIBRADOR DA MÁQUINA DE ESTADOS

class StateMachineCalibrator:
    @staticmethod
    def generate_primes(n):
        primes = []
        num = 2
        while len(primes) < n:
            if all(num % p != 0 for p in primes): primes.append(num)
            num += 1
        return primes

    @staticmethod
    def score_text(text):
        patterns = ['THE', 'AND', 'ING', 'ION', 'TH', 'ER', 'AN', 'RE', 'ENT', 'NON', 'TIS', 'ET']
        score = 0
        for p in patterns:
            score += text.count(p) * 25
        return score

    @staticmethod
    def run(text):
        cipher_vals = GematriaEngine.text_to_values(text)
        if len(cipher_vals) < 2: return
        
        primes = StateMachineCalibrator.generate_primes(len(cipher_vals) + 50)
        
        print("\n" + "="*60)
        print(" CALIBRADOR DA MÁQUINA DE ESTADOS (PRIMOS + F-SKIP) ")
        print("="*60)
        
        best_score = -1
        best_text = ""
        best_start = -1
        best_mode = ""
        
        # Testar começando a sequência de primos do índice 0 até 10
        for start_offset in range(10):
            # MODO 1: F-Skip no Plaintext (Se Plain = F, não avança)
            p_idx = start_offset
            m1_vals = []
            for c_val in cipher_vals:
                p = primes[p_idx]
                p_val = (c_val - (p - 1)) % 29
                m1_vals.append(p_val)
                if p_val != 0: p_idx += 1 # Se não for F, avança
            
            m1_text = GematriaEngine.values_to_text(m1_vals)
            m1_score = StateMachineCalibrator.score_text(m1_text)
            
            if m1_score > best_score:
                best_score = m1_score
                best_text = m1_text
                best_start = start_offset
                best_mode = "F-skip no Plaintext"
                
            # MODO 2: F-Skip na Cifra (Se Runa = F/ᚠ, não avança)
            p_idx = start_offset
            m2_vals = []
            for c_val in cipher_vals:
                p = primes[p_idx]
                p_val = (c_val - (p - 1)) % 29
                m2_vals.append(p_val)
                if c_val != 0: p_idx += 1 # Se a runa cifrada não for F, avança
                
            m2_text = GematriaEngine.values_to_text(m2_vals)
            m2_score = StateMachineCalibrator.score_text(m2_text)
            
            if m2_score > best_score:
                best_score = m2_score
                best_text = m2_text
                best_start = start_offset
                best_mode = "F-skip na Cifra"
                
        print(f"Melhor Mecanismo: {best_mode}")
        print(f"Inicio da Sequência de Primos: Índice {best_start} (Primo {primes[best_start]})")
        print(f"Score de Linguagem: {best_score}")
        print(f"Texto Decifrado:\n{best_text}")
        print("="*60)


# EXECUÇÃO

if __name__ == "__main__":
    PAGE_55_TEXT = """
    ᛝ᛫ᚫᛗᛁᚹ᛫ᛋᛒ᛫ᛉᛗ᛫ᛋᛇᚷᛞᚦᚫ᛫ᚠᛡᚪᛒᚳᚢ᛫ᚹᚱ᛫ᛒ
    ᛠᚠᛉᛁᛗᚢᚳᛈᚻᛝᛚᛇ᛫ᛗᛋᛞᛡᛈᚠ᛫ᛒᚻᛇᚳ᛫
    ᛇᛖ᛫ᛠᛖᛁᚷᛉᚷᛋ᛫ᛖᛋᛇᚦᚦᛖᛋ᛫ᚦᛟ᛫ᚳᛠᛁᛗ
    ᚳᛉ᛫ᛞᛄᚢ᛫ᛒᛖᛁ
    """
    
    StateMachineCalibrator.run(PAGE_55_TEXT)