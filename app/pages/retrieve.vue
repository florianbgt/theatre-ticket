<template>
  <div>
    <b-button to="/">Back to homepage</b-button>
    <h1>Retrieve the tickets for your group</h1>
    <form @submit.prevent="getTickets()">
      <b-row>
        <b-col cols=12 sm=6>
          <b-form-group label="Enter your group #">
            <b-input-group>
              <b-form-input v-model="group" type="number" min="0" step="1" />
              <b-button class="h-100" type="submit">Retrieve tickets</b-button>
            </b-input-group>
          </b-form-group>
        </b-col>
      </b-row>
    </form>
    <p v-if="tickets.length == 0">
      <strong>
        To get your tickets, input your group # and click on "Retrieve tickets"
      </strong>
    </p>
    <b-row v-else>
      <b-col v-for="ticket in tickets" :key="ticket.id">
        <b-table-simple bordered striped>
          <b-thead>
            <b-th colspan="2" class="text-center text-light bg-dark"
              >Ticket #{{ ticket.number }}</b-th
            >
          </b-thead>
          <b-tbody>
            <b-tr>
              <b-th>Section</b-th>
              <b-td>{{ ticket.section.name }}</b-td>
            </b-tr>
            <b-tr>
              <b-th>Rank</b-th>
              <b-td>{{ ticket.rank.name }}</b-td>
            </b-tr>
            <b-tr>
              <b-th>Row #</b-th>
              <b-td>{{ ticket.row }}</b-td>
            </b-tr>
            <b-tr>
              <b-th>Seat #</b-th>
              <b-td>{{ ticket.number }}</b-td>
            </b-tr>
            <b-tr>
              <b-th colspan="2" class="text-center">Seat type</b-th>
            </b-tr>
            <b-tr>
              <b-td colspan="2" class="text-center">
                {{ ticket.is_aisle ? "Aisle - " : ""
                }}{{ ticket.is_balcony ? "Balcony" : "Main floor" }}
              </b-td>
            </b-tr>
          </b-tbody>
        </b-table-simple>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      group: null,
      tickets: []
    };
  },
  methods: {
    async getTickets() {
      const response = await this.$axios.$post(
        "http://localhost:8000/seats/retrieve/",
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
    }
  }
};
</script>
