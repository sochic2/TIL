<template>
 <v-container>
    <v-layout text-center wrap>
      <v-flex xs12>
        <v-img
          class="my-3"
          contain
          height="30"
        ></v-img>
      </v-flex>
       <PublicCalendar />
    </v-layout>
  </v-container>
</template>

<script>
import PublicCalendar from '../components/calendars/PublicCalendar';

export default {
  components: {
    PublicCalendar,
  },
};
</script>
