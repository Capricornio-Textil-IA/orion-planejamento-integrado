# Preparação de publicação

**Situação atual: Neon e Railway sem plano contratado; acessos, papéis e responsáveis em aberto.** Este roteiro descreve preparação e etapas futuras. Não houve provisionamento de banco, workspace ou aplicação hospedada por este template.

## O que já é possível localmente

- Executar API e interface, testar e gerar o build com os comandos do README.
- Construir a imagem Docker quando houver daemon Docker disponível. O frontend é compilado no build e apenas os arquivos de `app/static/` são servidos. O processo respeita `PORT`, roda como usuário sem privilégios e expõe `/api/health`.
- Planejar contratos, dados, autenticação, modelo SQL e migrações usando dados sintéticos. O template não inclui driver de banco ou SDK de IA sem uma funcionalidade que os demande.
- Revisar PRs e executar CI. Não é necessário fornecer credenciais de Neon, Railway ou Anthropic ao pipeline inicial.

## Definições antes da ativação dos serviços

A área responsável precisa definir contratação, plano, titularidade, administradores, papéis, concessão/revogação de acessos, ambientes, região, dados permitidos e limites/alertas de gasto. Não criar contas pessoais em substituição à titularidade corporativa.

Para Neon, definir isolamento de banco e credenciais por protótipo, permissões por projeto, backup e recuperação. Para Railway, definir workspace corporativo, acesso à organização GitHub, visibilidade das aplicações, domínio e segredos por ambiente. As condições comerciais devem ser verificadas antes de qualquer contratação.

Para um app com dados internos, validar solução de autenticação e autorização **no backend**. Uma URL difícil de adivinhar, uma interface sem botão ou um repositório privado não restringem o acesso ao app publicado.

## Fluxo futuro, após contratação e acessos liberados

1. O administrador concede somente os papéis necessários. O responsável registra no projeto o ambiente e a autorização aplicável, sem valores de credenciais.
2. Desenvolva em branch e abra PR. Exija revisão e verificações passando; configure proteção de branch/revisores administrativamente no novo repositório. Essas configurações não são herdadas automaticamente do template.
3. Gere preview temporário em ambiente separado com dados sintéticos. Confirme a disponibilidade e as configurações do recurso no plano contratado, a execução do CI e a restrição de acesso antes de habilitar preview automático para PRs. Não envie segredos de produção a código de PR não revisado. Encerre recursos temporários ao terminar.
4. Quando houver persistência implementada, crie banco/projeto Neon isolado para o protótipo e configure `DATABASE_URL` no gerenciador seguro do ambiente de backend. Não a coloque em código, chat, variável `VITE_*` ou logs. Configure TLS e conceda o menor privilégio necessário. Migrações exigem validação e autorização compatíveis com o impacto.
5. Conecte o repositório privado do produto a um serviço Railway autorizado. Use a raiz do repositório como contexto do Dockerfile e mantenha o `railway.toml`. Configure segredos por ambiente sem compartilhá-los no repositório.
6. Para deploy automático da branch aprovada, habilite **Wait for CI** nas configurações do serviço e confirme as permissões da integração GitHub. O workflow inclui `push` em `main`, requisito desse recurso. `railway.toml` não habilita Wait for CI por si só.
7. Após aprovação do PR e validação do preview, integre na branch de deploy e verifique commit publicado, `/api/health`, comportamento do produto, autenticação/autorização, ausência de vazamento de logs e limites de consumo. Healthcheck não comprova integridade do banco nem autorização do produto.
8. Documente como retornar à versão anterior e recuperar dados antes de mudanças de schema. Reverter código não reverte automaticamente migrações nem perdas de dados.

O fluxo detalhado de preview, integração e publicação depende dos ambientes e papéis que forem contratados e aprovados. O template não presume que toda funcionalidade comercial estará disponível.

## Produção

Os critérios de entrada e a hospedagem autorizada de produção continuam sujeitos à área responsável. Validar segurança, disponibilidade, suporte, observabilidade, tratamento de dados, recuperação e compromissos financeiros. Planejar a migração para a plataforma corporativa de dados conforme sua implantação. Protótipo publicado não equivale a produto aprovado para produção.

## Referências técnicas

- [FastAPI em containers](https://fastapi.tiangolo.com/deployment/docker/)
- [uv em Docker](https://docs.astral.sh/uv/guides/integration/docker/)
- [Tailwind com Vite](https://tailwindcss.com/docs/installation/using-vite)
- [Conexão de aplicações ao Neon](https://neon.com/docs/connect/connect-from-any-app)
- [Dockerfile no Railway](https://docs.railway.com/builds/dockerfiles)
- [Autodeploy e Wait for CI](https://docs.railway.com/deployments/github-autodeploys)
- [Skills de projeto no Claude Code](https://code.claude.com/docs/en/skills)

Documentação técnica consultada na preparação da base em 18/10/2026. Condições e permissões do plano efetivamente contratado precisam de verificação própria.
