# Stack, origem das decisões e pendências

Referência: `Capricornio_Diretrizes_IA_Versao_Final.docx`, fornecido pelo solicitante. A [transcrição](diretrizes-fonte.md) preserva o texto, inclusive as recomendações comerciais históricas. Esta matriz interpreta a aplicação ao template; não é uma nova política corporativa.

## Precedência e escopo

A avaliação complementar de banco afirma explicitamente que Neon substitui Supabase **apenas na prototipação**. A migração futura para a plataforma corporativa permanece. A avaliação complementar de deploy recomenda Railway e um fluxo com PR/testes/preview/deploy; isso não elimina a validação dos critérios de produção pela área responsável.

Em orientação adicional de **18/10/2026**, o solicitante informou que **os planos de Neon e Railway ainda não foram contratados** e pediu que a questão dos acessos fique em aberto. Portanto, recomendação técnica, contratação e acesso são estados diferentes. Não interpretar o documento como evidência de contratação, plano escolhido ou acesso concedido.

## Rastreabilidade

| Fonte | Aplicação no template |
| --- | --- |
| §1 Versionamento | Organização GitHub Capricornio-Textil-IA, instruções para identidade corporativa, branches e PRs |
| §2 Linguagens | Backend Python, dados SQL, frontend JavaScript e Tailwind |
| §3 + avaliação complementar de banco | Neon/PostgreSQL recomendado para protótipos; Supabase como alternativa justificada; banco e credenciais isolados por protótipo |
| §3 Industrial | ClickHouse só com aprovação/suporte dos administradores |
| §4 + avaliação complementar de deploy | Preparação Docker/Railway; PR e CI; roteiro de preview e publicação; produção a validar |
| §5 Skills | Seis skills versionadas e orientações de reutilização |
| §6 DataViz | Mapeamento prévio de acesso; solução própria corporativa ainda em avaliação |
| §7 3D | Three.js ou Babylon.js conforme necessidade; nenhuma instalada sem caso de uso |
| §8 Knowledge Base | Vault Markdown compatível com Obsidian |
| §9 Ferramentas de IA | Claude/Claude Code prioritários; Copilot complementar; integração direta aprovada |
| §10 9Router | Não recomendar nem incorporar 9Router |
| Princípios corporativos fornecidos pelo solicitante | Precisão, confidencialidade, proteção de credenciais, rastreabilidade, revisão de dados, limites de autonomia e comunicação em AGENTS.md |
| Orientação adicional de 18/10/2026 | Planos, contratação e acessos de Neon/Railway explicitamente em aberto; uso local sem serviços externos |

## Pendências que não devem ser preenchidas por suposição

| Tema | Definição necessária | Situação |
| --- | --- | --- |
| Neon | Plano, contratação, titularidade corporativa, projetos, papéis, concessão/revogação, região, retenção e política de dados | Em aberto; plano não contratado |
| Railway | Plano, contratação, workspace, administradores, papéis, limites/alertas, ambientes, instalação GitHub e concessão/revogação | Em aberto; plano não contratado |
| Identidade dos apps | Autenticação, autorização, eventual SSO e responsáveis | A validar com a área responsável |
| Produção | Hospedagem autorizada, critérios de entrada, observabilidade, suporte e recuperação | A validar com a área responsável |
| Plataforma de dados | Destino corporativo, cronograma e estratégia de migração | A definir com responsáveis |
| DataViz | Solução própria e fluxo operacional de acessos às fontes | Em avaliação |
| IA | Ferramentas/modelos permitidos, dados autorizados, retenção e orçamento | Confirmar por caso de uso |
| GitHub | Equipes, revisores, proteção de branch e política de acesso dos participantes | Configuração administrativa por repositório/organização |

Preços e cotas presentes no documento não são garantias contratuais nem valores atuais confirmados pelo template. Não derivar orçamento ou contratação automática a partir deles.

## Convenções locais da base

FastAPI, Vite, Tailwind 4, uv, npm, pytest, Ruff, ESLint, Python 3.12, Node 22 e um container que serve frontend e API são escolhas de implementação do template, compatíveis com as linguagens definidas. Não constam como exigências no documento corporativo. Os arquivos de lock registram as versões resolvidas.

Registre adaptações locais em [decisoes.md](decisoes.md), mantendo explícita a diferença entre proposta e aprovação. Mudanças de diretriz exigem validação da área responsável.
