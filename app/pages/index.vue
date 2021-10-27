<template>
  <div>
    <b-button to="/retrieve">Retrieve your tickets</b-button>
    <h1>Assign seats to each groups</h1>
    <b-form @submit.prevent="assign()">
      <b-button type="submit">Assign seats to each groups</b-button>
      <Groups v-model="groups" />
    </b-form>
    <hr />
    <b-spinner v-if="isLoading" />
    <Layout v-else :seats="seats" />
  </div>
</template>

<script>
export default {
  async mounted() {
    this.isLoading = true;
    try {
      this.sections = await this.$axios.$get("sections/");
      this.ranks = await this.$axios.$get("ranks/");
      const seats = await this.$axios.$get("seats/");
      this.seats = this.layout(seats);
    } catch (err) {
      this.$bvToast.toast("A problem occur while retrieving the seat layout", {
        title: "An error occurred",
        autoHideDelay: 5000,
        appendToast: false,
        toaster: "b-toaster-top-center",
        solid: true,
        variant: "danger",
      });
    } finally {
      this.isLoading = false;
    }
  },

  data() {
    return {
      isLoading: true,
      groups: [null],
      sections: [],
      ranks: [],
      seats: [],
    };
  },

  methods: {
    layout(seats) {
      const layout = [];
      for (const section of this.sections) {
        const seats_section = seats.filter(
          (seat) => seat.section.id === section.id
        );
        const section_ordered = [];
        for (const rank of this.ranks) {
          const seat_rank = seats_section.filter(
            (seat) => seat.rank.id === rank.id
          );
          if (seat_rank.length === 0) {
            continue;
          }
          const rank_ordered = [];
          const row_ordered = [];
          const row_number = seat_rank[0].row;
          while (seat_rank.length > 0) {
            if (row_number === seat_rank[0].row) {
              row_ordered.push(seat_rank[0]);
              seat_rank.splice(0, 1);
            } else {
              rank_ordered.push(row_ordered);
              row_ordered = [];
              row_number = seat_rank[0].row;
            }
          }
          rank_ordered.push(row_ordered);
          section_ordered.push(rank_ordered);
        }
        layout.push(section_ordered);
      }
      return layout;
    },
    async assign() {
      this.isLoading = true;
      const concatSection = [].concat.apply([], this.seats);
      const concatRank = [].concat.apply([], concatSection);
      const concatRow = [].concat.apply([], concatRank);
      const concatSeat = [].concat.apply([], concatRow);
      const availableSeats = concatSeat.filter(
        (seat) => seat.blocked === false
      ).length;
      const remainingSeats =
        this.groups.reduce((a, b) => a + b, 0) - availableSeats;
      if (remainingSeats > 0) {
        this.$bvToast.toast(
          `You have more people than available seats. Please remove ${remainingSeats} users`,
          {
            title: "Too many people to be seated",
            autoHideDelay: 5000,
            appendToast: false,
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
        this.isLoading = false;
        return;
      }
      try {
        const seats = await this.$axios.$post("seats/assign/", {
          groups: this.groups.filter((group) => group !== null),
        });
        this.seats = this.layout(seats);
        this.groups = [null];
      } catch (err) {
        this.$bvToast.toast("A problem occur while assigning the seats", {
          title: "An error occurred",
          autoHideDelay: 5000,
          appendToast: false,
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "danger",
        });
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>
