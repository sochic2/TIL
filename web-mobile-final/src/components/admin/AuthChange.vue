<template>

    <v-menu
      :close-on-content-click="closeOnContentClick"
      :offset-x="offsetX"
      :offset-y="offsetY"
    >
      <template v-slot:activator="{ on }">
          <v-btn
            color="primary"
            dark
            v-on="on"
          >
            권한변경
          </v-btn>
      </template>
      <v-list>
        <v-list-item @click="makeAdmin">
          <v-list-item-title>관리자</v-list-item-title>
        </v-list-item>
        <v-list-item @click="makeNormal">
          <v-list-item-title>새싹회원</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

</template>

<script>
import firebase from "firebase";
import FirebaseService from '../../plugins/FirebaseService';

export default {
  data: () => ({
    closeOnClick: true,
    closeOnContentClick: true,
    offsetX: false,
    offsetY: true,
  }),
  props: {
    id:{type : String}
  },
  methods : {

    makeAdmin(){
      FirebaseService.changeToAdmin(this.id)

    },

    makeNormal() {
      FirebaseService.changeToNormal(this.id)
    },

  }
}
</script>

<style>
</style>
