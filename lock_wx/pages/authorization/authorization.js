// pages/authorization/authorization.js
var util = require('../../utils/util.js')
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    users:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var url = "https://www.wyt.cloud/wx_auth/users"
    var data = null
    util.requestFun(url, data).then((res) => {
      return util.requestFun(url, data);
      //Promise队列实现异步函数顺序执行
    }).catch((res) => {
      console.log('错误' + res)
    }).then((res) => {
      app.globalData.users = res.data.users
      this.setData({ users: app.globalData.users})
      console.log(res.data.users);
    }).catch((res) => {
      console.log('错误' + res)
    })
  },
  bindViewTap_del: function (e) {
    var nickname=e.currentTarget.dataset.nickname
    var avatar = e.currentTarget.dataset.avatar
    console.log(nickname)
    var url = "https://www.wyt.cloud/wx_auth/auth_user"
    var data = { "action": "del","avatar":avatar,"nickname":nickname}
    util.requestFun(url, data).then((res) => {
      return util.requestFun(url, data);
      //Promise队列实现异步函数顺序执行
    }).catch((res) => {
      console.log('错误' + res)
    }).then((res) => {
      if (res.data.info == "success") {
        wx.showToast({
          title: res.data.tip,
          icon: 'succes',
          duration: 1000,
          mask: true
        })
      } else {
        wx.showToast({
          title: res.data.tip,
          icon: 'fail',
          duration: 1000,
          mask: true
        })
      }
    }).catch((res) => {
      console.log('错误' + res)
    })
  },

  bindViewTap_ok: function (e) {
    var nickname = e.currentTarget.dataset.nickname
    var avatar = e.currentTarget.dataset.avatar
    console.log(nickname)
    var url = "https://www.wyt.cloud/wx_auth/auth_user"
    var data = { "action": "ok", "avatar": avatar, "nickname": nickname }
    util.requestFun(url, data).then((res) => {
      return util.requestFun(url, data);
      //Promise队列实现异步函数顺序执行
    }).catch((res) => {
      console.log('错误' + res)
    }).then((res) => {
      if (res.data.info == "success") {
        wx.showToast({
          title: res.data.tip,
          icon: 'succes',
          duration: 1000,
          mask: true
        })
      } else {
        wx.showToast({
          title: res.data.tip,
          icon: 'fail',
          duration: 1000,
          mask: true
        })
      }
    }).catch((res) => {
      console.log('错误' + res)
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  bindViewTap: function () {
  
},
})