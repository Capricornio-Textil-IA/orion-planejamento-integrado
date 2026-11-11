# Diretrizes — transcrição da fonte fornecida

Fonte: `Capricornio_Diretrizes_IA_Versao_Final.docx`, fornecido pelo solicitante. Texto extraído dos parágrafos do documento em 18/10/2026; a formatação e os hiperlinks originais não são reproduzidos.

SHA-256 do DOCX original: `d1e75a293d2c28eaa74a6549f464375a8cb0e53be9c8b10fe1ae139868e27b5a`.

Esta é uma transcrição histórica. Preços e cotas abaixo não foram revalidados e não indicam contratação. Para a aplicação no template e a orientação posterior de manter contratação e acessos de Neon/Railway em aberto, consulte [stack-e-governanca.md](stack-e-governanca.md).

---

REFERENCIAL DE TECNOLOGIA E GOVERNANÇA

Diretrizes para construção de produtos de IA

Contexto. No Programa de Adoção de IA da Capricórnio Têxtil, estas diretrizes estabelecem uma base comum para desenvolver protótipos e evoluí-los para produtos corporativos. As escolhas buscam facilitar a colaboração entre áreas, o reaproveitamento de soluções e a governança de código, dados e acessos. Os pontos ainda não definidos serão validados com as equipes responsáveis antes da entrada em produção.

1. Versionamento de código

•  Centralizar os repositórios na organização Capricornio-Textil-IA no GitHub, assegurando histórico de alterações, colaboração e continuidade dos projetos.

•  Utilizar contas vinculadas ao e-mail corporativo da Capricórnio para manter os acessos sob gestão institucional.

TO-DO  ✓ Concluído — Organização da Capricórnio no GitHub identificada: Abrir organização

2. Linguagens de programação

•  Adotar Python para aplicações e integrações com IA, e SQL para consultas e manipulação de dados.

•  Utilizar JavaScript no desenvolvimento web e Tailwind CSS para padronizar a construção das interfaces.

3. Banco de dados

•  Usar um ambiente centralizado no Supabase para protótipos, simplificando a criação e o compartilhamento das primeiras soluções.

•  Planejar a migração dos produtos para a nova plataforma corporativa de dados conforme sua implantação e os requisitos de produção.

•  Para aplicações industriais, aproveitar o ClickHouse existente, com orientação e suporte dos administradores da plataforma.

TO-DO  Pendente — Pesquisar os planos do Supabase e recomendar o mais adequado à Capricórnio.

4. Deploy

•  Definir um processo padronizado para publicação das aplicações, com controle de permissões, configurações e ambientes.

•  A tecnologia de hospedagem e os critérios de entrada em produção permanecem em definição com a área responsável.

TO-DO  Pendente — Pesquisar ferramentas que simplifiquem o deploy de protótipos e comparar os planos mais adequados à Capricórnio.

5. Skills e templates

•  Disponibilizar templates de Skills na organização da Capricórnio no GitHub, permitindo clonagem e adaptação pelas equipes.

•  Versionar os templates e registrar orientações mínimas de uso para facilitar o reaproveitamento entre projetos.

TO-DO  Pendente — Elaborar as Skills e disponibilizá-las em um repositório template dentro da organização no GitHub.

6. DataViz

•  Mapear os acessos necessários às fontes de dados e aos recursos de visualização antes de iniciar os dashboards.

•  Estabelecer o fluxo operacional para solicitação, concessão e manutenção desses acessos.

TO-DO  Pendente — Avaliar uma solução própria de DataViz, com deploy na mesma stack, permitindo publicar dashboards apenas editando o repositório no GitHub.

7. Modelagem 3D

•  Adotar Three.js e Babylon.js como bibliotecas de referência para aplicações de visualização 3D no navegador.

•  Selecionar a biblioteca conforme a necessidade de interação, desempenho e complexidade de cada produto.

8. Knowledge Base

•  Utilizar Obsidian para estruturar bases de conhecimento em arquivos Markdown, facilitando consulta e atualização.

•  Padronizar a organização de pastas e documentos para tornar o conhecimento reutilizável entre áreas e projetos.

9. Ferramentas de IA

•  Priorizar o ecossistema Anthropic, com Claude para apoio às atividades e Claude Code para desenvolvimento assistido.

•  Considerar Copilot como ferramenta complementar de assistência à programação, conforme os acessos disponíveis.

10. 9Router

•  Não recomendar o uso do 9Router nas soluções desenvolvidas no programa.

•  Preferir integrações diretas e ferramentas aprovadas pela Capricórnio, sujeitas aos controles corporativos de acesso e segurança.

Avaliação complementar | Banco de dados

•  Recomendação. Neon Free como padrão para ~10 protótipos: até 100 projetos independentes, 1 GB de PostgreSQL e 100 CU-h/mês por projeto, sem mensalidade.

•  Evolução recomendada. Neon Launch, pago por consumo e sem mensalidade mínima, para casos que superarem as cotas ou exigirem maior retenção e capacidade.

•  Supabase como alternativa. Pro: US$ 25/mês pelo primeiro projeto Micro + ~US$ 10 por Micro adicional (10 projetos ≈ US$ 115/mês). Válido se sua integração nativa justificar o custo.

•  Governança. Isolar banco e credenciais por protótipo, usar permissões por projeto e dados sintéticos ou autorizados; acesso industrial ao ClickHouse só com aprovação dos administradores.

•  Atualização de diretriz. Esta recomendação substitui o Supabase citado na seção 3 da página 1 apenas na prototipação; migração futura para a plataforma corporativa permanece.

Fontes (18/10/2026): neon.com/blog/neon-free-plan-1-gb-per-project · neon.com/pricing · supabase.com/pricing

Avaliação complementar | Deploy

•  Recomendação. Railway Pro: US$ 20/mês por workspace, com US$ 20 de consumo incluído. Hospeda múltiplos apps Python/JS com cobrança de CPU e RAM por uso, sem tarifa fixa por aplicativo.

•  Fluxo. Template na organização GitHub → PR aprovado e testes → preview temporário → deploy automático. Guardar segredos no Railway e configurar acesso individual ao Neon.

•  Governança. Equipe e papéis corporativos, 30 dias de auditoria no Pro, alertas/limites de gastos. Apps ociosos podem hibernar, mas o recurso depende do tráfego e gera cold start.

•  Comparação. Render Pro: US$ 25/mês + US$ 7 por serviço Starter (≈ US$ 95/mês para 10 serviços ativos); mais previsível para apps contínuos. Railway pode passar de US$ 20 conforme o consumo.

Fontes (18/10/2026): docs.railway.com/pricing · docs.railway.com/deployments/serverless · render.com/pricing
