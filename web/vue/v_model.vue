<script setup>
import { computed } from "vue";

const model = defineModel({ type: String, default: "" });
const length = computed(() => model.value.length);
</script>

<template>
  <input v-model="model" placeholder="Type here" />
  <small>{{ length }} characters</small>
</template>
