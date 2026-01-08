document.addEventListener("DOMContentLoaded", () => {

  console.log("SCRIPT CARREGADO")

  document.getElementById("checklistForm").addEventListener("submit", async (e) => {
    console.log("SUBMIT DISPARADO")
    e.preventDefault()

    const itens = []
    document.querySelectorAll("select[data-item]").forEach(select => {
      itens.push({
        descricao: select.dataset.item,
        valor: select.value
      })
    })

    const payload = {
      phone: document.getElementById("phone").value,
      veiculo: {
        placa: document.getElementById("placa").value,
        modelo: document.getElementById("modelo").value
      },
      itens,
      responsavel: document.getElementById("responsavel").value,
      observacoes: document.getElementById("observacoes").value
    }

    try {
      const response = await fetch(
        "https://checklist-mvp-production.up.railway.app/checklist/send",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(payload)
        }
      )

      if (!response.ok) {
        throw new Error(await response.text())
      }

      alert("✅ Checklist enviado via WhatsApp com sucesso!")
      document.getElementById("checklistForm").reset()

    } catch (err) {
      alert("❌ Erro ao enviar checklist")
      console.error(err)
    }
  })

})
