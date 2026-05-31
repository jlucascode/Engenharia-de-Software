<template>
  <section class="main">
    <form @submit="processarDados($event)">
      <div class="form">
        <input type="text" v-model="email" placeholder="Digite seu email" />
        <input type="text" v-model="nome" placeholder="Digite seu nome" />
        <button type="submit">Enviar dados</button>
      </div>
    </form>

    <div v-if="visivel">
      <p>Seu email é: {{ email }}</p>
      <p>Seu nome é: {{ nome }}</p>
      <p>Seu nome é: {{ nome }}</p>
      <p>Seu nome é: {{ nome }}</p>
      <p>Seu nome é: {{ nome }}</p>
      <p>Seu nome é: {{ nome }}</p>
      <p>Seu nome é: {{ nome }}</p>
      <p>Seu nome é: {{ nome }}</p>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const nome = ref("");
const email = ref("");
const visivel = ref(false);

function processarDados(evento) {
  evento.preventDefault();
  visivel.value = true;
}
</script>

<style scoped>
.main {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 10px;
  background-color: gray;
  padding: 20px;
  border-radius: 20px;
  & input,
  button {
    background-color: rgb(189, 230, 230);
    padding: 10px;
    outline-color: rgb(39, 19, 19);
    border-radius: 10px;
  }
}
</style>
