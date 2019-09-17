<template>
  <div height="20px">
    <v-toolbar>


    <v-icon color="pink">favorite</v-icon>

      <v-toolbar-title>DungJi's TIL🐣</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items>
          
          <v-btn text @click="gohome">Home</v-btn>
          <LoginModal v-if="!isActive"></LoginModal>
          <SignupModal v-if="!isActive"></SignupModal>
          <v-btn text @click="gomypage" v-if="isActive">{{userEmail}}의 페이지</v-btn>
          <Logout v-if="isActive"></Logout>
          <v-btn v-if="userAuth==='관리자'" text @click="goadmin">Admin</v-btn>

      </v-toolbar-items>

    </v-toolbar>

  </div>

</template>

<script>
import firebase from 'firebase';
import "firebase/firestore";
import "firebase/auth";
import LoginModal from '../logins/LoginModal'
import SignupModal from '../logins/SignupModal'
import Logout from '../logins/Logout'
import MyPage from '../../views/MyPage'
import FirebaseService from "../../plugins/FirebaseService";


export default {
	name: 'Header',
	components: {
    LoginModal,
    SignupModal,
    MyPage,
    Logout
	},
  data() {
    return {
      userAuth: "",
      userEmail: "",
      isActive2: true,
      isActive: false
    }
  },
  computed: {

  },
  watch: {
      firebase: function() {
        this.isActive2 = firebase.auth().currentUser
        //console.log('isactive2d', this.isActive2);
      }
  },
  created() {
    this.isSignedIn()
    this.$root.$on(
      'loggedIn', ()=> {
      this.isActive = true;
      this.userEmail = firebase.auth().currentUser.email;
      this.userEmail = this.userEmail.split('@')[0]
      // console.log()
    }
    //this.$root.$on(
    //      'loggedOut', ()=> {
    //this.isActive = false;
    //alert("들어옴")
      //this.userEmail = firebase.auth().currentUser.email;
    //}

    )
  },
  mounted () {
    this.getAuth()
    
  },


  methods: {
    getAuth() {
      firebase.auth().onAuthStateChanged(user => {
        if (user) {

          FirebaseService.getUserAuth(user.email).then(res => {
            this.userAuth = res
          })
        }
      })
    },
    goadmin() {
      location.href = '/admin'
    },
    gomypage() {
      //location.href = '/mypage'
      this.$router.replace('/mypage')
    },
    gohome() {
      //location.href = '/'
      this.$router.replace('/')
    },


    async isSignedIn() {
      var user = firebase.auth().currentUser

        if (user) {

          this.userEmail = user.email;
          //this.isActive = true

        } else {

          this.userEmail = "Guest";
          //this.isActive = false
        }
      }


    }



   }


</script>

<style>

</style>
