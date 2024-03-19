var util = require('../../utils/util.js')
const app = getApp()
Page({
  data: {
    pic:[],
  },
  onLoad:function(){
    var url = "https://www.wyt.cloud/wx_auth/camera"
    var data=null
    util.requestFun(url, data).then((res) => {
      return util.requestFun(url, data);
      //Promise队列实现异步函数顺序执行
    }).catch((res) => {
      console.log('错误' + res)
    }).then((res) => {
      app.globalData.pic=res.data.pic
      this.setData({ pic: app.globalData.pic })
      console.log(res);
    }).catch((res) => {
      console.log('错误' + res)
    })
  },
})
