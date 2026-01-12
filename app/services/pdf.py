from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from io import BytesIO
from datetime import datetime

CHECKLIST_MAP = {
    "COMBUSTÍVEL": ["VAZIO", "1/4", "1/2", "3/4", "CHEIO"],
    "ÓLEO MOTOR": ["NÍVEL", "BAIXO"],
    "ÁGUA RADIADOR": ["NÍVEL", "BAIXO"],
    "FLUIDO FREIO": ["NÍVEL", "BAIXO"],
    "FLUIDO DIREÇÃO": ["NÍVEL", "BAIXO"],
    "SIRENE OK": ["SIM", "NÃO"],
    "GABINE LIMPA": ["SIM", "NÃO"],
    "PINTURA LIMPA": ["SIM", "NÃO"],
    "BAÚ LIMPO": ["SIM", "NÃO"],
    "DIREÇÃO": ["NORMAL", "PUXANDO"],
    "PUXANDO LADO": ["ESQUERDO", "DIREITO"],
    "LÂMPADA QUEIM.": ["SIM", "NÃO"],
    "PORTA C. DEFEITO": ["SIM", "NÃO"],
    "PARA BRISAS": ["NORMAL", "AVARIA"],
    "MACA": ["NORMAL", "DEFEITO"],
    "COLCHÃO MACA": ["NORMAL", "DEFEITO"],
    "BANCO BAÚ": ["NORMAL", "DEFEITO"],
    "SUPORTE O2": ["NORMAL", "DEFEITO"],
    "CHAVE DE RODA": ["PRESENTE", "FALTA"],
    "MACACO": ["PRESENTE", "FALTA"],
    "ESTEPE": ["PRESENTE", "FALTA"],
    "CHAVE TIRA ESTEPE": ["PRESENTE", "FALTA"],
    "VIDROS PORTA": ["NORMAL", "AVARIA"],
    "RETROVISORES": ["NORMAL", "AVARIA"],
    "PALHETA LIMPADOR": ["NORMAL", "DEFEITO"],
    "CALOTAS": ["PRESENTE", "AUSENTE"],
    "GIROFLEX FRONTAL": ["NORMAL", "DEFEITO"],
    "CINTO SEG GABINE": ["NORMAIS", "DEFEITO"],
    "CINTO SEG B. BAÚ": ["NORMAL", "DEFEITO"],
    "FLUXÔMETRO O2": ["PRESENTE", "AUSENTE"],
    "MANÔMETRO O2": ["PRESENTE", "AUSENTE"],
    "MAÇANETA PORTA D": ["NORMAL", "AVARIA"],
    "MAÇANETA PORTA E": ["NORMAL", "AVARIA"],
    "MAÇANETA BAÚ": ["NORMAL", "AVARIA"],
    "RÁDIO COMUNICAÇÃO": ["NORMAL", "DEFEITO"]
}

def marcar_opcao(c, x, y, valor, esperado):
    if valor and valor.upper() == esperado:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x, y, "X")
        c.setFont("Helvetica", 8)


