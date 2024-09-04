// @ts-check

/** @type {import('alpinejs').default} */
var Alpine;

const contractType = document.getElementById("id_contract_type");
const totalAmount = document.getElementById("div_id_total_amount");
const label = document.querySelector('label[for="id_security_deposit"]');
const version = document.querySelector("#div_id_template_version");        
const insurancedCheckbox = document.getElementById('id_insuranced');
const insuranceDetailsDiv = document.getElementById('div_id_insurance_details');


contractType?.setAttribute("x-model", "contractType");
totalAmount?.setAttribute("x-show", "contractType == 'lto'");
insuranceDetailsDiv?.setAttribute("x-show", "insurancedCheckbox");
label?.setAttribute(
  "x-text",
  "contractType == 'lto' ? 'Down payment*' : 'Security deposit*'",
);
version?.setAttribute("x-show", 'contractType == "rent"');
version?.setAttribute("x-cloak", "true");
insurancedCheckbox?.setAttribute("x-model", "insurancedCheckbox");
totalAmount?.setAttribute("x-cloak", "true");

document.addEventListener("alpine:init", () => {
  Alpine.data("createContract", () => {
    return {
      contractType: "rent",
      insurancedCheckbox: false
    };
  });
});
