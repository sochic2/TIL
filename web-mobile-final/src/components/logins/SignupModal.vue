<template>

    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" text v-on="on">
          Signup
        </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          Signup
        </v-card-title>

        <Signup></Signup>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            닫기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

</template>

<script>
import Signup from './Signup'

  export default {
    name: 'SignupModal',
    components: {
      Signup
    },
    data () {
      return {
        dialog: false,
      }
    },
  }
</script>

<style>
</style>
