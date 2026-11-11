---
name: capricornio-entrega
description: Verificar entregas e preparar publicação de produtos da Capricórnio com PR, testes, configuração e tratamento explícito das pendências de Neon e Railway.
---

# Entregar e preparar deploy

Leia `AGENTS.md` e `docs/deploy.md`. Planos, contratação e acessos de **Neon e Railway estão pendentes**. Preparar arquivos e instruções é possível sem provisionar, contratar ou assumir permissões.

1. Verifique os critérios de aceite e rode as checagens pertinentes do README. Para a base completa, execute lint/formatação/testes Python, lint/build JavaScript, sincronização de skills e build do Docker quando o daemon estiver disponível. Informe o que não foi executado.
2. Revise o diff para remover credenciais, dados reais não autorizados, logs sensíveis e artefatos gerados. Confirme que a configuração pública não contém segredos. Evite expor informações internas até em mensagens de commit e PR.
3. Abra PR com problema, comportamento final, evidências e riscos. Não declare revisão humana concluída sem evidência. Proteção de branch e revisores precisam de configuração administrativa; um checklist não os impõe.
4. Se o pedido for apenas preparar, entregue os arquivos e a lista objetiva de pendências. Se incluir publicar, confirme autorização existente, acesso efetivo, ambiente e custos previstos antes de executar operações externas. Não peça novamente autorização já dada para a mesma ação e escopo.
5. Quando a contratação e os acessos forem liberados, siga `docs/deploy.md` para papéis corporativos, configuração de segredos, ambientes isolados, banco por protótipo, limites de gasto, Wait for CI, preview com dados sintéticos e verificação pós-deploy.
6. Antes de dados internos ou produção, a área responsável deve validar autenticação/autorização, permissões, observabilidade, backup/recuperação e plano de migração de dados. O pipeline inicial não certifica esses requisitos.

Informe separadamente o que foi preparado, testado localmente, validado no CI e publicado com evidência. Não afirme contratação ou acesso concedido a partir de configuração presente no repositório.
