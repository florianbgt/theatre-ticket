<template>
  <div>
    <b-button to="/">Back to homepage</b-button>
    <h1>Assign seats to each groups</h1>
    <b-form @submit.prevent="assign()">
      <b-button type="submit">Assign seats to each groups</b-button>
      <b-row>
        <b-col v-for="(group, index) in groups" :key="index" cols="12" sm="6">
          <b-form-group
            :label="`Group #${index + 1} - How many people in your party?`"
          >
            <b-input-group>
              <b-form-input
                v-model.number="groups[index]"
                type="number"
                min="0"
                step="1"
              />
              <b-button
                v-if="index == groups.length - 1"
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
    </b-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      groups: [null]
    };
  },

  methods: {
    add() {
      if (this.groups[this.groups.length - 1] !== null) {
        this.groups.push(null);
      } else {
        this.$bvToast.toast(
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
      }
    },
    remove(index) {
      this.groups.splice(index, 1);
    },
    async assign() {
      const response = await this.$axios.$post(
        "http://localhost:8000/seats/assign/",
        {
          groups: this.groups.filter(group => group !== null)
        }
      );
      if (response.length == 0) {
        this.$bvToast.toast(
          "A problem occur while assigning the seats",
          {
            title: "An error occurred",
            autoHideDelay: 5000,
            appendToast: false,
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger"
          }
        );
      }
      this.tickets = response;
    }
  }
};
</script>
