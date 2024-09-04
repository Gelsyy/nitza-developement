// @ts-check

/** @type {import('alpinejs').default} */
var Alpine;

const ownership = document.getElementById("id_ownership");
const owner = document.getElementById("div_id_owner");

owner?.setAttribute("x-show", "ownership !== 'towit'");

ownership?.setAttribute("x-model", "ownership");

document.addEventListener("alpine:init", () => {
  Alpine.data("createTrailer", () => {
    return {
      ownership: "towit",
    };
  });
});
