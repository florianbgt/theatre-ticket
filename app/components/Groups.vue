<template>
  <b-row>
    <b-col v-for="(group, index) in value" :key="index" cols="12" sm="6" lg="4">
      <b-form-group
        :label="`Group #${index + 1} - How many people in your party?`"
      >
        <b-input-group>
          <b-form-input
            v-model.number="value[index]"
            type="number"
            min="0"
            step="1"
          />
          <b-button
            v-if="index == value.length - 1"
            @click="add()"
            class="h-100"
            variant="success"
          >
            Add another group
          </b-button>
          <b-button
            v-else
            @click="remove(index)"
            class="h-100"
            variant="warning"
          >
            Remove this group
          </b-button>
        </b-input-group>
      </b-form-group>
    </b-col>
  </b-row>
</template>

<script>
export default {
  props: {
    value: { type: Array, required: true }
  },
  methods: {
    add() {
      if (this.value[this.value.length - 1] === null) {
        this.$root.$bvToast.toast(
          "Please assign the number of people in the last group before adding a new one",
          {
            title: "Last group is not assigned",
            autoHideDelay: 5000,
            appendToast: false,
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger"
          }
        );
        return;
      }
      const groups = this.value
      groups.push(null)
      this.$emit('input', groups)
    },
    remove(index) {
        const groups = this.value
        groups.splice(index, 1)
        this.$emit('input', groups)
    }
  }
};
</script>
