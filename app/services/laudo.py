from app.models import ChecklistRequest
from datetime import datetime

def gerar_laudo(data: ChecklistRequest) -> str:
    linhas = [
        "🛠️ *LAUDO DE CHECKLIST VEICULAR*",
        f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        f"👤 Cliente: {data.cliente}",
        f"👨‍🔧 Técnico: {data.tecnico}",
        f"🚗 Veículo: {data.veiculo.modelo} - {data.veiculo.placa}",
        "",
        "*Itens verificados:*"
    ]

    for item, status in data.checklist.items():
        linhas.append(f"- {item}: {status}")

    return "\n".join(linhas)