def gerar_pdf_institucional(checklist):

    itens_recebidos = {
    item["descricao"].upper(): item["valor"].upper()
    for item in checklist.itens
    }

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 2 * cm

    # =====================================================
    # CABEÇALHO
    # =====================================================
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, y, "CHECK LIST VEICULAR")
    y -= 0.7 * cm
    c.setFont("Helvetica", 10)
    c.drawCentredString(
        width / 2,
        y,
        "BOLETIM DIÁRIO DE TRÁFEGO / ESTADO E RECEBIMENTO DA VIATURA"
    )

    y -= 1 * cm

    # =====================================================
    # BLOCO SUPERIOR (CAIXAS)
    # =====================================================
    # Linha 1
    c.drawString(2 * cm, y, f"DATA: {checklist.data or ''}")
    c.drawString(7 * cm, y, f"VEÍCULO: {checklist.veiculo.get('nome', '')}")
    c.drawString(13 * cm, y, f"PLACA: {checklist.veiculo.get('placa', '')}")

    y -= 0.7 * cm

    # Linha 2
    c.drawString(2 * cm, y, f"LOTAÇÃO: {checklist.veiculo.get('lotacao', '')}")
    c.drawString(7 * cm, y, f"KM INICIAL: {checklist.km_inicial or ''}")
    c.drawString(13 * cm, y, f"KM FINAL: {checklist.km_final or ''}")

    y -= 0.7 * cm

    # Cilindro O2
    c.drawString(2 * cm, y, "CILINDRO O2:")
    c.rect(5.2 * cm, y - 0.2 * cm, 0.4 * cm, 0.4 * cm)
    c.drawString(5.7 * cm, y, "SIM")
    marcar_opcao(c, 5.3 * cm, y - 0.1 * cm, checklist.cilindro_o2, "SIM")

    c.rect(6.8 * cm, y - 0.2 * cm, 0.4 * cm, 0.4 * cm)
    c.drawString(7.3 * cm, y, "NÃO")
    marcar_opcao(c, 6.9 * cm, y - 0.1 * cm, checklist.cilindro_o2, "NÃO")

    # Plantão
    c.drawString(9.5 * cm, y, "PLANTÃO:")
    c.rect(11.5 * cm, y - 0.2 * cm, 0.4 * cm, 0.4 * cm)
    c.drawString(12.1 * cm, y, "12h")
    marcar_opcao(c, 11.6 * cm, y - 0.1 * cm, checklist.plantao, "12H")

    c.rect(13.2 * cm, y - 0.2 * cm, 0.4 * cm, 0.4 * cm)
    c.drawString(13.8 * cm, y, "24h")
    marcar_opcao(c, 13.3 * cm, y - 0.1 * cm, checklist.plantao, "24H")

    y -= 1.2 * cm

    # =====================================================
    # CONDUTORES
    # =====================================================
    # Condutores
    c.line(3 * cm, y, 9 * cm, y)
    c.drawCentredString(6 * cm, y - 0.4 * cm, "CONDUTOR DE PLANTÃO")
    c.drawCentredString(6 * cm, y + 0.2 * cm, checklist.condutor_plantao or "")

    c.line(11 * cm, y, 17 * cm, y)
    c.drawCentredString(14 * cm, y - 0.4 * cm, "CONDUTOR DE ANTERIOR")
    c.drawCentredString(14 * cm, y + 0.2 * cm, checklist.condutor_anterior or "")

    y -= 1.2 * cm


    # =====================================================
    # TABELA CENTRAL (CHECKLIST)
    # =====================================================
    c.setFont("Helvetica", 8)

    tabela_itens = [
        "COMBUSTÍVEL",
        "ÓLEO MOTOR",
        "ÁGUA RADIADOR",
        "FLUIDO FREIO",
        "FLUIDO DIREÇÃO",
        "SIRENE OK",
        "GABINE LIMPA",
        "PINTURA LIMPA",
        "BAÚ LIMPO",
        "DIREÇÃO",
        "PUXANDO LADO",
        "LÂMPADA QUEIM.",
        "PORTA C. DEFEITO",
        "PARA BRISAS",
        "MACA",
        "COLCHÃO MACA",
        "BANCO BAÚ",
        "SUPORTE O2",
        "CHAVE DE RODA",
        "MACACO",
        "ESTEPE",
        "CHAVE TIRA ESTEPE",
        "VIDROS PORTA",
        "RETROVISORES",
        "PALHETA LIMPADOR",
        "CALOTAS",
        "GIROFLEX FRONTAL",
        "CINTO SEG GABINE",
        "CINTO SEG B. BAÚ",
        "FLUXÔMETRO O2",
        "MANÔMETRO O2",
        "MAÇANETA PORTA D",
        "MAÇANETA PORTA E",
        "MAÇANETA BAÚ",
        "RÁDIO COMUNICAÇÃO"
    ]

    x_item = 2 * cm
x_start = 9 * cm
col_width = 1.8 * cm
row_height = 0.45 * cm

for item, opcoes in CHECKLIST_MAP.items():
    # Caixa do item
    c.rect(x_item, y - row_height, 7 * cm, row_height)
    c.drawString(x_item + 2, y - row_height + 2, item)

    # Desenha colunas
    for i, opcao in enumerate(opcoes):
        x = x_start + (i * col_width)
        c.rect(x, y - row_height, col_width, row_height)
        c.drawCentredString(x + col_width / 2, y - row_height + 2, opcao)

        # Marca X se for a opção escolhida
        if itens_recebidos.get(item) == opcao:
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(x + col_width / 2, y - row_height + 1, "X")
            c.setFont("Helvetica", 8)

    y -= row_height

    if y < 4 * cm:
        c.showPage()
        y = height - 2 * cm
        c.setFont("Helvetica", 8)


    y -= 0.8 * cm

    # =====================================================
    # CAMPOS FINAIS
    # =====================================================
    c.setFont("Helvetica-Bold", 9)
    c.drawString(2 * cm, y, "OUTROS DEFEITOS APRESENTADOS:")
    y -= 0.3 * cm
    c.rect(2 * cm, y - 2 * cm, width - 4 * cm, 2 * cm)

    y -= 2.5 * cm

    c.drawString(2 * cm, y, "DEFEITOS OU INTERCORRÊNCIAS DURANTE O PLANTÃO:")
    y -= 0.3 * cm
    c.rect(2 * cm, y - 2 * cm, width - 4 * cm, 2 * cm)

    # =====================================================
    c.showPage()
    c.save()
    buffer.seek(0)

    return buffer
