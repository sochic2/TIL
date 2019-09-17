<template>
  <v-app>
    <Header>
    </Header>
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer>
    </Footer>
  </v-app>
</template>

<script>

import firebase from "firebase";
import Header from './components/navbars/Header.vue'
import Footer from './components/footer/Footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  },

  data: () => ({
    //
    userEmail: ""
  }),
  mounted() {
      firebase.auth().onAuthStateChanged(user => {
      if (user) {
        // User is signed in.
        //console.log(user.email);
        this.userEmail = user.email;
        this.$root.$emit('loggedIn')
        //console.log("!!!")
      } else {
        this.userEmail = "Guest";
        //console.log(this.userEmail)
        this.$root.$emit('loggedOut')
        //console.log("???")
        // No user is signed in.
      }
    });


  }
};
</script>
