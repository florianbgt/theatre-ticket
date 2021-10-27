<template>
  <b-row>
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
</template>

<script>
export default {
  props: {
    tickets: { type: Array, required: true }
  }
};
</script>
