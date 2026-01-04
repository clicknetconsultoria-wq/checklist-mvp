from datetime import datetime

def gerar_laudo(checklist) -> str:
    veiculo = checklist.veiculo
    itens = checklist.itens

    linhas_itens = []
    for item in itens:
        linhas_itens.append(f"- {item['descricao']}: {item['valor']}")

    texto = f"""
📋 *LAUDO DE CHECKLIST VEICULAR*

🚗 Veículo:
Placa: {veiculo['placa']}
Modelo: {veiculo.get('modelo', '')}

🛠️ Itens Verificados:
{chr(10).join(linhas_itens)}

📝 Observações:
{checklist.observacoes or "Não informado"}

👤 Responsável:
{checklist.responsavel}

📅 Data:
{checklist.criado_em.strftime("%d/%m/%Y %H:%M")}

Declaro que as informações acima refletem a condição do veículo no momento da vistoria.
"""

    return texto.strip()
