## 2) Arquivo principal (ex.: src/main.js)
- Ponto de entrada da app: cria a instância, registra plugins e monta no DOM.
- Exemplo mínimo (Composition API + Vite):
```js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import pinia from './stores'

createApp(App)
    .use(router)
    .use(pinia)
    .mount('#app')
```
- Coisas comuns: registrar componentes globais, diretivas personalizadas, configurar i18n ou bibliotecas UI.

## 3) Conceitos essenciais que todo iniciante precisa entender
- Reatividade: mudanças nos dados atualizam a UI automaticamente.
- Componentes: unidades reutilizáveis (SFC — template, script, style).
- Template vs JavaScript: templates declarativos, lógica no script.
- Ciclo de vida: created/mounted/updated/unmounted — entender quando executar efeitos.
- Composition API vs Options API: Composition (setup, refs, reactive, computed) é recomendado hoje.

## 4) Sintaxe básica e diretivas úteis
- Interpolação: {{ mensagem }}
- Bind: :src="img" (v-bind)
- Eventos: @click="handle" (v-on)
- Condicional: v-if / v-else / v-show
- Listas: v-for="item in list" :key="item.id"
- Formulários: v-model para inputs
- Exemplo curto:
```html
<input v-model="texto" />
<ul><li v-for="t in tarefas" :key="t.id">{{ t.nome }}</li></ul>
```

## 5) Componentes SFC (Single File Components)
- Estrutura: <template>, <script>, <style>
- Props: passagem de dados do pai para o filho
- Emit: filho notifica o pai (emit('evento', payload))
- Slots: conteúdo passado para o filho (default/named)
- Isolar estilos com scoped quando necessário

## 6) Comunicação entre componentes
- Pai -> Filho: props
- Filho -> Pai: emits
- Irmãos: via pai ou via store
- Provide / Inject: para dependências em árvore profunda
- Store global: Pinia (recomendado) para estado compartilhado

## 7) Roteamento e estado
- vue-router: rotas definidas com componentes, usar <router-link> e <router-view>
- Pinia: criar stores reativas, ações e getters
- Boas práticas: manter rotas simples, stores para estado global (autenticação, preferências)

## 8) Ferramentas e fluxo de trabalho
- Iniciar rápido: CDN (teste) ou create-vue (Vite) para projetos reais
- Scripts: dev (vite), build, preview
- Devtools: Vue Devtools para inspecionar state e componentes
- Lint & Format: ESLint + Prettier
- Testes: unit (Vitest/Jest) e E2E (Cypress)

## 9) Boas práticas para iniciantes
- Componentes pequenos e com responsabilidade única
- Nomear props e eventos claramente
- Validar props quando possível
- Evitar mutar props diretamente
- Preferir Composition API para novas habilidades; aprender Options API ajuda a ler exemplos antigos

## 10) O que você precisa conseguir mexer (práticas/mini-projetos)
- Criar componentes reutilizáveis (botões, modais, listas)
- Fazer formulários com validação básica
- Consumir API (fetch/axios) e mostrar dados
- Gerenciar estado simples com Pinia
- Navegação entre páginas com vue-router
- Empacotar e publicar (build + deploy em Netlify/Vercel)

## 11) Próximos passos e recursos
- Docs oficiais: vuejs.org (Português/EN)
- Tutorial: criar um Todo app completo
- Comunidade: Discord, fóruns e cursos práticos
- Pratique lendo código de projetos e criando pequenas features regularmente

Resumo rápido: aprenda reatividade, componentes, diretivas básicas, props/emits, roteamento e um store. Pratique com mini-projetos (todo, CRUD, autenticação simples) e use ferramentas modernas (Vite, Pinia, Vue Router, Devtools).