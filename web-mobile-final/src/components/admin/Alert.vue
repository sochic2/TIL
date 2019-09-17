<template>
  <div>
    <v-container>
      <h1>공지사항 수정</h1>
      <br>
        <v-textarea
          id="alertcontents"
          v-model = "contents"
          label="내용을 써주세요"
          auto-grow
          outlined
          rows="3"
          row-height="25"
          shaped
          v-on:keyup.enter="intovalue"
        ></v-textarea>
        <div class="text-center">
          <v-btn class="red white--text" @click="intovalue">공지사항 등록</v-btn>
        </div>
    </v-container>
  </div>
</template>

<script>
import FirebaseService from '../../plugins/FirebaseService';

export default {
  name:'Alert',
  data() {
    return {
        contents: '',
        value : '',
    }
  },
  mounted() {
    FirebaseService.getalert().then(res => {
              this.contents = res
            })

  },
  methods: {

    intovalue() {
      FirebaseService.alertchange(this.contents)
    },

  }
}
</script>

<style>
</style>
