//index.js
//获取应用实例
const app = getApp()


Page({
  data: {
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    iv: '',
    encryptedData: '',
    code: '',
    cookie:'',
  },
  //事件处理函数
  onLoad: function () {
    if (app.globalData.userInfo && app.globalData.iv && app.globalData.encryptedData && app.globalData.code) {
      this.setData({
        userInfo: app.globalData.userInfo,
        iv: app.globalData.iv,
        encryptedData: app.globalData.encryptedData,
        code: app.globalData.code,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          iv: res.iv,
          encryptedData: res.encryptedData,
          code: app.globalData.code,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          app.globalData.code = app.globalData.code
          app.globalData.iv = res.iv
          app.globalData.encryptedData = res.encryptedData
          this.setData({
            code: app.globalData.code,
            userInfo: res.userInfo,
            iv: res.iv,
            encryptedData: res.encryptedData,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function (e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    app.globalData.iv=e.detail.iv
    app.globalData.encryptedData=e.detail.encryptedData
    this.setData({
      userInfo: e.detail.userInfo,
      iv:e.detail.iv,
      code:app.globalData.code,
      encryptedData:e.detail.encryptedData,
      hasUserInfo: true
    })
  },
  bindViewTap: function () {
    console.log(this.data.iv)
    wx.request({
      url: 'https://www.wyt.cloud/wx_auth/wx_login',
      method: "POST",//指定请求方式，默认get
      data: { "code": this.data.code, "encrypted_data":     this.data.encryptedData, "iv": this.data.iv },
      success: function (res) {
        console.log(res.header["Set-Cookie"])
        app.globalData.cookie = res.header["Set-Cookie"]
      }
    });
    wx.switchTab({
      url: '../main/main'
    })
  },
})
