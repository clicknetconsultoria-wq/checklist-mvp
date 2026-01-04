from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from io import BytesIO
from datetime import datetime


def gerar_pdf_laudo(checklist):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4

    y = altura - 2 * cm

    # Cabeçalho
    c.setFont("Helvetica-Bold", 16)
    c.drawString(2 * cm, y, "LAUDO DE CHECKLIST VEICULAR")

    y -= 1.5 * cm
    c.setFont("Helvetica", 11)

    # Veículo
    c.drawString(2 * cm, y, f"Placa: {checklist.veiculo['placa']}")
    y -= 0.6 * cm
    c.drawString(2 * cm, y, f"Modelo: {checklist.veiculo.get('modelo', '')}")

    y -= 1 * cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "Itens Verificados:")

    y -= 0.6 * cm
    c.setFont("Helvetica", 11)
    for item in checklist.itens:
        c.drawString(2.5 * cm, y, f"- {item['descricao']}: {item['valor']}")
        y -= 0.5 * cm

    y -= 0.8 * cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "Observações:")

    y -= 0.6 * cm
    c.setFont("Helvetica", 11)
    c.drawString(2.5 * cm, y, checklist.observacoes or "Não informado")

    y -= 1 * cm
    c.drawString(2 * cm, y, f"Responsável: {checklist.responsavel}")
    y -= 0.6 * cm
    c.drawString(
        2 * cm,
        y,
        f"Data: {checklist.criado_em.strftime('%d/%m/%Y %H:%M')}"
    )

    # Rodapé
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(
        2 * cm,
        1.5 * cm,
        "Documento gerado automaticamente pelo sistema de checklist veicular."
    )

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
