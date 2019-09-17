<template>

  <v-footer
    color="grey lighten-1"
    padless
  >
    <v-layout
      justify-center
      wrap
    >
      <v-btn
        v-if="loginuser !== 'null'"
        color="white"
        text
        rounded
        class="my-2"
        @click="FooterWithdrawal()"
      >
        탈퇴하기
      </v-btn>

      <v-flex
        black
        lighten-2
        py-4
        text-center
        white--text
        xs12
      >

        {{ new Date().getFullYear() }} — <strong>gUgUgU</strong>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>
  import FirebaseService from "../../plugins/FirebaseService";
  import firebase from "firebase"
  import 'firebase/auth'
  export default {
    name: 'Footer',


    data: () => ({
      loginuser:"null"
    }),
    methods : {
      FooterWithdrawal() {
        var value = confirm("정말 탈퇴하시겠습니까?")
        if (value === true){
        FirebaseService.Withdrawl()
      }
      else{

      }
    },


    logincheck() {
      firebase.auth().onAuthStateChanged(user => {
        if (user) {
          this.loginuser = user.email;
        }
        else {
        }
      })
    }

  },
    mounted()  {
      this.logincheck()
    },


}
</script>

<style>
</style>
