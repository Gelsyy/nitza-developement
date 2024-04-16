function autoGenPass() {
  const length = 10;
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  const digits = "0123456789";
  // const spec = ".-+*%$&#@";
  const spec = "+-@#/.&";
  const all = letters + digits + spec;
  let pass = "";
  let hasDig = false;
  let hasLet = false;
  let hasSpe = false;

  for (let i = 0; i < length; i++) {
    const idx = Math.floor(Math.random() * all.length);
    const char = all.charAt(idx);
    pass += char;

    if (letters.indexOf(char) != -1) {
      hasLet = true;
    } else if (digits.indexOf(char) != -1) {
      hasDig = true;
    } else if (spec.indexOf(char) != -1) {
      hasSpe = true;
    }
  }
  if (!hasLet) {
    const idx = Math.floor(Math.random() * letters.length);
    const char = letters.charAt(idx);
    pass += char;
  }
  if (!hasDig) {
    const idx = Math.floor(Math.random() * digits.length);
    const char = digits.charAt(idx);
    pass += char;
  }
  if (!hasSpe) {
    const idx = Math.floor(Math.random() * spec.length);
    const char = spec.charAt(idx);
    pass += char;
  }
  return pass;
}

document.addEventListener("alpine:init", () => {
  Alpine.data("userPass", () => ({
    passOShow: false,
    pass1Show: false,
    pass2Show: false,

    togglePassO() {
      this.passOShow = !this.passOShow;
    },
    togglePass1() {
      this.pass1Show = !this.pass1Show;
    },
    togglePass2() {
      this.pass2Show = !this.pass2Show;
    },

    randomPass() {
      const pass = autoGenPass();
      this.$refs.pass1.value = pass;
      this.$refs.pass2.value = pass;
    },
  }));

  // pass inputs
  Alpine.bind("passO", () => ({
    "x-ref": "passO",
    ":type"() {
      return this.passOShow ? "text" : "password";
    },
  }));

  Alpine.bind("pass1", () => ({
    "x-ref": "pass1",
    ":type"() {
      return this.pass1Show ? "text" : "password";
    },
  }));

  Alpine.bind("pass2", () => ({
    "x-ref": "pass2",
    ":type"() {
      return this.pass2Show ? "text" : "password";
    },
  }));

  // pass buttons
  Alpine.bind("butPassO", () => ({
    ":class"() {
      return this.passOShow ? "bx bx-show" : "bx bx-hide";
    },
    "@click"() {
      this.togglePassO();
    },
  }));

  Alpine.bind("butPass1", () => ({
    ":class"() {
      return this.pass1Show ? "bx bx-show" : "bx bx-hide";
    },
    "@click"() {
      this.togglePass1();
    },
  }));

  Alpine.bind("butPass2", () => ({
    ":class"() {
      return this.pass2Show ? "bx bx-show" : "bx bx-hide";
    },
    "@click"() {
      this.togglePass2();
    },
  }));
});
