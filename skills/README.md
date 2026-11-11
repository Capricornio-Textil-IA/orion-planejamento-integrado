# Skills do treinamento

Cada pasta contém um `SKILL.md` com nome, descrição de uso e um procedimento específico. As regras comuns ficam em [AGENTS.md](../AGENTS.md); as skills não concedem autorização para contratar, publicar, compartilhar informações ou acessar dados.

| Skill | Quando usar |
| --- | --- |
| [capricornio-produto](capricornio-produto/SKILL.md) | Briefing, escopo e implementação de apps internos |
| [capricornio-dados](capricornio-dados/SKILL.md) | Modelagem, consultas, migrações e validação de dados |
| [capricornio-ia](capricornio-ia/SKILL.md) | Integrações diretas e funcionalidades com modelos de IA |
| [capricornio-visualizacoes](capricornio-visualizacoes/SKILL.md) | Dashboards, indicadores e experiências 3D |
| [capricornio-conhecimento](capricornio-conhecimento/SKILL.md) | Documentos internos e base Markdown/Obsidian |
| [capricornio-entrega](capricornio-entrega/SKILL.md) | Verificação, revisão e preparação para deploy |

No Claude Code, use `/capricornio-produto`, por exemplo. As cópias de descoberta ficam em `.claude/skills/` e são geradas por `python3 scripts/sync_skills.py`. O CI rejeita divergências. Em outras ferramentas, peça explicitamente a leitura do arquivo em `skills/` correspondente.

Para criar uma skill de um produto, copie a estrutura de uma pasta, use nome em minúsculas com hífens, descreva **quando** se aplica e inclua somente regras específicas que alterem a implementação. Referencie regras corporativas em vez de duplicá-las. Não coloque dados reais ou credenciais nos exemplos. Registre no AGENTS.md quando a nova skill for relevante e sincronize as cópias.

Essas pastas são instruções versionadas de repositório. Disponibilizá-las em outros produtos ou interfaces pode exigir instalação própria da ferramenta; clonagem não instala automaticamente skills em contas da organização.
