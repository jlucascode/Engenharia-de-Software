<template>
  <section class="main">
    <div>
      <h1>Listagem de Usuários</h1>
      <template v-for="nome in arrayUsers" :key="nome">
        <p>Seu nome é: {{ nome }}</p>
        <p>Seu nome é: {{ nome }}</p>
        <p>Seu nome é: {{ nome }}</p>
        <p>Seu nome é: {{ nome }}</p>
        <p>Seu nome é: {{ nome }}</p>
        <p>Seu nome é: {{ nome }}</p>
        umium
      </template>
    </div>
  </section>
</template>
<script setup>
import { ref } from "vue";
const arrayUsers = ref(["joao", "joana", "teste", "nome", "maria", "jose"]);
</script>
<style scoped>
.main {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
</style>
