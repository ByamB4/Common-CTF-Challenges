Java.perform(function () {
  let hook = Java.use("mn.chall.challname.ui.screens.PasswordViewModel");
  hook["submit"].implementation = function (arg) {
    console.log("hook: " + arg);
    let ret = this.submit(arg);
    return ret;
  };
});
