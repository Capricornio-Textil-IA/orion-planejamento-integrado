# Template de apps internos — Capricórnio Têxtil

Base do treinamento para transformar problemas internos em protótipos de produtos, com código, instruções para agentes e skills versionadas na organização **Capricornio-Textil-IA**.

**Neon e Railway: planos, contratação, responsáveis, permissões e acessos permanecem em aberto.** Não é necessário criar conta ou informar credenciais para executar esta base localmente. A recomendação técnica desses serviços não representa contratação ou autorização de uso com dados internos.

## Comece pelo seu próprio repositório

1. Na página deste template, clique em **Use this template → Create a new repository**.
2. Escolha a organização `Capricornio-Textil-IA` e a visibilidade **Private**. Use um nome que identifique o produto.
3. Clone o novo repositório e abra a pasta na sua ferramenta de desenvolvimento. Clonar diretamente este template serve para estudar a base; criar pelo botão mantém seu produto em um repositório independente.
4. Leia [AGENTS.md](AGENTS.md), preencha [o briefing do produto](docs/produto.md) e peça ao agente a primeira entrega pequena, com critérios de aceite.
5. Use a conta corporativa orientada pela Capricórnio. A concessão de acesso à organização é responsabilidade dos administradores; este template não concede permissões.

## Stack e decisões

| Camada | Diretriz a seguir | Situação |
| --- | --- | --- |
| Código | GitHub na organização Capricornio-Textil-IA; acesso institucional | Repositórios privados por padrão deste template |
| Aplicações e integrações com IA | Python | Base local pronta |
| Dados | SQL; PostgreSQL no Neon para protótipos | Plano, contratação e acessos pendentes |
| Web | JavaScript e Tailwind CSS | Base local pronta |
| Hospedagem | Railway como recomendação para protótipos | Plano, contratação, acessos e configuração pendentes |
| Produção | Evolução para a plataforma corporativa de dados | Critérios e arquitetura a validar com a área responsável |
| Industrial | ClickHouse existente | Somente com autorização e suporte dos administradores |
| 3D | Three.js **ou** Babylon.js conforme o produto | Adicionar apenas quando necessário |
| Conhecimento | Markdown organizado com Obsidian | [Vault inicial](knowledge/README.md) |
| IA assistiva | Claude e Claude Code prioritários; Copilot complementar | Conforme ferramentas e acessos aprovados |
| Integrações de IA | Integrações diretas e ferramentas aprovadas | Não recomendar nem incorporar 9Router |

As avaliações complementares do documento substituem a escolha inicial de Supabase **na prototipação**. Supabase permanece alternativa condicionada à justificativa e validação. Os valores comerciais no documento são históricos; confirme condições com os responsáveis antes de contratar. Veja a [matriz de rastreabilidade e pendências](docs/stack-e-governanca.md) e a [transcrição da fonte](docs/diretrizes-fonte.md).

**Convenções de implementação deste template:** FastAPI para a API Python, Vite para desenvolvimento/build de JavaScript, Tailwind 4, `uv` e `npm` com arquivos de lock, Python 3.12 e Node 22.13+. O documento não escolhe esses frameworks ou versões; eles tornam a base reproduzível. Para mudar uma convenção, registre o motivo e o impacto em `docs/decisoes.md`. Para contrariar uma diretriz corporativa, obtenha validação da área responsável.

## Executar localmente

Instale [uv](https://docs.astral.sh/uv/getting-started/installation/), Python 3.12 e Node.js 22.13+ com npm. O `uv` pode instalar a versão de Python indicada em `.python-version`.

No primeiro terminal, na raiz:

```bash
uv sync --frozen
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

No segundo terminal:

```bash
cd frontend
npm ci
npm run dev
```

Abra o endereço local exibido pelo Vite (normalmente `http://127.0.0.1:5173`). A tela consulta `GET /api/health`. Esse endpoint indica que o processo está vivo; não verifica banco, permissões ou disponibilidade de provedores de IA.

Não há login, persistência, integração de IA ou acesso a dados reais implementados. O ponto de partida contém apenas uma página e um endpoint de saúde. Antes de acrescentar informações internas, implemente autenticação e autorização no servidor conforme a solução aprovada pela empresa.

Para uma configuração futura, copie `.env.example` para `.env`, preencha **somente no seu ambiente seguro** e use `uv run uvicorn app.main:app --reload --env-file .env`. A base ignora o banco e a chave de IA enquanto essas integrações não forem implementadas. Nunca use variáveis `VITE_*` para segredos: elas podem entrar no JavaScript do navegador.

## Agentes e skills

[AGENTS.md](AGENTS.md) concentra as instruções técnicas e os princípios corporativos adaptados. [CLAUDE.md](CLAUDE.md) importa esse arquivo para Claude Code; o Copilot recebe uma orientação em [`.github/copilot-instructions.md`](.github/copilot-instructions.md).

As skills canônicas ficam em [`skills/`](skills/README.md). Para descoberta no Claude Code, o repositório mantém cópias geradas em `.claude/skills/`, verificadas no CI. Edite a fonte em `skills/` e execute `python3 scripts/sync_skills.py`. Isso evita depender de links simbólicos em máquinas Windows. Outras ferramentas devem ler o AGENTS.md e as skills indicadas nele; a descoberta automática depende da ferramenta.

Exemplo de pedido inicial:

> Leia AGENTS.md e a skill capricornio-produto. Quero um app para [problema], usado por [público], com [resultado esperado]. Use dados sintéticos e entregue a menor versão que permita validar [critério]. Respeite as pendências de Neon e Railway e registre as premissas.

## Verificar e contribuir

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
python3 scripts/sync_skills.py --check
cd frontend
npm ci
npm run lint
npm run build
```

Faça mudanças em uma branch, abra PR e descreva problema, resultado, validação e riscos. O [CI](.github/workflows/ci.yml) verifica backend, frontend, skills e construção do container. Testes de negócio devem acompanhar comportamentos relevantes do seu produto; não é necessário testar texto estático da documentação.

Para servir a interface compilada pela própria API, rode `npm run build` em `frontend/`, volte à raiz e inicie a API. O build é gerado em `app/static/` e não é versionado. O [Dockerfile](Dockerfile) faz esse build e inicia o Python respeitando `PORT`.

```bash
docker build -t capricornio-app .
docker run --rm -p 8000:8000 capricornio-app
```

## Deploy e evolução

Leia [a preparação para deploy](docs/deploy.md). `Dockerfile` e `railway.toml` são preparação técnica; não provisionam serviços, contratam planos nem habilitam acesso. Não publique dados internos antes de validar autenticação, autorização, permissões, observabilidade, custos e responsáveis. O treinamento pode avançar integralmente em ambiente local com dados sintéticos.

## Mapa do repositório

```text
AGENTS.md                  Regras corporativas e técnicas para agentes
CLAUDE.md                  Entrada do Claude Code
skills/                    Skills canônicas reutilizáveis
.claude/skills/             Cópias geradas para Claude Code
app/                       Backend Python
frontend/                  JavaScript e Tailwind
tests/                     Testes do backend
docs/                      Fonte, stack, briefing, decisões e deploy
knowledge/                 Base Markdown compatível com Obsidian
scripts/sync_skills.py      Sincronização e verificação de skills
.github/                   CI e orientações de contribuição
```

Uso interno. Não torne público este repositório nem suas cópias com informações internas sem autorização da Capricórnio.
