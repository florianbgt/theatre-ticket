<template>
  <div>
    <div
      v-for="(section, index) in seats"
      :key="`section-${index}`"
      class="border mb-2"
    >
      <h2 class="bg-success text-light text-center mb-0">
        {{ section[0][0][0].section.name }} Section
      </h2>
      <div v-for="(rank, index) in section" :key="`rank-${index}`">
        <h3 class="bg-warning text-center mb-0">
          {{ rank[0][0].rank.name }}
        </h3>
        <b-table-simple
          v-for="(row, index) in rank"
          :key="`row-${index}`"
          small
          stripped
          bordered
          class="mb-0"
        >
          <b-thead head-variant="dark">
            <b-tr>
              <b-th colspan="100%" class="text-center">
                Row #{{ row[0].row }}
              </b-th>
            </b-tr>
          </b-thead>
          <b-tbody>
            <b-tr>
              <b-th v-for="(seat, index) in row" :key="`th-seat-${index}`">
                #{{ seat.number }}
              </b-th>
            </b-tr>
            <b-tr>
              <b-td v-for="(seat, index) in row" :key="`td-seat-${index}`">
                {{ !!seat.user ? `Group ${seat.user}` : "Available" }}
              </b-td>
            </b-tr>
          </b-tbody>
        </b-table-simple>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    seats: { type: Array, required: true }
  }
};
</script>
