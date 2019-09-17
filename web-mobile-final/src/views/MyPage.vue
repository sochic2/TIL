<template>
  <v-container>
    <v-layout text-center wrap>
      <v-flex xs12 mb-4>
        <h1 class="display-2 font-weight-bold mb-3">반갑습니다. {{userEmail2}}님</h1>
        <p class="subheading font-weight-regular">
          내 conference, markdown edit를 확인하세요.
          <br />해당 페이지에서 즉시 수정이 가능합니다.
        </p>
      </v-flex>

      <v-flex fluid row>
        <v-switch v-model="switch1" :label="`calendar`"></v-switch>
        <v-switch v-model="switch2" :label="`list`"></v-switch>
      </v-flex>

      <v-flex xs12 v-if="switch1">
        <!-- <v-img :src="require('../assets/logo.svg')" class="my-3" contain height="200"></v-img> -->
        <myCalendar></myCalendar>
      </v-flex>

      <v-flex v-if="switch2">
      <!-- 컨퍼런스 -->
      <!-- 컨퍼런스 컨트롤 테이블 -->
      <v-flex xs12>
        <h2 class="headline font-weight-bold mb-3">Conference Table</h2>

        <v-layout justify-center>
          <!-- table -->
          <v-card width="1000vw">
            <v-card-title>
              Conference
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="search"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table :headers="headers" :items="desserts" :search="search">
              
              <template v-slot:item.title="{ item }">
                <div mb-10 @click="toDetail(item.title)" style="color:blue">{{item.title}}</div>
              </template>

              <template v-slot:item.delete="{ item }">
                <v-icon small @click="unfavorite(item.title)">delete</v-icon>
              </template>
            </v-data-table>
          </v-card>
        </v-layout>
      </v-flex>

      <!-- 마크다운 -->
      <v-flex xs12 class='my-4'>
        <h2 class="headline font-weight-bold mb-3">Markdown</h2>
      </v-flex>
      <v-dialog v-model="dialogm" width="500">
        <template v-slot:activator="{ on }">
      <v-layout row>
          <v-flex xs4 mb-5 v-for="umd in markdowns">
            <h3 class="headline font-weight-bold mb-3">{{umd.date}}</h3>
            <!-- 마크다운 디테일 -->
            <v-btn text v-on="on" color="primary">
              <p v-on:click="abc(umd)">{{umd.title}}</p>
            </v-btn>
          </v-flex>
          </v-layout>
        </template>

        <v-card>
          <v-card-title class="headline grey lighten-2" primary-title>{{markdowntitle}}</v-card-title>
          <v-card-text>
            <v-layout wrap row>
              <v-flex xs12 sm6>
                <viewer :value="umdText" />
              </v-flex>
            </v-layout>
            <p>{{markdowndate}}</p>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text v-on:click="deleteMarkdown(markdownid)">삭제</v-btn>
            <v-btn color="primary" text @click=" dialogm = false">닫기</v-btn>
          </v-card-actions>
        </v-card>
      
      </v-dialog>
    
      </v-flex>
    </v-layout>
    <v-layout text-center wrap class='mx-10'>
    <!-- 마크다운 생성 -->
      <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on }">
          <v-btn justify-center v-on="on">마크다운 생성</v-btn>
        </template>

        <v-card>
          <v-card-title class="headline grey lighten-2" primary-title>마크다운</v-card-title>
          <v-card-text>
            title :
            <input type="text" id="mdtitle" style="height:50px"/>
            <v-layout wrap row>
              <v-flex xs12 sm6>
                <editor v-model="editorText" />
              </v-flex>
              <v-flex xs12 sm6>
                <viewer :value="editorText" />
              </v-flex>
              <v-flex xs12>
                <span>{{editorText}}</span>
              </v-flex>
            </v-layout>date :
            <input type="date" id="mddate" />
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click=" dialog = false" v-on:click="postMarkdown">등록</v-btn>
            <v-btn color="primary" text @click=" dialog = false">닫기</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </v-container>
</template>

<script>
import firebase from "firebase";
import myCalendar from "../components/calendars/MyCalendar";
import FirebaseService from "../plugins/FirebaseService";
import "tui-editor/dist/tui-editor.css";
import "tui-editor/dist/tui-editor-contents.css";
import "codemirror/lib/codemirror.css";
import { Editor, Viewer } from "@toast-ui/vue-editor";

export default {
  components: {
    editor: Editor,
    viewer: Viewer,
    myCalendar
  },
  props: {
    text: { type: String }
  },
  data: () => ({
    userEmail: "",
    userEmail2: "",
    userConference: [],
    dialog: false,
    dialogm: false,
    editorText: "",
    umdText: "",
    markdowns: [],
    markdowntitle: [],
    markdowndate: [],
    markdownid: [],
    // switch
    switch1: true,
    switch2: true,

    // table data
    search: "",
    headers: [
      {
        text: "Conferences",
        align: "left",
        sortable: false,
        value: "title"
      },
      { text: "Host", value: "host" },
      { text: "Field", value: "field" },
      { text: "Target", value: "target" },
      { text: "Start", value: "start" },
      { text: "End", value: "end" },
      { text: "Delete", value: "delete"}
    ],
    desserts: []
    //
  }),
  created() {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        // User is signed in.

        this.userEmail = user.email;
        this.userEmail2 = this.userEmail.split('@')[0]
        this.getUserConference(user.email);

        this.getUserMarkdowns(user.email);
      } else {
        // No user is signed in.
        this.userEmail = "Guest";
      }
    });
  },
  methods: {
    postMarkdown() {
      //user,content,date
      FirebaseService.postMarkdown(
        this.userEmail,
        mdtitle.value,
        this.editorText,
        mddate.value
      ).then(() => {
        location.href = "/mypage";
      });
    },

    // Conference Detail
    async getConferenceDetail(con_param) {
      const conDe = await FirebaseService.getConference(con_param);
      this.userConference.push({
        conference: conDe
      });
      // table에 들어가는 Conference
      this.desserts.push({
        title: conDe.title,
        host: conDe.host,
        field: conDe.field,
        target: conDe.target,
        start: conDe.start,
        end: conDe.end,
        delete: ""
      });
    },

    // 사용자 별 ConferenceID
    async getUserConference(user_param) {
      const userCon = await FirebaseService.getUserConference(user_param);
      userCon.forEach(eachCon => {
        this.getConferenceDetail(eachCon);
      });
    },

    // user의 markdown 가져오기
    async getUserMarkdowns(user_param) {
      const usermarkdowns = await FirebaseService.getMarkdowns(user_param);
      usermarkdowns.forEach(um => {
        this.markdowns.push({
          title: um.title,
          date: um.date,
          content: um.content,
          id: um.id
        });
      });

    },

    deleteMarkdown(md_id) {
      FirebaseService.deleteMarkdown(this.userEmail, md_id).then(() => {
        location.href = "/mypage";
      });
    },

    // 마크다운 에디터에 정보 가져오기
    abc(umd) {
      this.markdowntitle = umd.title
      this.markdownid = umd.id
      this.markdowndate = umd.date
      this.umdText = umd.content;
    },

    unfavorite(conf_id) {
      FirebaseService.deleteMyConference(conf_id, this.userEmail)
      FirebaseService.deleteUserToConference(conf_id, this.userEmail)
      .then(() => {
        location.href='myPage'
      })
    },
    toDetail(url) {
      location.href='/conference/'+url
    },

  }
};
</script>

<style>
</style>
