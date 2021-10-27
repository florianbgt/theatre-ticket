<template>
  <div>
    <b-button to="/">Back to homepage</b-button>
    <h1>Retrieve the tickets for your group</h1>
    <form @submit.prevent="getTickets()">
      <b-row>
        <b-col cols="12" sm="6">
          <b-form-group label="Enter your group #">
            <b-input-group>
              <b-form-input v-model="group" type="number" min="0" step="1" />
              <b-button class="h-100" type="submit">Retrieve tickets</b-button>
            </b-input-group>
          </b-form-group>
        </b-col>
      </b-row>
    </form>
    <b-spinner v-if="isLoading" />
    <p v-else-if="tickets.length == 0">
      <strong>
        To get your tickets, input your group # and click on "Retrieve tickets"
      </strong>
    </p>
    <Tickets v-else :tickets="tickets"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoading: false,
      group: null,
      tickets: []
    };
  },
  methods: {
    async getTickets() {
      this.isLoading = true;
      try {
        const response = await this.$axios.$post(
          "seats/retrieve/",
          {
            group: this.group
          }
        );
        if (response.length == 0) {
          this.$bvToast.toast(
            "No tickets available for this group. Are you sure you entered the correct group #?",
            {
              title: "No reccords found",
              autoHideDelay: 5000,
              appendToast: false,
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "danger"
            }
          );
        }
        this.tickets = response;
      } catch (err) {
        this.$bvToast.toast("An error occured on the server", {
          title: "An error occured",
          autoHideDelay: 5000,
          appendToast: false,
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "danger"
        });
      } finally {
        this.isLoading = false;
      }
    }
  }
};
</script>
