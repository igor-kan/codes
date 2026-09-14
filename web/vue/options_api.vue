<script>
export default {
  data() {
    return { message: "Hello from Vue", items: ["a", "b", "c"] };
  },
  computed: {
    reversed() {
      return this.message.split("").reverse().join("");
    },
    itemCount() {
      return this.items.length;
    },
  },
  methods: {
    addItem() {
      this.items.push(`item-${this.items.length + 1}`);
    },
  },
};
</script>

<template>
  <p>{{ message }} — {{ reversed }} ({{ itemCount }})</p>
  <button @click="addItem">Add</button>
</template>
