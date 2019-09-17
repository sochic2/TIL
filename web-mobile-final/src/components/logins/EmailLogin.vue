<template>
  <v-card-text>
    <v-container>
      <div class="login">
        <div>
          <h3>Sign In</h3>
          <br />
          <input type="text" v-model="email" placeholder="Email click" style=" width: 28rem; height:30px; border:lightgray 1px solid;"/>
          <br />
          <input type="password" v-model="password" placeholder="Password click" v-on:keyup.enter="signIn"  style="margin-top:5px; width: 28rem; height:30px; border:lightgray 1px solid;"/>
          <br />
          <br />
          <button v-on:click="signIn" style="width: 28rem; background-color: darkgray; color:white; font-size:12px; padding:5px 30px">Login</button>
          <br />
          <br />
          <hr />
        </div>

        <div class="mt-3">
          <p>회원가입 안하셨나요?</p>
          <SignupModal></SignupModal>
        </div>

        <!-- google login -->
        <v-btn rounded color="#df4a31" dark v-on:click="loginWithGoogle" style="width:100%;">
          <v-icon size="25" class="mr-2">fa-google</v-icon>Google 로그인
        </v-btn>
        <!-- facebook login -->
        <v-btn rounded color="blue" dark v-on:click="loginWithFacebook" style="width:100%;">
          <v-icon size="25" class="mr-2">fa-facebook</v-icon>Facebook 로그인
        </v-btn>
      </div>
    </v-container>
  </v-card-text>
</template>

<script>
import SignupModal from "./SignupModal";
import firebase from "firebase";
import FirebaseService from "../../plugins/FirebaseService";
import "firebase/firestore";
import "firebase/auth";

export default {
  name: "login",
  components: {
    SignupModal
  },
  data: function() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    signIn: function() {
      firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION)
      .then((user) => {
        firebase.auth().signInWithEmailAndPassword(this.email, this.password)
        .then((user) => {
          alert('로그인 되었습니다')
          // console.log(this.email)
          FirebaseService.logging(this.email)
          this.$router.replace('/')
          this.$emit('closeModal', false)
          FirebaseService.alert()
          // this.$root.$emit('loggedIn')

        },
        (err) => {
          alert('로그인 정보를 다시 확인해주세요')
        }
      );
      },

      );
    },

    async loginWithGoogle() {
      const result = await FirebaseService.loginWithGoogle();
      this.$store.state.accessToken = result.credential.accessToken;
      this.$store.state.user = result.user;
      alert(this.$store.state.user.displayName);
    },

    async loginWithFacebook() {
      const result = await FirebaseService.loginWithFacebook();
      this.$store.state.accessToken = result.credential.accessToken;
      this.$store.state.user = result.user;
    }
  },

  mounted() {
    // console.log(this.$store.state.user);
    // console.log(this.$session)
    // FirebaseService.logging(this.$session.get("name"), this.$route['path'])
    // FirebaseService.logging(this.$store.state.user.displayName, this.$route['path'])
  }
};
</script>

<style lang="css" scoped>
</style>
