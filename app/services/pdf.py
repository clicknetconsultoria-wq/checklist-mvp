from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from io import BytesIO


def gerar_pdf_layout_estatico():
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4

    x_margin = 2 * cm
    y = altura - 2 * cm

    # ===============================
    # CABEÇALHO
    # ===============================
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(largura / 2, y, "CHECK LIST VEICULAR")

    y -= 0.8 * cm
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(
        largura / 2,
        y,
        "BOLETIM DIÁRIO DE TRÁFEGO / ESTADO E RECEBIMENTO DA VIATURA"
    )

    y -= 1.2 * cm

    # ===============================
    # BLOCO 1 — IDENTIFICAÇÃO
    # ===============================
    c.setFont("Helvetica", 10)

    def campo(label, x, y, largura_campo):
        c.drawString(x, y, label)
        c.line(x + 40, y - 2, x + largura_campo, y - 2)

    campo("DATA:", x_margin, y, 120)
    campo("VEÍCULO:", x_margin + 180, y, 300)

    y -= 0.7 * cm
    campo("PLACA:", x_margin, y, 120)
    campo("LOTAÇÃO:", x_margin + 180, y, 300)

    y -= 1 * cm

    # ===============================
    # BLOCO 2 — OPERAÇÃO
    # ===============================
    campo("KM INICIAL:", x_margin, y, 120)
    campo("KM FINAL:", x_margin + 180, y, 300)

    y -= 0.7 * cm
    c.drawString(x_margin, y, "CILINDRO O2:")
    c.rect(x_margin + 90, y - 10, 10, 10)
    c.drawString(x_margin + 105, y, "SIM")
    c.rect(x_margin + 150, y - 10, 10, 10)
    c.drawString(x_margin + 165, y, "NÃO")

    y -= 0.7 * cm
    c.drawString(x_margin, y, "PLANTÃO:")
    c.rect(x_margin + 90, y - 10, 10, 10)
    c.drawString(x_margin + 105, y, "12h")
    c.rect(x_margin + 150, y - 10, 10, 10)
    c.drawString(x_margin + 165, y, "24h")

    y -= 1 * cm

    # ===============================
    # CONDUTORES
    # ===============================
    c.drawString(x_margin, y, "CONDUTOR DE PLANTÃO:")
    c.line(x_margin + 150, y - 2, largura - x_margin, y - 2)

    y -= 0.8 * cm
    c.drawString(x_margin, y, "CONDUTOR ANTERIOR:")
    c.line(x_margin + 150, y - 2, largura - x_margin, y - 2)

    y -= 1 * cm

    # ===============================
    # TABELA CHECKLIST
    # ===============================
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x_margin, y, "ITENS DE VERIFICAÇÃO")
    y -= 0.5 * cm
    c.setFont("Helvetica", 9)

    itens = [
        "COMBUSTÍVEL",
        "ÓLEO MOTOR",
        "ÁGUA RADIADOR",
        "FLUIDO FREIO",
        "SIRENE OK",
        "GABINE LIMPA",
        "PINTURA LIMPA",
        "DIREÇÃO",
        "LÂMPADAS",
        "PARA-BRISAS",
        "MACA",
        "COLCHÃO MACA",
        "ESTEPE",
        "VIDROS",
        "RETROVISORES",
        "GIROFLEX",
        "CINTOS DE SEGURANÇA",
        "RÁDIO COMUNICAÇÃO"
    ]

    for item in itens:
        c.drawString(x_margin, y, item)
        c.rect(x_margin + 180, y - 10, 10, 10)
        c.drawString(x_margin + 195, y, "OK")
        c.rect(x_margin + 240, y - 10, 10, 10)
        c.drawString(x_margin + 255, y, "NÃO OK")
        y -= 0.5 * cm

    y -= 0.5 * cm

    # ===============================
    # CAMPOS ABERTOS
    # ===============================
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x_margin, y, "OUTROS DEFEITOS APRESENTADOS:")
    y -= 0.3 * cm
    c.rect(x_margin, y - 60, largura - 2 * x_margin, 60)

    y -= 1.5 * cm
    c.drawString(x_margin, y, "DEFEITOS OU INTERCORRÊNCIAS DURANTE O PLANTÃO:")
    y -= 0.3 * cm
    c.rect(x_margin, y - 60, largura - 2 * x_margin, 60)

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
