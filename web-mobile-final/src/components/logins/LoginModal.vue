<template>

    <v-dialog v-model="dialog" width="500">

      <template v-slot:activator="{ on }">
        <v-btn text v-on="on">
          login
        </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          로그인
        </v-card-title>


          <EmailLogin @closeModal="chDialog"></EmailLogin>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click=" dialog = false">
              닫기
            </v-btn>
          </v-card-actions>
          </v-card>


    </v-dialog>

</template>

<script>
import EmailLogin from './EmailLogin'


export default {
  name: 'LoginModal',
  components: {
    EmailLogin,
  },
  data () {
    return {
      dialog: false
    }
  },
  methods:{
    chDialog:function(bool){
      this.dialog = bool
    }

  }
}
</script>

<style>
</style>
