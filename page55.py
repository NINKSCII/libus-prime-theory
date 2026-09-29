import math
import re
from collections import Counter

# =======================================================
# MÓDULO 1: GEMATRIA PRIMUS E LIMPEZA
# =======================================================
class GematriaEngine:
    GEMATRIA = {
        'ᚠ': 0, 'ᚢ': 1, 'ᚦ': 2, 'ᚩ': 3, 'ᚱ': 4, 'ᚳ': 5, 'ᚷ': 6, 'ᚹ': 7,
        'ᚻ': 8, 'ᚾ': 9, 'ᛁ': 10, 'ᚼ': 11, 'ᛇ': 12, 'ᛈ': 13, 'ᛉ': 14, 'ᛋ': 15,
        'ᛏ': 16, 'ᛒ': 17, 'ᛖ': 18, 'ᛗ': 19, 'ᛚ': 20, 'ᛝ': 21, 'ᛟ': 22, 'ᛞ': 23,
        'ᚪ': 24, 'ᚫ': 25, 'ᚣ': 26, 'ᛡ': 27, 'ᛠ': 28, 'ᛳ': 2, 'ᛄ': 5
    }
    
    @staticmethod
    def text_to_values(text):
        return [GematriaEngine.GEMATRIA[c] for c in text if c in GematriaEngine.GEMATRIA]

# =======================================================
# MÓDULO 2: MOTOR LIBUS PRIME (TEORIA DAS DUAS CAMADAS)
# =======================================================
class LibusPrimeEngine:
    @staticmethod
    def analyze_page_55(text):
        values = GematriaEngine.text_to_values(text)
        if len(values) < 10: return
        
        print("\n" + "="*60)
        print(" ANÁLISE LIBUS PRIME - PÁGINA 55 REAL (ISOLADA) ")
        print("="*60)
        print(f"Total de runas extraídas da página: {len(values)}")
        
        # 1. TEORIA 1: ESTRUTURA GEOMÉTRICA (MDC)
        # Como a página é curta, usamos uma matriz de 14 colunas (Período de Pisano)
        cols = 14
        rows = math.ceil(len(values) / cols)
        matrix = []
        for r in range(rows):
            row = values[r*cols : (r+1)*cols]
            while len(row) < cols: row.append(None)
            matrix.append(row)
            
        gcd_h = Counter()
        for r in range(rows):
            for c in range(cols-1):
                v1, v2 = matrix[r][c], matrix[r][c+1]
                if v1 is not None and v2 is not None:
                    gcd_h[math.gcd(v1, v2)] += 1
                    
        coprime_ratio = (gcd_h.get(1, 0) / sum(gcd_h.values())) * 100 if sum(gcd_h.values()) > 0 else 0
        print(f"\n[CAMADA 1] Matriz {rows}x{cols} (Pisano):")
        print(f"Densidade de Coprimalidade (MDC=1): {coprime_ratio:.2f}%")
        print("Invariantes Horizontais mais comuns:")
        for g, count in gcd_h.most_common(3):
            print(f"  MDC = {g}: {count} ocorrências")

        # 2. TEORIA 2: FUNÇÃO NÃO-LINEAR E FIBONACCI
        # Teste de transição recorrente: x_{n+1} = (x_n + x_{n-1}) mod 29
        fib_match = 0
        for i in range(1, len(values)-1):
            if (values[i] + values[i-1]) % 29 == values[i+1]:
                fib_match += 1
                
        percent_fib = (fib_match / (len(values)-2)) * 100
        print(f"\n[CAMADA 2] Função Posicional / Fibonacci:")
        print(f"Transições que seguem Soma Recorrente (Fibonacci mod 29): {percent_fib:.2f}%")
        
        # 3. TESTE DA FUNÇÃO ALGÉBRICA f(x,y) = (X*x + Y*y) mod 29
        print("\nProcurando coeficientes algébricos escondidos...")
        best_match = 0
        best_X = 0
        best_Y = 0
        # Amostra de 100 iterações para não travar
        for X in range(29):
            for Y in range(29):
                match_count = 0
                for i in range(1, len(values)-1):
                    calc = (X * values[i-1] + Y * values[i]) % 29
                    if calc == values[i+1]:
                        match_count += 1
                if match_count > best_match:
                    best_match = match_count
                    best_X = X
                    best_Y = Y
                    
        print(f"Melhor coeficiente: X={best_X}, Y={best_Y}")
        print(f"Casamentos na amostra: {best_match} de {len(values)-2}")
        if best_match > (len(values)-2) * 0.1:
            print("[***] ALERTA: Função algébrica não-linear detectada!")

# =======================================================
# EXECUÇÃO
# =======================================================
if __name__ == "__main__":
    # As runas REAIS da Página 55 extraídas do arquivo que você mandou
    PAGE_55_RUNES = """
    ᛝ᛫ᚫᛗᛁᚹ᛫ᛋᛒ᛫ᛉᛗ᛫ᛋᛇᚷᛞᚦᚫ᛫ᚠᛡᚪᛒᚳᚢ᛫ᚹᚱ᛫ᛒ
    ᛠᚠᛉᛁᛗᚢᚳᛈᚻᛝᛚᛇ᛫ᛗᛋᛞᛡᛈᚠ᛫ᛒᚻᛇᚳ᛫
    ᛇᛖ᛫ᛠᛖᛁᚷᛉᚷᛋ᛫ᛖᛋᛇᚦᚦᛖᛋ᛫ᚦᛟ᛫ᚳᛠᛁᛗ
    ᚳᛉ᛫ᛞᛄᚢ᛫ᛒᛖᛁ
    """
    
    LibusPrimeEngine.analyze_page_55(PAGE_55_RUNES)