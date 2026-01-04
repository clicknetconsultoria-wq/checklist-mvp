document.getElementById("checklistForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const itens = [];
    document.querySelectorAll("select[data-item]").forEach(select => {
        itens.push({
            descricao: select.dataset.item,
            valor: select.value
        });
    });

    const payload = {
        veiculo: {
            placa: document.getElementById("placa").value,
            modelo: document.getElementById("modelo").value
        },
        itens: itens,
        observacoes: document.getElementById("observacoes").value,
        responsavel: document.getElementById("responsavel").value
    };

    const response = await fetch("/checklists", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    if (response.ok) {
        alert("Checklist enviado com sucesso!");
        document.getElementById("checklistForm").reset();
    } else {
        alert("Erro ao enviar checklist");
    }
});
