---
name: capricornio-produto
description: Definir e implementar apps de produtos internos da Capricórnio a partir de um problema e critérios de aceite, respeitando a stack do treinamento.
---

# Construir um produto interno

Leia `AGENTS.md`, `docs/produto.md` e `docs/stack-e-governanca.md` a partir da raiz do repositório. Preserve o que já foi definido pelo solicitante.

1. Identifique problema, público, responsável de negócio e menor resultado verificável. Se faltar detalhe não essencial, registre a premissa e avance; pergunte quando a ausência impedir uma implementação confiável.
2. Registre critérios de aceite observáveis e a classificação/origem dos dados no briefing. Não invente políticas, indicadores ou requisitos como se fossem aprovados.
3. Implemente um fluxo pequeno de ponta a ponta. Use Python/FastAPI no servidor, SQL quando houver dados e JavaScript/Vite com Tailwind na interface. Reaproveite a estrutura existente e mantenha regras de negócio no servidor.
4. Desenvolva com dados sintéticos claramente identificados. Sem acesso a Neon/Railway, mantenha o fluxo local e explicite qualquer persistência simulada. Não adicione banco ou serviço substituto como decisão corporativa.
5. Trate carregamento, vazio, erro, sucesso e acessibilidade. Antes de dados internos, implemente identidade e autorização no servidor com a solução validada pela empresa; não invente um provedor corporativo.
6. Verifique os critérios de aceite e os comandos pertinentes do README. Atualize o briefing, decisões e instruções afetadas.

Apresente o comportamento entregue, evidências de validação, premissas e pendências de acesso. Use a skill de dados, IA ou visualização somente quando o produto exigir essas capacidades.
