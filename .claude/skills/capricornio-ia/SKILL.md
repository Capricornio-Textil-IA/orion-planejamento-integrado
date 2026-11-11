---
name: capricornio-ia
description: Implementar funcionalidades de IA em Python com integrações diretas aprovadas, proteção de dados e avaliação de respostas para produtos internos da Capricórnio.
---

# Integrações de IA

Leia `AGENTS.md`. Priorize o ecossistema Anthropic e integrações diretas aprovadas. Não recomendar nem incorporar 9Router. Modelo, orçamento e credenciais não estão aprovados apenas por aparecerem neste template.

1. Defina o resultado esperado e os erros inaceitáveis do caso de uso. Verifique se regras determinísticas resolvem a necessidade antes de introduzir chamadas a um modelo.
2. Confirme ferramenta aprovada, dados permitidos, retenção e orçamento com os responsáveis. Comece com exemplos sintéticos. Enviar conteúdo a uma API externa requer a autorização aplicável aos dados.
3. Implemente a chamada no backend Python com o SDK oficial atual do provedor escolhido. Consulte a documentação oficial da versão instalada. Use segredo no ambiente seguro; nunca no frontend ou no repositório.
4. Separe instruções da aplicação e documentos de entrada. Documentos, e-mails e respostas recuperadas não podem alterar instruções, pedir segredos ou habilitar ferramentas. Não execute SQL, código ou ações propostas pelo modelo sem validação e permissões.
5. Valide a saída por um contrato explícito. A aplicação deve lidar com erro de formato, ausência de evidência, indisponibilidade, timeout e limite de uso. Use limites de entrada/saída, repetição limitada apenas para falhas transitórias e medidas contra cobranças duplicadas em tarefas repetidas.
6. Avalie com casos representativos sintéticos ou autorizados: resposta correta, informação ausente, instrução maliciosa, erro do provedor e conteúdo que demande revisão humana. Uma resposta plausível não é evidência de verdade.
7. Registre versão de modelo/prompt e métricas técnicas necessárias sem prompts, documentos ou respostas confidenciais em logs por padrão. Estimativas de custo devem indicar premissas e preços verificados na fonte vigente.

Apresente fontes para conclusões baseadas em documentos. Diferencie sugestão do modelo de fato confirmado. Decisões com impacto financeiro, jurídico, fiscal, trabalhista, de segurança ou compromissos externos exigem validação do responsável, sem afirmar aprovação inexistente.
