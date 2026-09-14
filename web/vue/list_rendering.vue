<script setup>
import { ref } from "vue";

const users = ref([
  { id: 1, name: "Ada" },
  { id: 2, name: "Grace" },
]);
</script>

<template>
  <ul>
    <li v-for="user in users" :key="user.id">{{ user.name }}</li>
  </ul>
  <p v-if="users.length === 0">No users.</p>
  <p v-else>{{ users.length }} users.</p>
</template>
