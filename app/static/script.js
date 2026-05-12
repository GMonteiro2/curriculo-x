let tabAtiva = 'texto';

function trocarTab(tab) {
  tabAtiva = tab;
  document.getElementById('tab-texto').style.display = tab === 'texto' ? 'block' : 'none';
  document.getElementById('tab-arquivo').style.display = tab === 'arquivo' ? 'block' : 'none';
  document.querySelectorAll('.tab').forEach((el, i) => {
    el.classList.toggle('ativo', (tab === 'texto' && i === 0) || (tab === 'arquivo' && i === 1));
  });
}

function arquivoSelecionado(input) {
  const nome = input.files[0]?.name || 'nenhum arquivo selecionado';
  document.getElementById('upload-label').textContent = '📄 ' + nome;
}

async function analisar() {
  const btn = document.getElementById('analisar-btn');
  const loading = document.getElementById('loading');
  const resultado = document.getElementById('resultado');
  const erro = document.getElementById('erro');

  resultado.style.display = 'none';
  erro.style.display = 'none';
  loading.style.display = 'flex';
  btn.disabled = true;
  btn.textContent = 'Analisando...';

  try {
    let resposta;

    if (tabAtiva === 'texto') {
      const curriculo = document.getElementById('curriculo').value.trim();
      if (!curriculo) throw new Error('Cole o currículo antes de analisar!');

      resposta = await fetch('/api/analisar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ curriculo })
      });

    } else {
      const arquivo = document.getElementById('arquivo-input').files[0];
      if (!arquivo) throw new Error('Selecione um arquivo antes de analisar!');

      const formData = new FormData();
      formData.append('arquivo', arquivo);

      resposta = await fetch('/api/analisar-arquivo', {
        method: 'POST',
        body: formData
      });
    }

    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.detail || 'Erro desconhecido');

    document.getElementById('nota').textContent = dados.nota_geral;
    preencherLista('pontos-fortes', dados.pontos_fortes);
    preencherLista('pontos-fracos', dados.pontos_fracos);
    preencherLista('sugestoes', dados.sugestoes);

    resultado.style.display = 'block';

  } catch (err) {
    document.getElementById('erro-msg').textContent = 'Erro: ' + err.message;
    erro.style.display = 'block';
  } finally {
    loading.style.display = 'none';
    btn.disabled = false;
    btn.textContent = 'Analisar currículo';
  }
}

function preencherLista(id, itens) {
  const ul = document.getElementById(id);
  ul.innerHTML = '';
  itens.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    ul.appendChild(li);
  });
}