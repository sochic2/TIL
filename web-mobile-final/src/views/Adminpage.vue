<template>
  <div class="mt-5">
    <!-- admin header.. -->
    <v-container>
      <v-tabs >
        <v-tab v-on:click="ChangeToUsers">User</v-tab>
        <v-tab v-on:click="ChangeToConferences">Conference</v-tab>
      </v-tabs>

    <!-- admin table -->
      <v-data-table
          :headers="headers"
          :items="contents"
          :items-per-page="5"
          class="elevation-1"
        >
        <template v-slot:item.title="{ item }">
          <div mb-10 @click="goDetail(item.title)" style="color:blue">{{item.title}}</div>
        </template>
        <template v-slot:item.action="{ item }">
          <AuthChange :id="item.id"></AuthChange>
        </template>

      </v-data-table>
    </v-container>

    <Alert></Alert>
  </div>


</template>

<script>
import firebase from "firebase";
import FirebaseService from '../plugins/FirebaseService';
import AuthChange from '../components/admin/AuthChange'
import Alert from '../components/admin/Alert'
  export default {
    name : 'AdminPageCopy',
    components : {
      AuthChange,
      Alert,
    },
    data () {
      return {
        headers: [],
        contents: [],
        adminUserscontents: [],
        adminConferencecontents: [],
        conferences_headers: [
          {
            text: 'title',
            align: 'left',
            sortable: true,
            value: 'title'
          },
          {text: 'start', value: 'start'},
          {text: 'end', value: 'end'},
        ],

        users_headers: [
          {
            text: 'id',
            align: 'left',
            sortable: false,
            value: 'id',
          },
          { text: '권한', value: '권한' },
          { text: '권한변경', value: 'action', sortable: false },
        ],


      }
    },
    methods : {
      // conference title 누르면 디테일 페이지로
      goDetail(title) {
        location.href = '/conference/'+title
      },

      async getAdminUsers() {
        this.adminUserscontents = await FirebaseService.getUsers()
        this.ChangeToUsers()
      },
      // Conference 가져오기
      async getAdminConferences() {
          this.adminConferencecontents = await FirebaseService.getConferences()
      },
      // 상위 버튼 누르면 전환되기
      ChangeToUsers () {
        this.headers = this.users_headers
        this.contents = this.adminUserscontents
      },
      ChangeToConferences() {
        this.headers = this.conferences_headers
        this.contents = this.adminConferencecontents
      },
    },
    mounted() {
      this.getAdminUsers()
      this.getAdminConferences()
    }
  }

</script>

<style>


</style>
