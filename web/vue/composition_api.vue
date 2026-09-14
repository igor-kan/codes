<script setup>
import { computed, ref } from "vue";

const count = ref(0);
const doubled = computed(() => count.value * 2);

function increment() {
  count.value += 1;
}
</script>

<template>
  <button type="button" @click="increment">
    count is {{ count }} (doubled: {{ doubled }})
  </button>
</template>

<style scoped>
button { padding: 0.5rem 1rem; border-radius: 0.5rem; }
</style>
