  document.querySelector('#form-voluntario').addEventListener('submit', async (e) => {
    e.preventDefault();

    const dados = {
      nome: e.target.nome.value,
      email: e.target.email.value,
      telefone: e.target.telefone.value,
      endereco: e.target.endereco.value,
      mensagem: e.target.mensagem.value
    };

    console.log('Dados coletados:', dados); 

    alert('Formulário enviado com sucesso! (tem q mudar isso dps)');
  });