<template>
    <v-btn text @click="Logout">Logout</v-btn>

</template>


<script>

import firebase from 'firebase'
import FirebaseService from '../../plugins/FirebaseService'
export default {
  name: 'Logout',

  methods: {

    Logout : function() {

      firebase.auth().signOut()
      // this.$root.$emit('loggedOut')
      //this.reset()
      alert("로그아웃")
      //this.$router.go('/mypage')
      location.href = '/'


    }

  }

}
</script>
