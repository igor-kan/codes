<script setup>
import { defineEmits, defineProps } from "vue";

const props = defineProps({
  title: { type: String, required: true },
  tone: { type: String, default: "neutral" },
});
const emit = defineEmits(["select"]);

function pick() {
  emit("select", props.title);
}
</script>

<template>
  <article :class="`card card--${tone}`" @click="pick">
    <h2>{{ title }}</h2>
    <slot />
  </article>
</template>
