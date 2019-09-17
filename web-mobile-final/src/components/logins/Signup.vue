<template>
<v-card-text>

  <v-container>

      <div class="sign-up">
        <p>계정 만들기</p>
        <input type="text" id='useremail' v-model="email" placeholder="Email"><br>
        <input type="password" v-model="password" placeholder="Password" v-on:keyup.enter="signUp"><br>
        <br>
        <v-btn v-on:click="signUp">Sign Up</v-btn>
      </div>

  </v-container>
</v-card-text>
</template>

<script>

import firebase from 'firebase'
import FirebaseService from '../../plugins/FirebaseService'
export default {
  name: 'SignUp',
  components: {

	},
  data () {
    return {
      email: '',
      password: '',

    }
  },
  methods: {


    signUp : function() {
      firebase.auth().createUserWithEmailAndPassword(this.email, this.password)
      .then(
        function (user) {
          FirebaseService.signup(useremail.value)
          .then(function() {
              alert('회원가입 되었습니다.')

          window.location.href="/"
          // FirebaseService.alert()
          })
          

        },
        function (err) {
          alert('다시 작성해주세요.')
        }
      );
    }

  }

}
</script>

<style>
</style>
