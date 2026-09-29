import math
from collections import Counter

# =======================================================
# MÓDULO 1: GEMATRIA PRIMUS E CAMADA POSICIONAL
# =======================================================
class GematriaEngine:
    GEMATRIA = {
        'ᚠ': 0, 'ᚢ': 1, 'ᚦ': 2, 'ᚩ': 3, 'ᚱ': 4, 'ᚳ': 5, 'ᚷ': 6, 'ᚹ': 7,
        'ᚻ': 8, 'ᚾ': 9, 'ᛁ': 10, 'ᚼ': 11, 'ᛇ': 12, 'ᛈ': 13, 'ᛉ': 14, 'ᛋ': 15,
        'ᛏ': 16, 'ᛒ': 17, 'ᛖ': 18, 'ᛗ': 19, 'ᛚ': 20, 'ᛝ': 21, 'ᛟ': 22, 'ᛞ': 23,
        'ᚪ': 24, 'ᚫ': 25, 'ᚣ': 26, 'ᛡ': 27, 'ᛠ': 28
    }
    
    @staticmethod
    def generate_pisano_sequence(mod=29, length=100):
        seq = [0, 1]
        for _ in range(length - 2):
            seq.append((seq[-1] + seq[-2]) % mod)
        return set(seq)

    @staticmethod
    def text_to_values(text):
        # Ignora qualquer pontuação e pega apenas as runas mapeadas
        return [GematriaEngine.GEMATRIA[c] for c in text if c in GematriaEngine.GEMATRIA]

    @staticmethod
    def analyze_positional_layer(text):
        values = GematriaEngine.text_to_values(text)
        if len(values) < 2: return
        
        differences = []
        for i in range(len(values) - 1):
            diff = (values[i+1] - values[i]) % 29
            differences.append(diff)
            
        pisano_seq = GematriaEngine.generate_pisano_sequence(29, 100)
        fibonacci_matches = [d for d in differences if d in pisano_seq]
        
        freq_diffs = Counter(differences)
        
        print("\n" + "="*50)
        print(" CAMADA 1 — ANÁLISE POSICIONAL E FIBONACCI ")
        print("="*50)
        print(f"Total de runas analisadas: {len(values)}")
        print(f"Total de diferenças calculadas: {len(differences)}")
        print(f"Matches com Sequência de Fibonacci (mod 29): {len(fibonacci_matches)} ({(len(fibonacci_matches)/len(differences))*100:.2f}%)")
        
        print("\nDiferenças mais frequentes (mod 29):")
        for diff, count in freq_diffs.most_common(10):
            tag = " [Fibonacci]" if diff in pisano_seq else ""
            print(f"  Diferença {diff:2d}: {count} vezes{tag}")

# =======================================================
# MÓDULO 2: ESTRUTURA GEOMÉTRICA E INVARIANTES (MDC)
# =======================================================
class StructuralMatrixAnalyzer:
    @staticmethod
    def build_matrix(values, cols=14):
        rows = math.ceil(len(values) / cols)
        matrix = []
        for r in range(rows):
            start = r * cols
            end = start + cols
            row = values[start:end]
            while len(row) < cols: row.append(None)
            matrix.append(row)
        return matrix

    @staticmethod
    def analyze_geometric_layer(text, cols=14):
        values = GematriaEngine.text_to_values(text)
        if len(values) < cols: return
        
        matrix = StructuralMatrixAnalyzer.build_matrix(values, cols)
        rows_count = len(matrix)
        
        gcd_horizontal = Counter()
        gcd_vertical = Counter()
        
        for r in range(rows_count):
            for c in range(cols):
                val = matrix[r][c]
                if val is None or val == 0: continue 
                
                if c + 1 < cols and matrix[r][c+1] is not None and matrix[r][c+1] != 0:
                    g = math.gcd(val, matrix[r][c+1])
                    gcd_horizontal[g] += 1
                    
                if r + 1 < rows_count and matrix[r+1][c] is not None and matrix[r+1][c] != 0:
                    g = math.gcd(val, matrix[r+1][c])
                    gcd_vertical[g] += 1

        print("\n" + "="*50)
        print(f" CAMADA 2 — ESTRUTURA GEOMÉTRICA (MDC) - MATRIZ {cols} COLUNAS ")
        print("="*50)
        print(f"Matriz construída: {rows_count} linhas x {cols} colunas")
        
        print("\nInvariantes Horizontais (MDC entre vizinhos direita):")
        for g, count in gcd_horizontal.most_common(5):
            print(f"  MDC={g}: {count} ocorrências")
            
        print("\nInvariantes Verticais (MDC entre vizinhos abaixo):")
        for g, count in gcd_vertical.most_common(5):
            print(f"  MDC={g}: {count} ocorrências")
            
        coprime_count = gcd_horizontal.get(1, 0) + gcd_vertical.get(1, 0)
        total_pairs = sum(gcd_horizontal.values()) + sum(gcd_vertical.values())
        
        if total_pairs > 0:
            coprime_ratio = (coprime_count / total_pairs) * 100
            print(f"\nDensidade de Coprimalidade (MDC=1): {coprime_ratio:.2f}%")
            print(f"Densidade de Invariantes (MDC>1): {100 - coprime_ratio:.2f}%")

# =======================================================
# EXECUÇÃO COM O TEXTO REAL FORNECIDO
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

    print("=== MOTOR DE ANÁLISE LIBUS PRIME v2 ===")
    print("Analisando trecho real extraído do Liber Primus...")
    
    # Executa a Camada 1
    GematriaEngine.analyze_positional_layer(REAL_TEXT)
    
    # Executa a Camada 2 testando a hipótese do Período de Pisano (14)
    print("\n" + "#"*50)
    print(" TESTANDO HIPÓTESE DE INVARIANTES EM DIFERENTES LARGURAS ")
    print("#"*50)
    
    for width in [13, 14, 15]:
        StructuralMatrixAnalyzer.analyze_geometric_layer(REAL_TEXT, cols=width)