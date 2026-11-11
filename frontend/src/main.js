import './style.css';

const status = document.querySelector('#api-status');
const retry = document.querySelector('#retry');

async function checkHealth() {
  retry.disabled = true;
  status.textContent = 'Verificando conexão com a API…';
  try {
    const response = await fetch('/api/health', { signal: AbortSignal.timeout(5000) });
    if (!response.ok) throw new Error('API indisponível');
    const data = await response.json();
    if (data.status !== 'ok') throw new Error('Resposta inesperada');
    status.textContent = 'API conectada. Ambiente pronto para começar.';
  } catch {
    status.textContent = 'API indisponível. Confirme se o servidor Python está rodando na porta 8000.';
  } finally {
    retry.disabled = false;
  }
}

retry.addEventListener('click', checkHealth);
checkHealth();
