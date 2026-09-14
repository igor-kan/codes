<script setup>
import { reactive, ref, watch } from "vue";

const seconds = ref(0);
const state = reactive({ running: false, label: "idle" });

watch(seconds, (value) => {
  state.label = value >= 10 ? "long" : "short";
});

let timer;
function toggle() {
  state.running = !state.running;
  if (state.running) {
    timer = setInterval(() => (seconds.value += 1), 1000);
  } else {
    clearInterval(timer);
  }
}
</script>

<template>
  <button @click="toggle">{{ state.running ? "Stop" : "Start" }}</button>
  <span>{{ seconds }}s ({{ state.label }})</span>
</template>
